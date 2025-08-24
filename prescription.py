from difflib import restore
import numpy as np
import re
import os
import pickle
import argparse
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Bidirectional, Dropout, Masking, LayerNormalization, SpatialDropout1D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

from data import sentences, test

MODEL_PATH = 'prescription_ner_model.keras'
TOKENIZER_PATH = 'tokenizer.pkl'
LABELS_PATH = 'labels.pkl'

def prepare_training_data(sentences, labels):
    tokenizer = Tokenizer(lower=False, filters='')
    tokenizer.fit_on_texts(sentences)
    X = tokenizer.texts_to_sequences(sentences)
    word2idx = tokenizer.word_index

    all_labels = sorted(list(set(l for label_seq in labels for l in label_seq)))
    label2idx = {l: i for i, l in enumerate(all_labels)}
    idx2label = {i: l for l, i in label2idx.items()}
    O_INDEX = label2idx.get('O', 0)

    maxlen = max(len(seq) for seq in X)
    X = pad_sequences(X, maxlen=maxlen, padding='post')
    y = pad_sequences([[label2idx[l] for l in seq] for seq in labels],
                      maxlen=maxlen, padding='post', value=O_INDEX)
    y = np.array([to_categorical(i, num_classes=len(all_labels)) for i in y])

    return X, y, tokenizer, label2idx, idx2label, maxlen, word2idx


def prepare_data(sentences, labels, tokenizer, label2idx, maxlen):
    O_INDEX = label2idx.get('O', 0)
    X = tokenizer.texts_to_sequences(sentences)
    X = pad_sequences(X, maxlen=maxlen, padding='post')
    y = pad_sequences([[label2idx.get(l, O_INDEX) for l in seq] for seq in labels],
                      maxlen=maxlen, padding='post', value=O_INDEX)
    y = np.array([to_categorical(i, num_classes=len(label2idx)) for i in y])
    return X, y

def create_model(vocab_size, n_tags, maxlen):
    model = Sequential([
        Embedding(vocab_size + 1, 64, input_length=maxlen, mask_zero=True),
        Masking(mask_value=0),
        Bidirectional(LSTM(200, return_sequences=True, dropout=0.3, recurrent_dropout=0.2)),
        Dropout(0.3),
        LayerNormalization(),
        TimeDistributed(Dense(n_tags, activation='softmax'))
    ])
    model.compile(optimizer=Adam(0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def extract_info_with_pattern(text, patterns):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            group = match.group(1) if match.lastindex else match.group(0)
            try:
                value = float(group)
                return value * (7 if 'tuần' in match.group(0).lower() else 1)
            except ValueError:
                return group.strip()  # Return raw string for non-numeric values
    return None

def extract_entities(sentence, model, tokenizer, idx2label, maxlen):
    # Predict labels
    seq = pad_sequences(tokenizer.texts_to_sequences([sentence]), maxlen=maxlen, padding='post')
    pred_labels = [idx2label[int(np.argmax(p))] for p in model.predict(seq, verbose=0)[0]]
    tokens = sentence.split()
    pred_labels = pred_labels[:len(tokens)]
    
    # Initialize result
    result = {key: [] for key in ['FREQ', 'DOSE', 'DUR', 'UNIT', 'NOTE']}
    
    # Extract entities and notes from parentheses
    for token, label in zip(tokens, pred_labels):
        if label in result:
            result[label].append(token)
    
    # Pattern matching for fallback
    text = ' '.join(tokens)
    patterns = {
        'freq': [
            r'(?:mỗi|/)\s*ngày\s*(\d+)\s*lần',
            r'(\d+)\s*lần/ngày',
            r'ngày\s*(\d+)\s*lần',
            r'(\d+)\s*lần\s*mỗi\s*ngày'
        ],
        'dose': [
            r'(?:mỗi|/)\s*lần\s*(\d+)\s*(?:v|viên|v/lần|viên/lần)',
            r'(?:^|\s)(\d+)\s*(?:v|viên)/lần',
            r'(?:^|\s)(\d+)\s*(?:v|viên)(?:\s|$)',
            r'uống\s*(\d+)\s*(?:v|viên)',
            r'(?:^|\s)(\d+)\s*(?:v/l|viên/l)',
            r'lần\s*(\d+)\s*(?:v|viên|v/lần|viên/lần)'
        ],
        'dur': [
            r'(?:trong|kéo dài|dùng)\s*(\d+)\s*(?:ngày|tuần)',
            r'(\d+)\s*(?:ngày|tuần)',
            r'(?:trong\s+)?(?:vòng\s+)?(\d+)\s*(?:ngày|tuần)'
        ],
        'unit': [
            r'\b(v|viên|gói|ống|ml|mg|g)\b',
            r'\b(v|viên|gói|ống|ml|mg|g)/lần'
        ],
        'note': [
            r'\((.*?)\)'
        ]
    }
    
    # Extract values using patterns
    values = {
        'freq': extract_info_with_pattern(text, patterns['freq']),
        'dose': extract_info_with_pattern(text, patterns['dose']),
        'dur': extract_info_with_pattern(text, patterns['dur']),
        'unit': extract_info_with_pattern(text, patterns['unit']),
        'note': extract_info_with_pattern(text, patterns['note'])
    }
    
    # Calculate total pills
    total_pills = None
    freq = values['freq']
    dose = values['dose']
    dur = values['dur']
    if freq is not None and dose is not None and dur is not None:
        total_pills = int(freq * dose * dur)
    
    return {
        'FREQ': result['FREQ'],
        'DOSE': result['DOSE'],
        'DUR': result['DUR'],
        'UNIT': result['UNIT'],
        'NOTE': result['NOTE'],
        'frequency': values['freq'],
        'dose': values['dose'],
        'duration': values['dur'],
        'unit': values['unit'],
        'total_pills': total_pills,
        'notes': values['note']
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train or load the prescription NER model.')
    parser.add_argument('--retrain', action='store_true', help='Force retrain the model from scratch')
    args = parser.parse_args()

   # Split the data into train/val/test
    train_data, temp_data = train_test_split(sentences, test_size=0.3, random_state=42)
    val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)
    train_sents = [s for s, l in train_data]
    train_labels = [l for s, l in train_data]

    val_sents = [s for s, l in val_data]
    val_labels = [l for s, l in val_data]

    test_sents = [s for s, l in test_data]
    test_labels = [l for s, l in test_data]


    # Prepare training data
    X, y, tokenizer, label2idx, idx2label, maxlen, word2idx = prepare_training_data(train_sents, train_labels)

    # Prepare validation data
    val_X, val_y = prepare_data(val_sents, val_labels, tokenizer, label2idx, maxlen)
    test_X, test_y = prepare_data(test_sents, test_labels, tokenizer, label2idx, maxlen)

    should_load_model = all(os.path.exists(f) for f in [MODEL_PATH, TOKENIZER_PATH, LABELS_PATH]) and not args.retrain

    if should_load_model:
        print("Loading existing model...")
        model = load_model(MODEL_PATH)
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer = pickle.load(f)
        with open(LABELS_PATH, 'rb') as f:
            label2idx, idx2label, maxlen = pickle.load(f)
    else:
        print("Training new model...")
        model = create_model(len(word2idx), len(label2idx), maxlen)
        model.fit(X, y,
                  validation_data=(val_X, val_y),
                  batch_size=32,
                  epochs=500,
                  verbose=1,
                  callbacks=[EarlyStopping(monitor='val_loss', patience=15, verbose=1)])
        
        model.save(MODEL_PATH)
        with open(TOKENIZER_PATH, 'wb') as f:
            pickle.dump(tokenizer, f)
        with open(LABELS_PATH, 'wb') as f:
            pickle.dump((label2idx, idx2label, maxlen), f)

    # Evaluate model on validation set
    val_loss, val_acc = model.evaluate(val_X, val_y, verbose=1)
    print(f"\nValidation Loss: {val_loss:.4f}, Accuracy: {val_acc:.4f}")

    # Evaluate model on test set
    test_loss, test_acc = model.evaluate(test_X, test_y, verbose=1)
    print(f"\nTest Loss: {test_loss:.4f}, Test Accuracy: {test_acc:.4f}")

    # Test the model
    for count, sentence in enumerate(test, 1):
        print(f"Sentence: {count}")
        print(sentence)
        print(f"{extract_entities(sentence, model, tokenizer, idx2label, maxlen)}\n")

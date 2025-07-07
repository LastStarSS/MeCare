import re
import data

class PrescriptionExtractor:
    def __init__(self):
        # Dictionary to normalize abbreviations and variants
        self.abbreviations = {
            "mn": "mỗi ngày",
            "ml": "mỗi lần",
            "sa": "sau ăn",
            "1v": "1 viên",
            "3l": "3 lần",
            "l/ngày": "lần mỗi ngày",
            "x/ngày": "lần mỗi ngày",
            "x": "lần",
        }

        # Patterns for prescription extraction
        self.freq_patterns = [
            r'(\d+)\s*(lần|ngày)',
            r'(mỗi|cách)\s*(\d+)\s*(giờ|ngày)',
        ]

        self.dose_patterns = [
            r'(mỗi\s*lần\s*\d+\s*(viên|ml|mg|g|ống|giọt))',
            r'(\d+(\.\d+)?)(\s*)(viên|ml|mg|g|ống|giọt)',
        ]

        self.duration_patterns = [
            r'(trong|kéo dài|dùng)\s*(\d+)\s*(ngày|tuần|tháng)',
            r'(\d+)\s*(ngày|tuần|tháng)',
        ]

        self.note_patterns = [
            r'\(.*?\)',  # anything inside parentheses as instructions
            r'(uống\s*(trước|sau)\s*ăn)',
            r'(khi\s*đau|\s*buổi\s*(sáng|tối))',
        ]

    def normalize_text(self, text):
        for abbr, full in self.abbreviations.items():
            text = re.sub(r'\b' + re.escape(abbr) + r'\b', full, text, flags=re.IGNORECASE)
        return text

    def extract(self, text):
        text = self.normalize_text(text)
        freq = self._extract_first(self.freq_patterns, text)
        dose = self._extract_first(self.dose_patterns, text)
        duration = self._extract_first(self.duration_patterns, text)
        note = self._extract_first(self.note_patterns, text)

        return {
            'frequency': freq,
            'dose': dose,
            'duration': duration,
            'note': note
        }

    def _extract_first(self, patterns, text):
        for pat in patterns:
            match = re.search(pat, text, re.IGNORECASE)
            if match:
                return match.group(0).strip().lower()
        return None


# Example usage
if __name__ == "__main__":
    extractor = PrescriptionExtractor()
    for sample in data.data:
        result = extractor.extract(sample)
        print(result)
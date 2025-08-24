test = ["Uống ngày 23 lần, lần 12 viên, trong 53 ngày"
        ]
# "Uống mỗi ngày 1 lần, mỗi lần 1 viên (tối), trong 14 ngày.",
#         "Uống lần 2 viên, ngày 2 lần, trong 10 ngày.",
#         "Uống trong 5 ngày, lần 3 viên, ngày 2 lần.",
#         "Uống ngày 2 lần, trong 21 ngày, lần 3 viên.",
#         "Uống lần 1 viên, trong 7 ngày, ngày 2 lần."

# "(Tiêm kháng viêm khớp gối trái tại phòng khám), trong 1 ngày"
# "Uống  mỗi ngày 1 lần, mỗi lần 1 Viên (tối TÁC DỤNG PHỤ: CHÓNG MẶT - Nếu chóng mặt nhiều => uống cách ngày - Nếu chóng mặt nhiều, không chịu nổi tác dụng phụ => ngưng thuốc, tái khám), trong 14 ngày.",
#         "Uống 1 tuần 1 viên (Uống cố định vào CHỦ NHẬT HẰNG TUẦN  (uống vào buổi sáng sau khi ngủ dậy trước ăn  30 phút, uống với 1 ly nước lọc đầy 200ml, uống trong khi bệnh nhân đang ngồi hoặc đứng ở tư thế thẳng, không nằm nghĩ trong vòng 1 giờ sau khi uống).), trong 28 ngày).",
#         "(Tiêm HA khớp gối  (T)  tại phòng khám), trong 1 ngày",
#         "ĐẶT ÂM ĐẠO CÁCH 2 ĐÊM 1 LẦN, MỖI LẦN 01 VIÊN (TỐI TRƯỚC NGỦ)",
#         "Rửa âm hộ ngày 2 lần (sáng. tối)",
#         "Nhỏ mắt  mỗi ngày 6 lần, mỗi lần 1 giọt (hai mắt), trong 14 ngày.",
#         "-Bôi ngoài da tại cột  thắt lưng, một lớp mỏng vừa đủ,  mỗi ngày bôi 3 lần ( sáng, trưa, tối trước khi ngủ).  -Không bôi dầu nóng vào vị trí đau.), trong 14 ngày"

sentences = [
    ("Uống mỗi ngày 2 lần, mỗi lần 1 Gói (sau ăn sáng, chiều 2 giờ), trong 28 ngày (Từ 31/12/2021 - 27/01/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên (trước ăn sáng 30 phút).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 viên, trong 5 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Đặt âm đạo mỗi ngày 1 lần, mỗi lần 1 viên (tối trước ngủ).",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 viên (tối), trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "O", "DUR", "DUR"]),

    ("Uống ngày 2 lần, mỗi lần 2 viên, trong 10 ngày.",
     ["O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Xịt mũi mỗi ngày 3 lần, mỗi lần 2 nhát, trong 5 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi sáng 1 viên, tối 1 viên.",
     ["O", "O", "FREQ", "DOSE", "UNIT", "FREQ", "DOSE", "UNIT"]),

    ("Nhỏ mắt mỗi ngày 4 lần, mỗi lần 1 giọt.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),

    ("Ngậm dưới lưỡi mỗi ngày 2 lần, mỗi lần 1 viên.",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),

    ("Tiêm bắp 1 ống/1 lần x 3 lần/tuần.",
     ["O", "O", "DOSE", "UNIT", "DOSE", "O", "FREQ", "FREQ"]),

    ("Xịt họng 2 nhát/lần x 3 lần/ngày.",
     ["O", "O", "DOSE", "UNIT", "O", "FREQ", "FREQ"]),

    ("Uống 1 viên/lần, 2 lần/ngày.",
     ["O", "DOSE", "UNIT", "FREQ", "FREQ"]),

    ("Dán 1 miếng/lần, 1 lần/ngày.",
     ["O", "DOSE", "UNIT", "FREQ", "FREQ"]),

    ("Đặt hậu môn mỗi ngày 1 lần, mỗi lần 1 viên.",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 5 ml (sáng tối), trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 gói (tối 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng, chiều sau ăn), trong 28 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 3 lần, mỗi lần 1 Viên (Trước ăn sáng, trưa, chiều), trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (trong khi ăn sáng)",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Ống (sáng), trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 gói (sáng chiều), trong 30 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Gói (Sau ăn sáng), trong 28 ngày (Từ 05/04/2021 - 02/05/2021).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 3 lần, mỗi lần 1 gói (trước ăn 30 phút sáng, trưa, tối), trong 14 ngày (Từ 19/05/2020 - 01/06/2020)",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng chiều), trong 14 ngày (Từ 12/02/2022 - 25/02/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống  mỗi ngày 2 lần, mỗi lần 1 Viên, trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng), trong 14 ngày (Từ 30/05/2020 - 12/06/2020).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("bôi ngoài âm hộ ngày 2 lần",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ"]),

    ("Rửa âm hộ ngày 2 lần (sáng. tối)",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (tối), trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 gói, trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 2 lần, mỗi lần 2 gói, trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 3 gói, trong 21 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (sau ăn chiều), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Ống (sáng, tối 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Chườm ấm mắt mỗi ngày 1 lần, mỗi lần 1 Gói, trong 14 ngày. (tối)",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên ((sau ăn) sáng , chiều), trong 14 ngày (Từ 08/11/2021 - 21/11/2021).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (sáng sau ăn), trong 30 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 3 lần, mỗi lần 2 viên, trong 10 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 6 lần, mỗi lần 3 viên, trong 19 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 5 viên, trong 30 ngày (sáng).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR", "NOTE"]),

    ("Uống mỗi ngày 2 lần (tối), mỗi lần 1 viên, trong 12 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "NOTE", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên (sáng), trong 2 tháng.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 5 tháng.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 33 lần, mỗi lần 10 viên, trong 30 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 25 lần, mỗi lần 13 viên, trong 22 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 5 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 21 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 viên (sáng)",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 3 viên",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),
    
    ("Uống mỗi ngày 5 lần, mỗi lần 1 viên",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 5 ml",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 viên ",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 3 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 13 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống trong 5 ngày, lần 2 viên, ngày 1 lần.",
     ["O", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống trong 14 ngày, lần 3 viên, ngày 2 lần.",
     ["O", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống trong 21 ngày, lần 2 viên, ngày 3 lần.",
     ["O", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống trong 30 ngày, lần 1 viên, ngày 3 lần.",
     ["O", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống trong 10 ngày, ngày 4 lần, lần 1 viên.",
     ["O", "O", "DUR", "DUR", "FREQ", "FREQ", "FREQ", "DOSE", "DOSE", "UNIT"]),
    
    ("Uống lần 3 viên, trong 10 ngày, ngày 2 lần.",
     ["O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống lần 2 viên, trong 14 ngày, ngày 3 lần.",
     ["O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR", "FREQ", "FREQ", "FREQ"]),
    
    ("Uống lần 2 viên, ngày 2 lần, trong 14 ngày.",
     ["O", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống lần 1 viên, ngày 3 lần, trong 7 ngày.",
     ["O", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống lần 2 viên, ngày 3 lần, trong 21 ngày.",
     ["O", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống lần 3 viên, ngày 1 lần, trong 21 ngày.",
     ["O", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống ngày 2 lần, trong 10 ngày, lần 3 viên.",
     ["O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT"]), 

    ("Uống ngày 3 lần, trong 21 ngày, lần 5 viên.",
     ["O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT"]),
    
    ("Uống ngày 1 lần, trong 7 ngày, lần 2 viên.",
     ["O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT"]),

    ("Uống ngày 3 lần, trong 14 ngày, lần 1 viên.",
     ["O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR", "DOSE", "DOSE", "UNIT"]),
    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên ((sau ăn) sáng , chiều), trong 7 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (trong khi ăn sáng), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1/2 Viên (tối 20h), trong 30 ngày (Từ 22/01/2021 - 20/02/2021).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng - chiều), trong 14 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Nhỏ mắt mỗi ngày 6 lần, mỗi lần 1 giọt (hai mắt), trong 7 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Tra mắt mỗi ngày 3 lần, mỗi lần 1 Một lượng vừa đủ (hai mắt), trong 14 ngày",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "DOSE", "DOSE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sau ăn sáng chiều), trong 14 ngày (Từ 04/03/2021 - 17/03/2021).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng chiều sau ăn), trong 7 ngày (Từ 01/06/2020 - 07/06/2020).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 2 Viên (tôi 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (sáng trước ăn 30 phút), trong 2 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sau ăn sáng, chiều), trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 Viên (sáng chiều sau ăn), trong 14 ngày (Từ 04/03/2022 - 17/03/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng chiều sau ăn), trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Đặt âm đạo mỗi ngày 1 lần, mỗi lần 1 Viên (tối trước ngủ), trong 6 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Dùng ngoài mỗi ngày 1 lần, mỗi lần 1 Gói (buổi tối), trong 10 ngày",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sau ăn trưa, tối),",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Đặt âm đạo cách 2 đêm 1 lần, mỗi lần 01 viên (tối trước ngủ)",
     ["O", "O", "NOTE", "NOTE", "NOTE", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng chiều sau ăn), trong 14 ngày (Từ 31/07/2020 - 13/08/2020).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sau ăn sáng, chiều), trong 5 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (tôi 20h), trong 40 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Thoa mỗi ngày 1 lần, mỗi lần 1 lớp mỏng, trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "UNIT", "O", "DUR", "DUR"]),

    ("Uống sáng 1 viên, chiều 1 viên, tối 1 viên, trong 10 ngày.",
     ["O", "FREQ", "DOSE", "UNIT", "FREQ", "DOSE", "UNIT", "FREQ", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống cách ngày 1 viên, trong 1 tuần.",
     ["O", "FREQ", "FREQ", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 viên, dùng liên tục trong 3 tháng.",
     ["O", "FREQ", "FREQ", "DOSE", "UNIT", "O", "O", "O", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần vào buổi sáng, trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 viên, trong 3 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 3 lần, mỗi lần 1 viên, trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (TÁC DỤNG PHỤ: Buồn nôn, nếu buồn nôn => cách ngày), trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE",
      "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("(Dùng khi đau), trong 14 ngày.",
     ["NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("(Uống khi buồn nôn), trong 2 ngày.",
     ["NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("(Tiêm khi đến phòng khám), trong 3 ngày.",
     ["NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("Uống 1 tuần 2 viên, trong 10 ngày",
     ["O", "FREQ", "FREQ", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 viên, trong 5 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Đặt âm đạo mỗi ngày 1 lần, mỗi lần 1 viên (tối trước ngủ)",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE"]),
    
    ("Bôi ngoài da mỗi sáng và tối, trong 7 ngày.",
     ["O", "O", "O", "O", "FREQ", "O", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống mỗi sáng 2 viên, trong 3 ngày.",
     ["O", "O", "FREQ", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Ngậm mỗi ngày 3 lần, mỗi lần 1 viên, trong 10 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Nhỏ mũi mỗi ngày 2 lần, mỗi lần 2 giọt, trong 5 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Tiêm bắp 1 ống mỗi ngày.",
     ["O", "O", "DOSE", "UNIT", "FREQ", "FREQ"]),
    
    ("Bôi thuốc vào vết thương mỗi sáng.",
     ["O", "O", "O", "O", "O", "O", "FREQ"]),
    
    ("Dán 1 miếng mỗi 12 giờ.",
     ["O", "DOSE", "UNIT", "O", "FREQ", "FREQ"]),
    
    ("Xịt họng mỗi ngày 3 lần, mỗi lần 1 nhát, trong 5 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "O", "DUR", "DUR"]),
    
    ("Uống 1 viên trước ăn sáng, trong 14 ngày.",
     ["O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("Rửa mũi mỗi tối bằng nước muối.",
     ["O", "O", "O", "FREQ", "O", "O", "O"]),
    
    ("Ngậm 2 viên mỗi 8 giờ.",
     ["O", "DOSE", "UNIT", "O", "FREQ", "FREQ"]),
    
    ("Bơm thuốc vào trực tràng mỗi tối, trong 6 ngày.",
     ["O", "O", "O", "O", "O", "O", "FREQ", "O", "DUR", "DUR"]),
    
    ("Tiêm mỗi ngày 1 lần.",
     ["O", "O", "FREQ", "FREQ", "FREQ"]),
    
    ("Xịt mũi mỗi ngày 2 lần, trong 7 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống thuốc mỗi sáng và chiều.",
     ["O", "O", "O", "FREQ", "O", "FREQ"]),
    
    ("Nhỏ 2 giọt vào mỗi mắt, mỗi ngày 3 lần.",
     ["O", "DOSE", "UNIT", "O", "O", "O", "O", "FREQ", "FREQ", "FREQ"]),
    
    ("Thoa thuốc mỗi ngày sau khi tắm.",
     ["O", "O", "O", "FREQ", "O", "O", "O"]),
    
    ("Ngậm 1 viên buổi tối trước khi ngủ.",
     ["O", "DOSE", "UNIT", "O", "FREQ", "O", "O", "O"]),
    
    ("Uống 3 viên sáng và tối trong 5 ngày.",
     ["O", "DOSE", "UNIT", "FREQ", "O", "FREQ", "O", "DUR", "DUR", "O"]),
    
    ("Xịt họng mỗi sáng 2 nhát.",
     ["O", "O", "O", "FREQ", "DOSE", "UNIT"]),
    
    ("Uống 1 gói trước ăn, trong 10 ngày.",
     ["O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("Bôi 1 lớp mỏng lên vùng da bị bệnh mỗi ngày.",
     ["O", "DOSE", "UNIT", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "FREQ", "FREQ"]),
    
    ("Đặt 1 viên sâu trong âm đạo vào buổi tối.",
     ["O", "DOSE", "UNIT", "O", "O", "O", "O", "O", "O", "FREQ"]),
    
    ("Nhỏ mũi 3 lần mỗi ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "FREQ"]),
    
    ("Tiêm thuốc mỗi 6 giờ.",
     ["O", "O", "O", "FREQ", "FREQ"]),
    
    ("Dán 1 miếng vào ngực mỗi tối.",
     ["O", "DOSE", "UNIT", "O", "O", "FREQ", "FREQ"]),
    
    ("Ngậm 1 viên mỗi 12 giờ trong 7 ngày.",
     ["O", "DOSE", "UNIT", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),
    
    ("Uống 1 viên cách nhau 8 giờ.",
     ["O", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "FREQ"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (tôi 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),
    
    ("Uống mỗi ngày 1 lần, mỗi lần 1/2 Viên (tôi 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (Sáng - chiều sau ăn.), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Nhỏ tai mỗi ngày 3 lần, mỗi lần 3 giọt (2 tai), trong 7 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng , chiều), trong 28 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Nhỏ mắt mỗi ngày 4 lần, mỗi lần 1 giọt (hai mắt), trong 30 ngày (Từ 19/02/2022 - 20/03/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Nhỏ mắt mỗi ngày 6 lần, mỗi lần 1 giọt, trong 10 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (sáng, tôi 20h), trong 21 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Ống (sáng , tôi 20h), trong 15 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 3 lần, mỗi lần 1 Viên (sáng trưa chiều), trong 7 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (sau ăn chiều), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng , chiều), trong 28 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (tối trước khi ngủ), trong 7 ngày (Từ 28/10/2020 - 03/11/2020).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên ((sau ăn) sáng , chiều), trong 7 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng - chiều), trong 14 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 1 lần, mỗi lần 1 Viên (tối sau ăn), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn 30 phút sáng - chiều), trong 14 ngày",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Viên (trước ăn sáng chiều 30 phút), trong 28 ngày (Từ 03/05/2022 - 30/05/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Bôi mỗi ngày 2 lần, mỗi lần 1 Một lớp mỏng, bôi da khi ngứa trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "DOSE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 Viên (sáng chiều , trong 14 ngày (Từ 18/02/2022 - 03/03/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "UNIT", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 1 Gói (sau ăn sáng, chiều 2 giờ), trong 28 ngày (Từ 31/12/2021 - 27/01/2022).",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR", "NOTE", "NOTE", "NOTE", "NOTE"]),

    ("Đặt âm đạo mỗi ngày 1 lần, mỗi lần 1 Viên (tối trước ngủ), trong 6 ngày.",
     ["O", "O", "O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Uống mỗi ngày 2 lần, mỗi lần 2 Viên (sau ăn sáng chiều), trong 28 ngày.",
     ["O", "O", "FREQ", "FREQ", "FREQ", "O", "DOSE", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "NOTE", "O", "DUR", "DUR"]),

    ("Ngậm dưới lưỡi mỗi 4 giờ 1 Viên, liên tục trong 5 ngày.",
     ["O", "O", "O", "O", "FREQ", "FREQ", "DOSE", "UNIT", "O", "O", "O", "DUR", "DUR"]),

    ("Xịt mũi mỗi bên 2 nhát, ngày 2 lần, dùng trong 7 ngày.",
     ["O", "O", "DOSE", "DOSE", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "O", "DUR", "DUR"]),

    ("Bôi ngoài da 1 lớp mỏng mỗi ngày 1 lần trong 10 ngày.",
     ["O", "O", "O", "DOSE", "UNIT", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Tiêm bắp 1 ống/lần, ngày 2 lần, trong 3 ngày.",
     ["O", "O", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Uống 1 gói sau ăn sáng mỗi ngày trong 14 ngày.",
     ["O", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "O", "O", "DUR", "DUR"]),

    ("Nhỏ mắt 1 giọt/lần, ngày 3 lần, trong 5 ngày.",
     ["O", "O", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Ngậm 1 viên mỗi 6 giờ trong 4 ngày.",
     ["O", "DOSE", "UNIT", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Thoa thuốc lên vùng da bị bệnh mỗi tối trong 7 ngày.",
     ["O", "O", "O", "O", "O", "O", "O", "O", "FREQ", "O", "DUR", "DUR"]),

    ("Tiêm dưới da 1 ống, mỗi ngày 1 lần, trong 5 ngày.",
     ["O", "O", "O", "DOSE", "UNIT", "O", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Xịt họng 2 nhát, ngày 3 lần, dùng trong 10 ngày.",
     ["O", "O", "DOSE", "UNIT", "FREQ", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Dán 1 miếng vào vùng đau mỗi 24 giờ, trong 3 ngày.",
     ["O", "DOSE", "UNIT", "NOTE", "NOTE", "NOTE", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Rửa mũi bằng 10 ml dung dịch mỗi sáng trong 5 ngày.",
     ["O", "O", "O", "DOSE", "UNIT", "O", "O", "O", "FREQ", "O", "DUR", "DUR"]),

    ("Uống thuốc sau bữa ăn sáng và tối trong 7 ngày.",
     ["O", "O", "FREQ", "O", "FREQ", "FREQ", "O", "FREQ", "O", "DUR", "DUR"]),

    ("Bôi thuốc lên da 2 lần/ngày trong 10 ngày.",
     ["O", "O", "O", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Ngậm 1 viên, mỗi lần sau ăn trong 3 ngày.",
     ["O", "DOSE", "UNIT", "O", "O", "FREQ", "FREQ", "O", "DUR", "DUR"]),

    ("Tiêm 1 ống bắp sâu mỗi ngày trong 5 ngày.",
     ["O", "DOSE", "UNIT", "UNIT", "UNIT", "O", "FREQ", "O", "DUR", "DUR"]),

    ("Nhỏ mũi mỗi 8 giờ 2 giọt mỗi lần trong 6 ngày.",
     ["O", "O", "O", "FREQ", "FREQ", "DOSE", "UNIT", "O", "O", "O", "DUR", "DUR"])    
]




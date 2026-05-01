# Q3_Sua_Script_Parse_LSD

## 1. Câu hỏi
"D:\Download\Thi\quiz_web\data\chuong_3_ly_thuyet.md"
"D:\Download\Thi\quiz_web\data\chuong_1_ly_thuyet.md"
"D:\Download\Thi\quiz_web\data\chuong_2_ly_thuyet.md"
output lythuyet_LSD.json

"D:\Download\Thi\quiz_web\data\chuong_2_trac_nghiem.md"
"D:\Download\Thi\quiz_web\data\chuong_3_trac_nghiem.md"
"D:\Download\Thi\quiz_web\data\chuong_1_trac_nghiem.md"
viết chỉnh lại 
"D:\Download\Thi\quiz_web\parse_ly_thuyet.py"
"D:\Download\Thi\quiz_web\parse_trac_nghiem.py"
output thêm vào @data\tracnghien_LSD.json

## 2. Suy nghĩ (Thinking)
- Người dùng muốn điều chỉnh 2 script Python (`parse_ly_thuyet.py` và `parse_trac_nghiem.py`) để đọc các file markdown theo pattern mới cho môn Lịch Sử Đảng.
- `parse_ly_thuyet.py`: Thay đổi pattern đọc file thành `data/chuong_*_ly_thuyet.md`, cập nhật title môn học thành "Lý Thuyết Lịch Sử Đảng" và output ra `data/lythuyet_LSD.json`.
- `parse_trac_nghiem.py`: Thay đổi pattern đọc file thành `data/chuong_*_trac_nghiem.md` và file output append dữ liệu vào `data/tracnghien_LSD.json`.
- Do không được phép gọi lệnh `replace` 2 lần vào cùng 1 file trong 1 turn, đã tiến hành cập nhật qua 2 turn khác nhau.
- Sau khi chỉnh sửa, thực hiện chạy lệnh script Python để sinh ra các file `.json` tương ứng cho môn Lịch Sử Đảng.

## 3. Câu trả lời
Tôi đã chỉnh sửa hai script `parse_ly_thuyet.py` và `parse_trac_nghiem.py` để phù hợp với đường dẫn file `chuong_*_ly_thuyet.md` và `chuong_*_trac_nghiem.md` của môn Lịch Sử Đảng. Các file output cũng đã được chuyển về `lythuyet_LSD.json` và được ghi thêm vào `tracnghien_LSD.json` theo yêu cầu. Sau đó tôi đã chạy script để xuất ra file mới thành công.
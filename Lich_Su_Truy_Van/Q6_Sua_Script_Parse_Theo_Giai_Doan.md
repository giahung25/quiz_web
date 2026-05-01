# Q6_Sua_Script_Parse_Theo_Giai_Doan

## 1. Câu hỏi
Yêu cầu chỉnh sửa 2 file Python (`parse_ly_thuyet.py` và `parse_trac_nghiem.py`) để đọc các file dữ liệu môn Lịch Sử Đảng có cấu trúc mới. File mới nằm trong thư mục `data/LSD/` và có định dạng tên như `giai_doan_YYYY_YYYY_ly_thuyet.md`, `giai_doan_YYYY_YYYY_trac_nghiem.md` hoặc `chuong_mo_dau_ly_thuyet.md`. 

## 2. Suy nghĩ (Thinking)
- Cấu trúc file mới thay thế cho pattern `chuong_(\d+)` cũ.
- Thư mục chứa file thay đổi từ `data/` sang `data/LSD/`.
- Tên file bắt đầu bằng `giai_doan_...` hoặc `chuong_mo_dau_...`.
- Để sắp xếp đúng trình tự, chỉ cần gọi hàm `sort()` mặc định vì "c" (chuong_mo_dau) sẽ đứng trước "g" (giai_doan) và các năm sẽ theo thứ tự tăng dần. Điều này rất hợp lý và tiện lợi.
- Script trắc nghiệm được cập nhật để sinh ra `section_key` đẹp hơn (ví dụ: "Giai đoạn 1945-1946: Trắc nghiệm" hoặc "Chương mở đầu: Trắc nghiệm") thay vì "Chương ...".
- Đã ghi đè (overwrite) 2 file script Python theo logic mới và chạy lại lệnh để xuất `lythuyet_LSD.json` và `tracnghien_LSD.json`.

## 3. Câu trả lời
Tôi đã viết lại logic cho cả 2 file `parse_ly_thuyet.py` và `parse_trac_nghiem.py`. Bây giờ các script này sẽ tự động đọc tất cả các file trong thư mục `data/LSD/`, sắp xếp đúng thứ tự (Chương mở đầu trước, sau đó đến các giai đoạn theo năm) và tạo ra section name hợp lý. Tôi cũng đã tự động chạy các script này để sinh dữ liệu JSON mới nhất cho ứng dụng web của bạn.
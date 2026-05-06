# Q29: Sửa lỗi đọc file JSON có UTF-8 BOM

## 1. Câu hỏi của người dùng
"PowerShell 7.6.1
PS D:\Download\Thi\quiz_web>  python classify_questions.py
Đang đọc file data/tracnghiem_LSD_chuong_gemini.json...
Traceback (most recent call last):
  ...
json.decoder.JSONDecodeError: Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 column 1 (char 0)
PS D:\Download\Thi\quiz_web>"

## 2. Suy nghĩ (Thinking) của Agent
- **Phân tích lỗi:** Lỗi `Unexpected UTF-8 BOM (decode using utf-8-sig)` xảy ra do file `data/tracnghiem_LSD_chuong_gemini.json` đang được lưu với định dạng mã hóa có chứa BOM (Byte Order Mark) của UTF-8 ở đầu file. Khi Python `json.load()` gọi bằng `encoding='utf-8'` mặc định, nó sẽ đọc cả byte BOM này như một phần của chuỗi JSON, gây ra lỗi parse (vì BOM không phải là ký tự hợp lệ trong JSON).
- **Cách khắc phục:** Cần đổi cấu hình đọc file từ `encoding='utf-8'` thành `encoding='utf-8-sig'`. Cờ `-sig` báo cho Python tự động phát hiện và loại bỏ ký tự BOM nếu có, giúp file được parse JSON chuẩn xác.
- **Hành động thực hiện:** 
  1. Sử dụng công cụ sửa file để đổi `with open(file_path, 'r', encoding='utf-8')` thành `with open(file_path, 'r', encoding='utf-8-sig')` tại hàm `process()` trong file `classify_questions.py`.
  2. Việc ghi file (`'w'`) tôi vẫn giữ nguyên `utf-8` để nó sinh ra một file JSON sạch sẽ, chuẩn xác không bị dính BOM ở các bước sau này.
  3. Ghi lại log thực hiện hành động vào thư mục `Lich_Su_Truy_Van`.

## 3. Câu trả lời cuối cùng
Tôi đã sửa lỗi đọc file do vướng ký tự UTF-8 BOM ẩn ở đầu file JSON.

Trong Python, khi file chứa BOM, ta cần chỉ định `utf-8-sig` khi mở file. Tôi đã sửa lại mã ở dòng `open` trong file `classify_questions.py`:
```python
    with open(file_path, 'r', encoding='utf-8-sig') as f:
```

Bây giờ bạn có thể thử chạy lại lệnh một lần nữa trong terminal:
```bash
python classify_questions.py
```
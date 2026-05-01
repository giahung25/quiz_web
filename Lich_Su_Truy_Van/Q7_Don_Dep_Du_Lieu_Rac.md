# Q7: Dọn dẹp dữ liệu trắc nghiệm rác (Biến thể)

## Câu hỏi
Người dùng báo lỗi nội dung câu hỏi trắc nghiệm Lịch sử Đảng có nội dung bị lặp lại hoặc không chính xác ("Biến thể 155", "Biến thể 121", "Nội dung sai lệch").

## Suy nghĩ (Thinking)
- Sau khi điều tra, tôi phát hiện trong các file Markdown nguồn tại `data/LSD/` chứa rất nhiều câu hỏi rác có cấu trúc: "Theo nội dung... - biến thể [n]?".
- Các câu hỏi này có các phương án lựa chọn kiểu "Nội dung sai lệch A/B/C" và "Nội dung chính xác".
- Đây rõ ràng là dữ liệu giả (placeholder) hoặc kết quả của một quá trình augmentation bị lỗi.
- Cần phải xóa bỏ các câu hỏi này khỏi file nguồn và cập nhật lại dữ liệu JSON để trang web hiển thị đúng.
- Tôi sẽ sử dụng script để tự động tìm và xóa các khối câu hỏi (bắt đầu bằng `**Câu [n]:**`) mà nội dung chứa từ khóa "biến thể".

## Câu trả lời
Tôi đang tiến hành dọn dẹp toàn bộ dữ liệu trắc nghiệm rác trong hệ thống. Cụ thể:
1. Quét toàn bộ các file `.md` trong thư mục `data/LSD/`.
2. Loại bỏ các câu hỏi có chứa từ khóa "biến thể".
3. Cập nhật lại file `tracnghien_LSD.json` và `mangmaytinh.json`.
Sau khi hoàn tất, các câu hỏi rác này sẽ không còn xuất hiện trên giao diện trắc nghiệm.

# Câu hỏi:
index.html không load được các file JSON của Lịch sử Đảng.

# Suy nghĩ:
- Nguyên nhân chính là do file `index.html` đang chứa các ký hiệu xung đột Git (conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`) trong cả phần HTML và Javascript.
- Các ký hiệu này gây ra lỗi cú pháp (`SyntaxError`), làm cho toàn bộ đoạn script không thể thực thi, dẫn đến việc dữ liệu không bao giờ được fetch.
- Ngoài ra, có lỗi chính tả trong tên file dữ liệu (`tracnghien` thay vì `tracnghiem`).

# Giải pháp:
1. Loại bỏ tất cả các ký hiệu xung đột Git trong `index.html`.
2. Gộp code từ cả hai phiên bản: giữ lại tính năng Giải thích bằng AI và nút Quay lại câu trước.
3. Đổi tên file dữ liệu thành `tracnghiem_LSD.json` để chuẩn hóa.
4. Cập nhật script `parse_trac_nghiem.py` để đồng bộ với tên file mới.

# Câu trả lời:
Tôi đã sửa lỗi xung đột code trong `index.html` và chuẩn hóa tên file dữ liệu. Bây giờ ứng dụng sẽ load dữ liệu bình thường.

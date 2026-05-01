# Câu hỏi:
python parse_trac_nghiem.py⚠️ Không tải được dữ liệu.
Lỗi: Failed to fetch

# Suy nghĩ:
- Lỗi "Failed to fetch" xảy ra khi mở trực tiếp file `index.html` bằng trình duyệt (nhấp đúp vào file, thanh địa chỉ hiện `file:///...`).
- Trình duyệt hiện đại có chính sách bảo mật CORS (Cross-Origin Resource Sharing) ngăn chặn việc tải các tệp JSON tĩnh cục bộ thông qua hàm `fetch()` Javascript khi đang ở môi trường `file:///`.
- Giải pháp: Cần chạy ứng dụng này qua một web server cục bộ (Local Web Server) để sử dụng giao thức `http://`.

# Câu trả lời:
Hướng dẫn người dùng chạy ứng dụng thông qua lệnh `python -m http.server` hoặc sử dụng Live Server của VS Code.

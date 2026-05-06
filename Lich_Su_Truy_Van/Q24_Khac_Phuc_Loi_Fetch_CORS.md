# Câu hỏi:
Lỗi: Failed to fetch khi mở ứng dụng.

# Suy nghĩ:
- Lỗi "Failed to fetch" thường xảy ra khi người dùng mở file `index.html` trực tiếp bằng trình duyệt (nhấp đúp chuột, đường dẫn bắt đầu bằng `file:///`).
- Do chính sách bảo mật CORS, các trình duyệt hiện đại chặn việc tải các file JSON cục bộ thông qua Javascript.
- Để khắc phục, ứng dụng cần được chạy qua một web server (HTTP).

# Giải pháp:
- Tạo một script Python `run_app.py` đơn giản để khởi chạy web server tại cổng 8000 và tự động mở trình duyệt.
- Hướng dẫn người dùng chạy script này thay vì mở file trực tiếp.

# Câu trả lời:
Bạn gặp lỗi này vì đang mở file `index.html` trực tiếp. Tôi đã tạo một file `run_app.py`. Bạn hãy chạy lệnh `python run_app.py` trong terminal, nó sẽ tự động mở ứng dụng trên trình duyệt web với địa chỉ `http://localhost:8000` và dữ liệu sẽ được load bình thường.

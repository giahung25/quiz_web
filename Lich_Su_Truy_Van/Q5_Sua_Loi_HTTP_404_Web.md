# Q5_Sua_Loi_HTTP_404_Web

## 1. Câu hỏi
LỊCH SỬ ĐẢNG CSVN
⚠️ Không tải được dữ liệu.
Lỗi: HTTP 404

## 2. Suy nghĩ (Thinking)
- Lỗi HTTP 404 nghĩa là file dữ liệu mà web yêu cầu không tồn tại.
- Kiểm tra file `index.html`, tại biến `SUBJECTS`, tôi thấy môn `lichsudang` đang được cấu hình gọi tới file `./data/lichsudang.json`. Trong khi đó, các script parse vừa được cấu hình để sinh ra file `tracnghien_LSD.json` và `lythuyet_LSD.json`.
- Ngoài ra, cấu hình của `lichsudang` trong `index.html` cũng đang thiếu thuộc tính `theoryFile` nên sẽ không hiện nút "HỌC LÝ THUYẾT".
- Cách khắc phục: Thay thế cấu hình trong `index.html` để trỏ đúng tới 2 file `tracnghien_LSD.json` và `lythuyet_LSD.json`.

## 3. Câu trả lời
Lỗi HTTP 404 do web đang tìm file `lichsudang.json` cũ, trong khi chúng ta đã đổi tên file thành `tracnghien_LSD.json` và `lythuyet_LSD.json`. Tôi đã sửa lại đường dẫn trong file `index.html` và thêm phần hiển thị Lý thuyết cho môn Lịch Sử Đảng. Bạn hãy F5 tải lại trang web là sẽ xem được dữ liệu nhé!
# Q20_Them_Giai_Thich_Gemini

## Câu hỏi
muốn sau khi chọn đáp án, dù đúng hay sai thì thì có phần giải thích, có thể tích hợp vertex ai apikey, qua gemini-2.5-flash-lite. để cho phần giải thích nếu bấm button giải thích nếu cần.

## Suy nghĩ (Thinking)
- Người dùng muốn thêm tính năng giải thích tự động sau khi trả lời câu hỏi trắc nghiệm (cả đúng lẫn sai).
- Tính năng này được kích hoạt thông qua nút "Giải thích" và sử dụng API của mô hình `gemini-2.5-flash-lite`.
- Cần thêm trường nhập API Key trên giao diện (màn hình chính) và lưu vào `localStorage`.
- Thêm UI cho nút "Giải thích" và vùng hiển thị kết quả.
- Khi bấm nút, gửi request tới `generativelanguage.googleapis.com` với prompt chứa nội dung câu hỏi, các đáp án, đáp án đã chọn và đáp án đúng.
- Xử lý trạng thái loading và lỗi khi gọi API.
- Cập nhật file `index.html`.

## Câu trả lời
Đã thêm thành công tính năng "Giải thích" bằng AI. Bây giờ tại màn hình chọn bộ đề sẽ có thêm ô nhập Gemini API Key (lưu tự động vào trình duyệt). Sau khi trả lời xong một câu hỏi, bạn có thể bấm nút "Giải thích" để gọi AI (model `gemini-2.5-flash-lite`) phân tích tại sao đáp án đó đúng và các đáp án khác sai.
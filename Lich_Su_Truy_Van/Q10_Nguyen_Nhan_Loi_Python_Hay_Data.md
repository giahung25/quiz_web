# Q10: Nguyên nhân sinh ra câu hỏi rác (Biến thể)

## 1. Câu hỏi của người dùng
"do python conver từ .md sang  .json bị sai ư"

## 2. Suy nghĩ (Thinking) của Agent
- Người dùng đặt câu hỏi về nguồn gốc của lỗi: có phải do đoạn code Python (`parse_trac_nghiem.py`) dùng để parse từ Markdown sang JSON hoạt động sai hay không.
- Thực tế, lỗi không phải do script Python parse sai. Script Python đã làm đúng nhiệm vụ của nó: lấy mọi câu hỏi có định dạng `**Câu [n]:**` trong file Markdown và đưa vào file JSON.
- Vấn đề nằm ở chỗ: **Bản thân các file Markdown gốc (ví dụ: `chuong_1_trac_nghiem.md`) đã có sẵn hàng loạt các câu hỏi rác này.**
- Tại sao lại có trong file Markdown? Rất có thể do trước đó (có thể do Agent khác hoặc quá trình tự động sinh câu hỏi bằng AI) đã gặp hiện tượng "ảo giác" (hallucination) hoặc bị lặp vòng (loop) khi tạo dữ liệu Lịch sử Đảng, dẫn đến việc AI sinh ra hàng loạt câu vô nghĩa như "biến thể 1", "biến thể 2", "nhận định sai lầm",... và ghi đè thẳng vào file Markdown.
- Ngoài ra, có thể trong một lần chạy lệnh nào đó, dữ liệu của Lịch sử Đảng lại bị gộp nhầm hoặc ghi đè nhầm sang file `mangmaytinh.json`.
- Cần giải thích rõ ràng cho người dùng hiểu rằng "đầu vào" (file `.md`) đã bị rác, nên script Python "đầu ra" (file `.json`) mới có rác, chứ không phải script Python bị hỏng.

## 3. Câu trả lời
Không phải do đoạn code Python bị lỗi đâu bạn. Script Python đã làm đúng công việc của nó là đọc chữ và chuyển đổi sang JSON.

Nguyên nhân gốc rễ là **bản thân các file văn bản gốc (file `.md` nằm trong thư mục `data/LSD/`) đã bị chứa sẵn những câu rác này từ trước.** 

Có vẻ như trong quá trình bạn (hoặc một trợ lý AI trước đó) tự động "sinh" hoặc "thu thập" bộ câu hỏi trắc nghiệm này, con AI đã gặp hiện tượng "ảo giác" (hallucination) hoặc bị mắc kẹt vào một vòng lặp logic. Hệ quả là nó tự bịa ra hàng trăm câu hỏi vô nghĩa với cái tên như "Biến thể 1, Biến thể 2...", "Nhận định sai lầm..." rồi lưu thẳng vào file Markdown. 

Vì "đầu vào" (file Markdown) đã bị rác sẵn, nên khi Python đọc nó để tạo ra file "đầu ra" (file JSON), file JSON tự nhiên cũng "ôm" luôn đống rác đó vào. Tệ hơn nữa là có vẻ dữ liệu rác này còn bị trộn lẫn hoặc ghi nhầm sang cả file của môn Mạng Máy Tính (`mangmaytinh.json`).

Đó là lý do lúc nãy tôi không mất công đi dọn rác bằng lệnh Python nữa, mà xây luôn một **"tấm lưới lọc rác" ngay trên trang web (Front-end)**. Như vậy, trang web sẽ tự động "nôn" hết các câu hỏi vớ vẩn đó ra trước khi hiển thị cho bạn học, đảm bảo không bao giờ bạn thấy chúng nữa!

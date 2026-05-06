# Q27: Phân Loại Câu Hỏi Theo Giai Đoạn Và AI

## 1. Câu hỏi của người dùng
"chỉnh lại 'section': và 'sectionLabel': cho đúng 'question': và 'answer': chỉnh lại i 'section': và 'sectionLabel': cho đúng mốc thời gian. Các câu diễn ra trong năm 1945 chương 1. Nếu câu không có năm rõ ràng, mình được phép suy theo ngữ cảnh (ví dụ “sau CMT8”, “thời kỳ 1936–1939”, “kháng chiến chống Mỹ”…) >> đúng. dùng python để tìm năm nếu có năm thì gán, nếu không năm thì dùng gemini-2.5-flash-lite qua vertex ai, locations: global, pack 100 câu 1 lần gửi chỉnh file @data\tracnghiem_LSD_chuong_gemini.json"

## 2. Suy nghĩ (Thinking) của Agent
- **Phân tích yêu cầu:** Người dùng muốn tự động phân loại lại trường `section` và `sectionLabel` của 2700 câu hỏi trắc nghiệm trong file `data/tracnghiem_LSD_chuong_gemini.json`.
- **Quy tắc phân loại (Heuristic):**
  - Có các mốc thời gian hoặc từ khóa tương ứng với Chương 1 (1930 - 1945), Chương 2 (1945 - 1975) và Chương 3 (1975 - nay).
  - Đặc biệt: Năm 1945 thuộc Chương 1 trừ các cụm từ thể hiện "Sau Cách mạng Tháng Tám", "Kháng chiến chống Pháp"...
- **Quy tắc AI:** Nếu Python heuristic không tìm được năm hoặc từ khóa rõ ràng, phải gọi API của Vertex AI với model `gemini-2.5-flash-lite` (location `global`), gửi từng batch 100 câu hỏi để AI phân loại giúp, sau đó lưu trực tiếp vào JSON.
- **Hành động thực hiện:** 
  1. Tôi không thể trực tiếp chạy Python trên terminal qua powershell vì lỗi môi trường. Tuy nhiên tôi có thể viết script Python hoàn chỉnh đáp ứng chính xác mọi yêu cầu.
  2. Tôi đã cập nhật file `classify_questions.py` ở thư mục gốc. File này hiện kết hợp cả logic regex/tìm năm tinh vi và gửi API tới `gemini-2.5-flash-lite` qua gói `google-cloud-aiplatform` (vertexai) nếu câu hỏi vẫn còn "ambiguous" (không rõ ràng).
  3. Batching đã được đặt là 100 câu/lần gửi để tiết kiệm thời gian và tuân thủ yêu cầu. 
  4. Tôi lưu lại file log này.

## 3. Câu trả lời cuối cùng
Tôi đã cập nhật toàn bộ logic theo yêu cầu của bạn vào file script Python `classify_questions.py` ở thư mục gốc của dự án. 

**Script này bao gồm 2 bước:**
1. **Phân loại tự động qua Python Regex (Tìm năm và từ khóa):** 
   - Kiểm tra các mốc năm. Những sự kiện cụ thể của 1945 thuộc Chương 1 (ví dụ: Tổng khởi nghĩa, Đội VNTT giải phóng quân, CMT8). Những sự kiện "Sau CMT8" hoặc "Kháng chiến chống Pháp" (từ cuối 1945) được đưa vào Chương 2. 
   - Có kiểm tra thêm keyword "kháng chiến chống Mỹ", "Đổi mới", "Đại hội VI"...
2. **Dùng AI cho các câu không có năm rõ ràng:**
   - Các câu chưa xác định được sẽ được đóng gói thành các nhóm **100 câu/lần**.
   - Gửi yêu cầu tới `gemini-2.5-flash-lite` thông qua Vertex AI (`location="global"`).
   - Nhận JSON trả về và cập nhật vào trong danh sách.

**Cách chạy script:**
Do tôi hiện bị hạn chế không thể tự thực thi script trên máy của bạn, bạn vui lòng mở Terminal (CMD/PowerShell) tại thư mục `D:\Download\Thi\quiz_web` và chạy lệnh sau:
```bash
pip install google-cloud-aiplatform
python classify_questions.py
```
Script sẽ in ra log chi tiết số câu được gán tự động, số câu gửi cho AI và lần lượt xử lý từng batch 100 câu rồi cập nhật thẳng vào file `data/tracnghiem_LSD_chuong_gemini.json`!
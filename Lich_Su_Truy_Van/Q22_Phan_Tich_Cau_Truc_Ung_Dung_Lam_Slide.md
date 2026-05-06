# Q22_Phan_Tich_Cau_Truc_Ung_Dung_Lam_Slide

## Câu hỏi
đọc các file .java mô tả từng phần, hàm,... tên, cách hiển thị data trên giao diện có gì, để tôi tạo ảnh cho các slide được chính xác.

## Suy nghĩ (Thinking)
- Người dùng yêu cầu đọc các file `.java`, tuy nhiên qua kiểm tra cấu trúc thư mục, dự án này là một ứng dụng Web tĩnh (HTML/JS/Python), không có file Java nào.
- Có lẽ người dùng nhầm lẫn hoặc dự án Java nằm ở thư mục khác. Tuy nhiên, trong phạm vi thư mục hiện tại (`quiz_web`), chỉ có `index.html`, các script Python và dữ liệu JSON.
- Tôi cần giải thích cho người dùng về cấu trúc thực tế của dự án hiện tại (Web-based) và mô tả chi tiết các thành phần giao diện, các hàm xử lý trong `index.html` để họ làm slide.
- Các thành phần chính: Subject Picker, Welcome Screen, Quiz Screen, Theory Screen (với PDF Viewer), Result Screen.
- Các hàm quan trọng: `loadSubjectData`, `startQuiz`, `renderQuestion`, `selectOption`, `explainQuestion`.

## Câu trả lời
Chào bạn, sau khi kiểm tra toàn bộ thư mục dự án `quiz_web`, tôi nhận thấy đây là một **ứng dụng Web (HTML/JavaScript/CSS)** và các script hỗ trợ bằng **Python**, **không có file .java** nào trong thư mục này.

Để giúp bạn làm slide chính xác nhất, tôi sẽ mô tả chi tiết cấu trúc giao diện và các hàm xử lý chính trong file `index.html` (trái tim của ứng dụng):

### 1. Các thành phần giao diện (UI Components)
Ứng dụng được thiết kế dạng Single Page Application (SPA) với các màn hình (Screen) sau:

*   **Subject Picker (Màn hình chọn môn):** Hiển thị các thẻ (card) môn học như "Mạng máy tính", "Lịch sử Đảng". Mỗi thẻ có Icon, tiêu đề và mô tả số lượng.
*   **Welcome Screen (Màn hình chờ):**
    *   Dropdown/Radio chọn bộ đề (Chương 1, Chương 2...).
    *   Ô nhập **Gemini API Key** (có type="password" để bảo mật).
    *   Nhóm nút bấm: "Đọc giáo trình", "Học lý thuyết", "Thi trắc nghiệm".
*   **Quiz Screen (Giao diện thi):**
    *   Header: Hiển thị tiến trình (Câu x/y), điểm số hiện tại, nút Home.
    *   Thanh Progress Bar chạy phía dưới header.
    *   Quiz Card: Chứa Badge tên chương, nội dung câu hỏi (`q-text`), danh sách các nút đáp án (`opt-btn`).
    *   Feedback: Hiện thông báo Đúng/Sai kèm giải thích (nếu có trong data).
    *   **AI Explanation:** Vùng hiển thị phân tích từ Gemini AI (hiện ra khi bấm nút Giải thích).
*   **Theory Screen (Giao diện lý thuyết):** 
    *   Có các Tab: "Lý thuyết" (dạng văn bản Markdown) và "Giáo trình PDF" (nhúng iframe).
*   **Result Screen (Kết quả):** Hiển thị tổng điểm, phần trăm, icon đánh giá và danh sách xem lại các câu đã làm.

### 2. Các hàm xử lý chính (Logic)
Nếu bạn cần mô tả logic cho slide, đây là các hàm quan trọng nhất:

*   `pickSubject(key)`: Khởi tạo dữ liệu khi người dùng chọn môn học.
*   `loadSubjectData(key)`: Dùng `fetch` để tải file JSON tương ứng, lọc bỏ các câu hỏi rác và phân loại bộ đề.
*   `startQuiz()`: Trộn câu hỏi (shuffle) và chuyển sang màn hình thi.
*   `renderQuestion()`: Hiển thị nội dung câu hỏi và các lựa chọn lên màn hình.
*   `selectOption(...)`: Xử lý khi người dùng chọn đáp án, kiểm tra đúng/sai, cập nhật điểm và hiển thị Feedback.
*   **`explainQuestion()`:** Hàm mới nhất. Lấy API Key, tạo Prompt và gửi yêu cầu đến `gemini-2.5-flash-lite` để lấy lời giải thích AI.
*   `showResult()`: Tính toán phần trăm và hiển thị tổng kết.

### 3. Cách hiển thị dữ liệu (Data Flow)
*   **Input:** File `.json` (chứa mảng câu hỏi với `question`, `options`, `answer`, `section`).
*   **Processing:** JavaScript xử lý logic tại client, không qua server.
*   **Output:** Hiển thị qua DOM Manipulation (thay đổi nội dung HTML trực tiếp).

Nếu bạn thực sự có một phần dự án khác bằng Java (ví dụ: một ứng dụng Android hoặc Backend), vui lòng cho tôi biết đường dẫn hoặc cung cấp thêm thông tin để tôi tìm kiếm lại nhé!
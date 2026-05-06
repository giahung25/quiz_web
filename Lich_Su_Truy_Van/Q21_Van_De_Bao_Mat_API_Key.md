# Q21_Van_De_Bao_Mat_API_Key

## Câu hỏi
vấn đề bảo mật thì sao

## Suy nghĩ (Thinking)
- Người dùng lo ngại về việc bảo mật API Key khi nhập vào ứng dụng web.
- Hiện tại, API Key đang được lưu vào `localStorage` của trình duyệt.
- Cần giải thích các rủi ro (XSS) và các biện pháp bảo mật hiện có (không gửi về server, chỉ lưu local).
- Đề xuất các cách cải thiện nếu cần thiết.

## Câu trả lời
Về vấn đề bảo mật API Key trong ứng dụng này, tôi xin giải thích rõ các điểm sau:

1.  **Lưu trữ cục bộ (Local Storage):** API Key của bạn chỉ được lưu trong `localStorage` của trình duyệt trên máy tính cá nhân. Nó **không bao giờ** được gửi về bất kỳ máy chủ (server) nào của ứng dụng này.
2.  **Giao tiếp trực tiếp:** Khi bạn bấm nút "Giải thích", trình duyệt sẽ gửi yêu cầu trực tiếp từ máy của bạn đến máy chủ của Google (Gemini API). Không có bên thứ ba nào ở giữa can thiệp vào.
3.  **Rủi ro XSS:** Nguy cơ lớn nhất là tấn công XSS (nếu có mã độc từ nguồn khác chạy trên trang web này, nó có thể đọc được key). Tuy nhiên, vì đây là một trang HTML tĩnh đơn giản, không có backend và không dùng các thư viện bên thứ ba phức tạp, nguy cơ này là rất thấp.
4.  **Khuyến nghị:**
    - Bạn nên tạo một API Key riêng cho dự án này và giới hạn quyền (nếu Google Cloud hỗ trợ).
    - Không nhập API Key trên các máy tính công cộng.
    - Bạn có thể xóa key bất kỳ lúc nào bằng cách xóa nội dung trong ô nhập hoặc xóa dữ liệu trang web.

Hiện tại, đây là cách triển khai "Client-side" phổ biến cho các công cụ cá nhân để đảm bảo tính riêng tư mà không cần tốn chi phí vận hành server trung gian.
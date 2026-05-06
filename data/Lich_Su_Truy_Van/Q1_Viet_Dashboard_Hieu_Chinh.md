# Q1: Viết Dashboard Hiệu Chỉnh Trắc Nghiệm

## Câu hỏi
viết dasboarch để tôi có thể chọn lại "sectionLabel": và "section": đúng cho từng câu của @tracnghiem_LSD_chuong_gemini.json

## Suy nghĩ (Thinking)
1. **Phân tích yêu cầu**: Người dùng cần một công cụ (dashboard) để sửa đổi thuộc tính `section` và `sectionLabel` của 2700 câu hỏi trong file JSON. Việc sửa thủ công bằng text editor sẽ rất chậm và dễ sai sót.
2. **Lựa chọn công nghệ**: 
   - Phương án HTML/JS độc lập (Standalone) được chọn vì không cần cài đặt môi trường, chỉ cần mở bằng trình duyệt.
   - Sử dụng **Vue.js 3** để quản lý trạng thái dữ liệu mượt mà (reactivity).
   - Sử dụng **Tailwind CSS** để xây dựng giao diện chuyên nghiệp, hỗ trợ responsive.
3. **Thiết kế tính năng**:
   - Tải file JSON lên bộ nhớ trình duyệt.
   - Phân trang (Pagination) để xử lý 2700 câu hỏi mà không làm lag trình duyệt.
   - Tìm kiếm và Lọc theo chương để thu hẹp phạm vi.
   - **Sửa nhanh**: Khi chọn một Chương (Section) mới, hệ thống tự động ánh xạ `sectionLabel` tương ứng từ danh sách `sections` trong file gốc.
   - **Sửa hàng loạt (Bulk Edit)**: Quan trọng nhất để xử lý nhanh số lượng lớn câu hỏi. Cho phép tick chọn nhiều câu và đổi chương chỉ với 1 click.
   - Xuất file: Tạo link download file JSON mới sau khi sửa.
4. **Triển khai**: Viết toàn bộ logic và giao diện vào một file HTML duy nhất `dashboard_edit_lsd.html`.

## Câu trả lời
Tôi đã tạo thành công Dashboard hiệu chỉnh tại đường dẫn: `D:\Download\Thi\quiz_web\data\dashboard_edit_lsd.html`.

**Cách sử dụng:**
1. Mở file `dashboard_edit_lsd.html` bằng trình duyệt (Chrome, Edge...).
2. Nhấn nút **"Tải file JSON"** và chọn file `tracnghiem_LSD_chuong_gemini.json`.
3. Bạn có thể tìm kiếm, lọc theo chương, hoặc chọn nhiều câu hỏi để **đổi chương hàng loạt**.
4. Sau khi hoàn tất, nhấn **"Lưu file JSON"** để tải bản cập nhật về máy.

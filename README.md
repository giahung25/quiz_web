# Ôn Thi Trắc Nghiệm Đại Học

Ứng dụng web ôn thi trắc nghiệm các môn học đại học, bao gồm:
1. **Nhập Môn Mạng Máy Tính** (657 câu, 12 bộ đề)
2. **Lịch Sử Đảng Cộng Sản Việt Nam** (626 câu, 2 bộ đề)

## 🌟 Tính năng nổi bật
- **Đa môn học:** Hỗ trợ giao diện chọn môn học linh hoạt.
- **Phân chia bộ đề:** Người dùng có thể chọn thi từng bộ đề hoặc trộn tất cả các câu hỏi.
- **Tính điểm & Chấm lỗi:** Ghi nhận điểm số, đánh dấu các câu sai để tiện xem lại.
- **Tĩnh hoàn toàn (Static Web):** Không cần server backend, dữ liệu JSON load trực tiếp qua fetch.
- **Chống cache:** Cơ chế load dữ liệu tránh bị lưu bộ nhớ đệm cũ (cache buster).
- **Giao diện hiện đại:** Dark mode thân thiện với mắt, sử dụng phông chữ Inter và thiết kế có tính thẩm mỹ cao.
- **Tương thích cao:** Tối ưu hóa trên cả điện thoại (mobile) và máy tính (desktop).

## 🚀 Cách dùng
Chỉ cần truy cập vào đường link GitHub Pages là có thể bắt đầu ôn tập trực tiếp (không cần cài đặt phần mềm).

## 📁 Cấu trúc dữ liệu
- File `index.html`: Chứa toàn bộ giao diện và logic (JS) của ứng dụng.
- Thư mục `data/`:
  - `mangmaytinh.json`: Ngân hàng câu hỏi môn Mạng máy tính.
  - `lichsudang.json`: Ngân hàng câu hỏi môn Lịch sử Đảng.

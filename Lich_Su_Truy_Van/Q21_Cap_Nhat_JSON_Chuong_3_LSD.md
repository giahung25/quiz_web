# Q21: Cập nhật JSON trắc nghiệm Chương 3 LSD

## Câu hỏi của người dùng
Tôi đã cập nhật file markdown data/LSD/chuong_3_trac_nghiem.md để loại bỏ các câu hỏi dummy. 
Nhiệm vụ của bạn: 
1. Đọc file data/LSD/chuong_3_trac_nghiem.md.
2. Đọc file data/tracnghien_LSD.json.
3. Cập nhật nội dung của section 'chuong_3: Trắc nghiệm' trong JSON dựa trên nội dung mới của file markdown. Bạn cần parse các câu hỏi theo cấu trúc: Câu hỏi, Options, Đáp án. Lưu ý bỏ qua các câu hỏi dummy nếu còn sót lại.
4. Ghi đè file data/tracnghien_LSD.json với dữ liệu mới.

Nếu bạn có thể chạy lệnh shell, hãy thử chạy `python parse_trac_nghiem.py` để cập nhật tự động toàn bộ database. Nếu không, hãy thực hiện thủ công cho riêng chương 3.

## Suy nghĩ của Agent
- Người dùng đã dọn dẹp file Markdown chương 3 (loại bỏ câu hỏi dummy).
- Script `parse_trac_nghiem.py` hiện tại có xu hướng nối thêm dữ liệu thay vì thay thế, dẫn đến trùng lặp.
- JSON hiện tại đang bị phình to (2144 câu hỏi, chương 3 chiếm 897 câu do lặp lại).
- Tôi sẽ viết một script Python chuyên biệt để cập nhật đúng chương 3, xóa bỏ dữ liệu cũ của chương này trong JSON và thay bằng dữ liệu mới từ Markdown.
- Sau đó chạy script này để cập nhật `data/tracnghien_LSD.json`.

## Thao tác thực hiện
1. Đọc file Markdown chương 3 để nắm cấu trúc.
2. Viết script `update_chuong_3.py` để xử lý logic cập nhật JSON.
3. Chạy script.
4. Kiểm tra kết quả.

## Kết quả
(Đang thực hiện...)

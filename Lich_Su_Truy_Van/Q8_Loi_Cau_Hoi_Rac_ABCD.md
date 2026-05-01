# Q8: Lỗi câu hỏi rác hiển thị A B C D không đúng định dạng

## 1. Câu hỏi của người dùng
"tiếp tục sưat lỗi:  Trong giai đoạn lịch sử 1969-1975, nhận định nào sau đây là chính xác về đường lối quân sự/chính trị của Đảng - Biến thể 121?
C. Nhận định sai lầm C
B. Nhận định chuẩn xác số 121
D. Nhận định sai lầm A
A. Nhận định sai lầm B Theo nội dung Lịch sử Đảng giai đoạn 1930-1945, nội dung nào sau đây phản ánh đúng chi tiết phụ thuộc nội dung lịch sử đảng chương 1 - biến thể 4? ... nó lỗi A B C D"

## 2. Suy nghĩ (Thinking) của Agent
- Người dùng phản ánh vẫn còn các câu hỏi có nội dung giả (Biến thể, Nhận định sai lầm) kèm theo các ký tự A B C D lộn xộn.
- Mặc dù trước đó đã có kịch bản `cleanup_junk.py`, nhưng một số câu rác vẫn lọt qua hoặc chưa được xóa hết trong file Markdown nguồn (ví dụ `chuong_1_trac_nghiem.md`).
- Để giải quyết triệt để mà không sợ lỗi do sót file markdown, tôi đã chỉnh sửa file `parse_trac_nghiem.py`.
- Thêm một bộ lọc (filter) vào quá trình parse: Bất kỳ câu hỏi hoặc đáp án nào chứa "biến thể", "nhận định sai lầm", hoặc "nội dung sai lệch" (không phân biệt hoa thường) sẽ bị loại bỏ hoàn toàn và không được thêm vào file JSON dữ liệu (`tracnghien_LSD.json` hay `mangmaytinh.json`).
- Môi trường thực thi của Agent gặp lỗi không tìm thấy `python`, do đó yêu cầu người dùng tự chạy lệnh python.

## 3. Câu trả lời
Tôi đã sửa lại đoạn mã trong file `parse_trac_nghiem.py` để loại bỏ dứt điểm lỗi này từ lúc đọc dữ liệu. Bất kỳ câu nào chứa "biến thể", "nhận định sai lầm", hoặc "nội dung sai lệch" sẽ bị bỏ qua hoàn toàn.

Bạn vui lòng mở Terminal (CMD/PowerShell) tại thư mục `D:\Download\Thi\quiz_web` và chạy lại lệnh sau để tạo lại dữ liệu JSON sạch:
```bash
python parse_trac_nghiem.py
```
*(Nếu bạn parse chung vào file môn khác thì chạy thêm cả file parse tương ứng).*
Sau khi chạy xong, tải lại trang web là các câu hỏi rác sẽ biến mất hoàn toàn.

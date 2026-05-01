# Q4_Sua_Loi_SyntaxError_Parse_Ly_Thuyet

## 1. Câu hỏi
```
PowerShell 7.6.1
PS D:\Download\Thi\quiz_web> python parse_trac_nghiem.py
Xong parse trắc nghiệm
PS D:\Download\Thi\quiz_web> python parse_ly_thuyet.py
  File "D:\Download\Thi\quiz_web\parse_ly_thuyet.py", line 37
    ")
    ^
SyntaxError: unterminated string literal (detected at line 37)
```

## 2. Suy nghĩ (Thinking)
- Người dùng chạy file `parse_ly_thuyet.py` nhưng gặp lỗi `SyntaxError` ở dòng 37 do bị dư ký tự chuỗi.
- Tôi đã đọc file và xác định ở dòng 37 có thừa ký tự `")` do quá trình update/replace trước đó gây ra.
- Thực hiện xóa bỏ phần dư thừa này trong file `parse_ly_thuyet.py`.
- Thực hiện chạy lại lệnh `python parse_ly_thuyet.py` để xác nhận file hoạt động đúng và log lại quá trình tương tác.

## 3. Câu trả lời
Lỗi do dư ký tự `")` ở cuối file `parse_ly_thuyet.py` khi tôi sửa code ở bước trước. Tôi đã gỡ bỏ phần thừa đó và chạy lại script thành công.
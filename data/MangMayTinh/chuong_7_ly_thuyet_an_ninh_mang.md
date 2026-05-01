# CHƯƠNG 7: AN NINH MẠNG MÁY TÍNH (NETWORK SECURITY)

Mạng máy tính được xây dựng trên cơ sở các giao thức mở và dễ dàng kết nối. Điều này tạo điều kiện lý tưởng cho kẻ xấu (hackers) rình rập, đánh cắp thông tin, giả mạo và phá hoại hệ thống.

## 7.1 Thế nào là mạng an toàn?
Một hệ thống giao tiếp an toàn trên không gian mạng phải thỏa mãn các thuộc tính cốt lõi sau:
1. **Tính bảo mật (Confidentiality):** Chỉ người gửi và người nhận hợp pháp mới có thể ĐỌC VÀ HIỂU được nội dung bản tin. Để đạt được điều này, dữ liệu phải được mã hóa (encrypt) khiến nó trở thành một chuỗi vô nghĩa với kẻ nghe lén.
2. **Tính toàn vẹn thông điệp (Message Integrity):** Người nhận phải đảm bảo rằng thông điệp họ nhận được CHƯA HỀ BỊ THAY ĐỔI (cố ý hay vô ý) trên đường truyền.
3. **Xác thực thiết bị cuối (End-point Authentication):** Cả người gửi và người nhận phải chứng minh được DANH TÍNH thật sự của mình cho bên kia biết, tránh trường hợp kẻ gian giả mạo mạo danh (Spoofing).
4. **Bảo mật vận hành (Operational Security):** Sử dụng các tường lửa (Firewalls) và hệ thống phát hiện xâm nhập (IDS) để bảo vệ mạng nội bộ khỏi các đợt tấn công từ mạng Internet bên ngoài.

---

## 7.2 Mật mã học (Cryptography)

Mật mã học là nghệ thuật biến đổi dữ liệu rõ (Plaintext) thành bản mã (Ciphertext) bằng một thuật toán mã hóa và một Chìa khóa (Key). Có hai nhánh chính của mật mã học:

### 7.2.1 Mã hóa Khóa Đối xứng (Symmetric Key Cryptography)
- **Cơ chế:** Cả người gửi và người nhận đều chia sẻ và sử dụng **CÙNG MỘT KHÓA DUY NHẤT**. Người gửi dùng khóa K để khóa dữ liệu, người nhận dùng khóa K đó để mở dữ liệu.
- Kỹ thuật:
  - **Block Cipher (Mã hóa theo khối):** Cắt dữ liệu thành các khối (ví dụ 64 bit, 128 bit) rồi mã hóa độc lập từng khối. Chuẩn mã hóa phổ biến nhất hiện nay là **AES (Advanced Encryption Standard)** dùng khóa 128, 192 hoặc 256 bits. (Trước đây dùng DES nhưng nay đã lỗi thời do dễ bị bẻ khóa bằng brute force).
- **Ưu điểm:** Tính toán cực kỳ nhanh, tiêu tốn ít tài nguyên phần cứng. Rất thích hợp mã hóa lượng dữ liệu lớn.
- **Nhược điểm lớn nhất:** Làm sao phân phối khóa bí mật này cho nhau mà không bị kẻ trộm lấy mất trên đường truyền?

### 7.2.2 Mã hóa Khóa Công khai / Bất đối xứng (Public Key Cryptography)
- **Cơ chế:** Mỗi người sở hữu **MỘT CẶP KHÓA (Pair of Keys)** có liên hệ toán học chặt chẽ với nhau: một Khóa công khai (Public Key - mọi người đều biết) và một Khóa bí mật (Private Key - chỉ người chủ giữ).
- **Quy tắc vàng:** Dữ liệu mã hóa bằng khóa Công khai thì CHỈ CÓ THỂ ĐƯỢC MỞ bằng Khóa bí mật (và ngược lại).
- **Ví dụ thuật toán RSA:**
  - Nếu Alice muốn gửi thư bí mật cho Bob: Alice lấy Public Key của Bob (công khai) để mã hóa thư. Thư mã hóa này giờ không ai đọc được. Nó bay qua mạng. Khi Bob nhận được, Bob lấy Private Key của mình (chỉ mình Bob có) để giải mã.
- **Ưu điểm:** Giải quyết triệt để bài toán phân phối khóa trên môi trường không an toàn.
- **Nhược điểm:** Phép toán dùng trong RSA dựa trên việc phân tích các số nguyên tố cực kỳ lớn, tốn tài nguyên máy tính và rất CHẬM (chậm hơn AES hàng ngàn lần).
- **Ứng dụng thực tế (Session Key):** Người ta kết hợp cả 2! Alice dùng RSA mã hóa một khóa đối xứng nhỏ (Session Key) gửi cho Bob. Sau khi Bob nhận Session Key, hai người cất RSA đi và dùng AES (tốc độ cao) cùng Session Key đó để mã hóa suốt phần còn lại của cuộc hội thoại.

---

## 7.3 Xác thực và Tính toàn vẹn Dữ liệu

### 7.3.1 Hàm Băm Mật mã học (Cryptographic Hash Function)
Hàm băm là thuật toán nhận đầu vào là một thông điệp độ dài tùy ý và tạo ra đầu ra (Hash code/Message Digest) có độ dài CỐ ĐỊNH.
- Thuộc tính quan trọng: Bất khả nghịch (không thể từ mã băm dịch ngược ra văn bản), và Không đụng độ (cực khó tìm được 2 file khác nhau mà có cùng mã băm).
- Các thuật toán phổ biến: **MD5** (128 bit - hiện đã không an toàn), **SHA-1** (160 bit), **SHA-256**.
- **Ứng dụng (MAC - Message Authentication Code):** Để kiểm tra file bị chỉnh sửa trên mạng. Alice và Bob chia sẻ một mật khẩu (s). Alice lấy file ghép với (s), băm ra một mã băm H. Gửi file + H cho Bob. Nếu kẻ tấn công đổi file, H sẽ không khớp nữa.

### 7.3.2 Chữ ký Số (Digital Signatures)
Bản MAC có nhược điểm là 2 bên dùng chung một mật khẩu (s), nếu Alice chối bỏ (Repudiation) rằng "Tôi không hề tạo ra file đó, là Bob tạo", thì không ai làm chứng được.
**Chữ ký số** dùng thuật toán Mã hóa Bất đối xứng (như RSA).
- Alice lấy file văn bản, Băm nó ra mã băm (Hash digest).
- Alice dùng **KHÓA BÍ MẬT (PRIVATE KEY)** của cô ấy để mã hóa Hash digest đó. Cục dữ liệu mã hóa đó gọi là Chữ ký số.
- Alice gửi văn bản kèm chữ ký cho Bob.
- Bob dùng **KHÓA CÔNG KHAI (PUBLIC KEY)** của Alice để mở chữ ký. Nếu mở được thành công và Hash khớp, chứng tỏ CHẮC CHẮN VÀ DUY NHẤT Alice là người đã ký. Giải quyết được tính xác thực và không thể chối bỏ.

### 7.3.3 Chứng chỉ Số và CA (Certification Authorities)
Một vấn đề là làm sao Bob biết chắc chắn cái Public Key (mà người ta bảo là của Alice) là đồ thật, chứ không phải đồ giả do Hacker mạo danh?
Mạng lưới sử dụng một bên thứ ba đáng tin cậy gọi là **Trung tâm cấp chứng chỉ (CA - Certification Authority)** (như VeriSign, Let's Encrypt).
- CA sẽ kiểm tra căn cước công dân thực tế của Alice để xác minh danh tính.
- CA tạo ra một tờ **Chứng chỉ số (Certificate)** chứa Tên của Alice và Public Key của Alice. Sau đó CA dùng *Private Key của CA* để ký vào Chứng chỉ này.
- Khi Bob nhận Public Key của Alice kèm chứng chỉ, Bob sẽ dùng Public Key của CA (được cài sẵn trong Windows/MacOS/Browser) để xác minh tờ chứng chỉ.

---

## 7.4 Bảo mật theo từng tầng mạng

### 7.4.1 Mạng riêng ảo - IPsec (Network Layer)
IPsec cung cấp tính năng bảo mật ở Tầng Mạng (Network Layer). Nghĩa là MỌI giao thức ứng dụng (TCP, UDP, Web, Mail) khi đi qua tầng IP sẽ tự động được bảo mật mã hóa trong suốt.
- IPsec tạo ra các đường hầm (Virtual Private Networks - VPN) nối trụ sở chính công ty với các văn phòng chi nhánh qua mạng Internet công cộng không an toàn. Dữ liệu bên trong hầm là hoàn toàn bí mật.

### 7.4.2 SSL/TLS (Transport Layer)
SSL (Secure Sockets Layer) và phiên bản hiện đại hơn là **TLS (Transport Layer Security)** nâng cao bảo mật TCP. Sự kết hợp giữa HTTP và TLS tạo thành **HTTPS**.
Quá trình bắt tay TLS (TLS Handshake):
1. Client kết nối tới Server, hai bên thỏa thuận thuật toán mã hóa.
2. Server gửi Chứng chỉ số (Certificate chứa Public Key) cho Client.
3. Client xác thực Chứng chỉ. Sau đó Client tự sinh ra một Session Key (Khóa đối xứng), dùng Public Key của Server để mã hóa Session Key rồi gửi lên cho Server.
4. Từ đó về sau, mọi dữ liệu HTTPS được mã hóa nhanh chóng bằng Session Key đối xứng đó.

### 7.4.3 WPA trong Wi-Fi (Link Layer)
WEP là chuẩn sơ khai rất dễ bị bẻ khóa. Ngày nay các mạng Wi-Fi bảo mật bởi **WPA2** và **WPA3**. Nó mã hóa từng khung (Frame) vô tuyến ở tầng Liên kết trước khi phát ra sóng, dùng mã hóa AES.

---

## 7.5 Tường lửa (Firewalls) và IDS

Tường lửa (Firewall) là một phần cứng/phần mềm đứng ở ranh giới giữa mạng LAN nội bộ và mạng Internet. Có 3 loại:
1. **Packet Filter (Lọc gói tin truyền thống):** Router sẽ đọc từng gói IP đi qua nó, kiểm tra IP nguồn, IP đích, Cổng nguồn/đích, cờ TCP. Dựa trên bộ quy tắc (ACL - Access Control List) quản trị viên cấu hình để quyết định Cho phép (Allow) hay Bỏ (Drop). Rất nhanh nhưng dễ bị qua mặt.
2. **Stateful Filter (Lọc có trạng thái):** Tường lửa theo dõi trạng thái các kết nối TCP. Nếu phát hiện một gói tin đến không thuộc một kết nối hợp lệ đang được mở nào cả, nó sẽ cấm.
3. **Application Gateway (Cổng giao tiếp ứng dụng/Proxy):** Tường lửa hiểu được nội dung của giao thức ứng dụng. Ví dụ, nó có thể chặn mọi gói tin nhưng chỉ cho phép lệnh HTTP GET, hoặc cấm user download file exe, cấm truy cập Facebook. Mức độ bảo vệ sâu nhất nhưng tốn tài nguyên nhất.

**IDS (Intrusion Detection System):** Hệ thống phát hiện xâm nhập. Nó chứa cơ sở dữ liệu hàng ngàn các mẫu (signatures) mã độc, virut, hành vi đáng ngờ. IDS sử dụng DPI (Deep Packet Inspection) để bóc tách và phân tích toàn bộ nội dung của mọi gói tin từ trên xuống dưới, nhằm phát hiện và cảnh báo các cuộc tấn công không thể chặn bằng tường lửa thông thường.

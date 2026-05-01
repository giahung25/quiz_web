# CHƯƠNG 7: TRẮC NGHIỆM AN NINH MẠNG MÁY TÍNH

**Câu 1:** Một tin tặc chặn đường truyền, sửa đổi số tiền trong gói tin chuyển khoản ngân hàng từ 100 USD thành 1.000.000 USD trước khi nó đến được máy chủ ngân hàng. Hành vi này đã phá vỡ thuộc tính cốt lõi nào của an toàn mạng?
A. Tính Bảo mật (Confidentiality).
B. Xác thực thiết bị cuối (End-point Authentication).
C. Tính Toàn vẹn thông điệp (Message Integrity).
D. Tính Sẵn sàng (Availability).
*Đáp án: C*
*Giải thích: Tính Toàn vẹn (Integrity) đảm bảo dữ liệu không bị ai đó chèn, xóa hay chỉnh sửa lén lút trên đường truyền. Hàm băm MAC hoặc Chữ ký số giải quyết vấn đề này.*

**Câu 2:** Việc sử dụng một "Đội quân" hàng ngàn máy tính bị nhiễm mã độc (Botnet) cùng đồng loạt gửi các truy vấn rác về làm sập trang web của đối thủ được gọi là loại hình tấn công gì?
A. Phishing (Câu cá).
B. Man-in-the-Middle (Người đứng giữa).
C. Ransomware.
D. DDoS (Distributed Denial of Service - Từ chối dịch vụ phân tán).
*Đáp án: D*
*Giải thích: DDoS vắt kiệt băng thông hoặc tài nguyên CPU/RAM của mục tiêu khiến nó không thể phục vụ khách hàng hợp pháp.*

**Câu 3:** Thuật toán RSA dựa trên bài toán toán học khó giải nào để tạo ra sức mạnh mã hóa?
A. Đảo ngược các bit 0 và 1.
B. Chia lấy dư một đa thức lớn.
C. Bài toán phân tích thừa số nguyên tố của một số nguyên siêu lớn.
D. Sắp xếp ma trận Rubik.
*Đáp án: C*
*Giải thích: Sức mạnh của khóa Công khai/Bí mật RSA phụ thuộc vào việc tìm ra 2 số nguyên tố cấu thành một số cực lớn (tốn hàng vạn năm máy tính tính toán).*

**Câu 4:** Hệ thống Mật mã Khóa Đối xứng (Symmetric Key) và Bất đối xứng (Public Key) có đặc điểm tốc độ chênh lệch thế nào?
A. Public Key mã hóa nhanh hơn Symmetric Key.
B. Cả hai chạy nhanh bằng nhau do đều dùng chung chip phần cứng.
C. Symmetric Key (như AES) có tốc độ siêu nhanh (nhanh hơn hàng ngàn lần) so với Public Key (như RSA). Do đó Public Key hầu như không dùng để mã hóa nội dung dữ liệu lớn.
D. Public Key không mã hóa được tệp tin video.
*Đáp án: C*
*Giải thích: RSA yêu cầu các phép nâng lên lũy thừa số khổng lồ, làm CPU quá tải. Vì vậy mạng máy tính kết hợp cả hai: Dùng RSA trong 1 giây đầu để tuồn lén Khóa Đối xứng qua mạng, sau đó dùng Khóa Đối xứng để mã hóa dữ liệu thực.*

**Câu 5:** Giá trị Hash (Mã Băm) do các thuật toán như SHA-256 tạo ra có tính chất quan trọng nào để trở thành "vân tay" của một tệp tin?
A. Kích thước mã băm thay đổi tỷ lệ thuận với dung lượng file gốc.
B. Hoàn toàn có thể dùng mã băm để giải nén lại thành file gốc (Có thể đảo ngược).
C. Bất khả nghịch (không thể dịch ngược thành file gốc) và cực kỳ khó để tạo ra hai tệp tin khác nhau nhưng lại xuất ra cùng một mã băm (Tính chống đụng độ).
D. Mỗi máy tính khi băm cùng một file sẽ ra mã khác nhau.
*Đáp án: C*
*Giải thích: Chỉ cần thay đổi 1 dấu phẩy trong file Word 10GB, mã băm SHA-256 cũng sẽ biến đổi thành một chuỗi Hexadecimal sai khác hoàn toàn.*

**Câu 6:** Một bức thư được ký bằng Chữ ký Số (Digital Signature) thực hiện bởi Alice được gửi cho Bob. Để xác thực đây ĐÚNG LÀ chữ ký của Alice chứ không phải bị giả mạo, Bob phải dùng chìa khóa nào để MỞ khóa chữ ký?
A. Khóa Bí mật của Alice.
B. Khóa Công khai của Bob.
C. Khóa Bí mật của Bob.
D. Khóa Công khai (Public Key) của Alice.
*Đáp án: D*
*Giải thích: Quy tắc vàng của Bất đối xứng: Alice niêm phong chữ ký bằng KHÓA BÍ MẬT của riêng cô ấy. Do đó, DUY NHẤT Khóa CÔNG KHAI của cô ấy mới có thể giải được niêm phong đó. Bất kỳ ai mở được đều phải công nhận người tạo là Alice.*

**Câu 7:** Để chứng minh cho Bob biết cái Khóa Công Khai (Public Key) mà anh ta nhận được TỪ INTERNET là đồ "chính chủ" của Alice chứ không phải do hacker Tráo đổi (Man-in-the-middle), Bob cần kiểm tra cái gì?
A. Nhìn xem chữ cái có viết hoa không.
B. Kiểm tra IP của Alice.
C. Đọc tờ Chứng chỉ Số (Digital Certificate) của Alice, xem nó có mang Chữ Ký bảo lãnh của một Tổ chức Cấp Chứng thực (CA) đáng tin cậy không.
D. Yêu cầu Alice đọc lại Khóa Công Khai qua điện thoại di động.
*Đáp án: C*
*Giải thích: Chứng chỉ số là thẻ Căn cước Công dân của thế giới số. CA (như VeriSign) đóng vai trò Công an đóng dấu đỏ khẳng định Khóa này thuộc về thực thể nào.*

**Câu 8:** Các cuộc tấn công "SQL Injection" vào dữ liệu website hay bẻ khóa mật khẩu người dùng sẽ đi qua lớp bảo vệ nào nếu Tường lửa (Firewall) cấu hình sai?
A. Đi qua lớp Packet Filter (Lọc IP và Port).
B. Đi qua lớp Physical.
C. Đi qua Tường lửa phần cứng nhưng bị chặn ở Tầng Liên Kết.
D. Tường lửa luôn luôn chặn được SQL Injection.
*Đáp án: A*
*Giải thích: Tường lửa lọc gói tin (Packet Filter) chỉ nhìn vỏ ngoài (Port 80/443). Do SQL Injection ngụy trang trong gói tin HTTP hợp lệ, Tường lửa truyền thống sẽ mù lòa mở cửa cho nó đi qua. Cần có IDS/IPS kiểm tra sâu (DPI) để chặn.*

**Câu 9:** HTTPS là giao thức kết hợp giữa HTTP truyền thống và cái gì?
A. IPsec (Bảo mật Tầng Mạng).
B. SSL / TLS (Bảo mật Tầng Giao vận).
C. WPA2 (Bảo mật Wi-Fi).
D. PGP (Bảo mật Email).
*Đáp án: B*
*Giải thích: SSL/TLS chèn một tầng mã hóa ngay bên trên TCP. Khi HTTP đẩy văn bản rõ xuống, TLS sẽ băm và khóa nó thành mớ hỗn độn rồi mới giao cho TCP truyền đi.*

**Câu 10:** Khi thiết lập IPsec (Mạng riêng ảo VPN) để nối thông hai văn phòng, các gói tin dữ liệu bên trong mạng LAN của chi nhánh sẽ được bảo vệ ra sao?
A. Chỉ mã hóa được nội dung web.
B. Được tự động mã hóa TẤT CẢ, bất kể đó là gói tin ứng dụng gì (Web, FTP, Game, Ping), vì IPsec hoạt động mã hóa trong suốt ở mức Tầng Mạng (Network Layer).
C. Được tải lên đám mây.
D. Phải dùng cáp riêng không qua Internet.
*Đáp án: B*
*Giải thích: IPsec nén toàn bộ IP Datagram gốc (kể cả Header IP gốc) vào trong Payload của một IP Datagram IPsec mới, mã hóa sạch sành sanh.*

**Câu 11:** Trong các Firewall (Tường lửa), loại "Stateful Packet Inspection" (Kiểm tra gói tin có trạng thái) cải tiến được nhược điểm nào của bộ lọc cũ?
A. Nó không cần CPU để chạy.
B. Thay vì chỉ kiểm tra từng gói tin rời rạc tĩnh, nó có "Trí nhớ" duy trì một Bảng theo dõi trạng thái các kết nối TCP hiện tại. Nhờ vậy nó biết gói tin đến có thuộc một luồng giao tiếp hợp pháp đang diễn ra hay là một gói rác đột ngột xâm nhập.
C. Nó mã hóa toàn bộ dữ liệu.
D. Nó tìm được địa chỉ nhà của hacker.
*Đáp án: B*
*Giải thích: Nếu một gói tin mang cờ ACK lao từ Internet vào LAN mà trong Bảng trạng thái không hề có kết nối SYN nào được mở ra trước đó, Stateful Firewall sẽ Drop ngay lập tức.*

**Câu 12:** Tính năng DPI (Deep Packet Inspection - Kiểm tra sâu) của thiết bị IDS làm gì?
A. Nó đo cáp mạng chìm dưới đáy biển.
B. Nó lột lớp vỏ TCP/IP để soi thẳng vào ruột Payload Tầng Ứng dụng xem có chứa chuỗi mã độc (Signatures) hoặc hành vi đáng ngờ không.
C. Nó tìm IP của người dùng.
D. Nó chia nhỏ Datagram ra sâu hơn MTU.
*Đáp án: B*
*Giải thích: Giống như Hải quan mở toang vali hàng hóa ra kiểm tra, DPI tốn cực kỳ nhiều CPU và tài nguyên mạng, bù lại có khả năng chống chọi hầu hết sự xâm nhập.*

**Câu 13:** Mã hóa DES (Data Encryption Standard) với khóa 56 bit bị coi là "Cổ vật" không an toàn ở hiện tại do đâu?
A. Giao diện quá xấu.
B. Chiều dài chìa khóa (Key) 56 bit là quá ngắn. Máy tính hiện đại, card màn hình có thể sử dụng phương pháp "Vét cạn" (Brute-force) thử hết 2^56 chìa khóa để bẻ khóa trong vòng 1-2 ngày.
C. Do không cài được trên Windows.
D. Do Microsoft chặn thuật toán.
*Đáp án: B*
*Giải thích: Thuật toán mật mã học bị đánh bại bởi tốc độ vi xử lý tăng theo định luật Moore. Ngày nay khóa tối thiểu của AES là 128 bits, mạnh hơn tỷ tỷ tỷ lần.*

**Câu 14:** Giao thức nào cung cấp bảo mật (Mã hóa và Xác thực) trên kênh truyền Không dây (Wi-Fi)?
A. OSPF
B. WEP, WPA2, WPA3
C. IPsec
D. TLS
*Đáp án: B*
*Giải thích: Chuẩn bảo mật WPA (đặc biệt bản mới nhất WPA3) sử dụng AES để mã hóa các khung vô tuyến (Frame) trực tiếp trước khi phát ra ăng ten.*

**Câu 15:** Vì sao hiện tượng "Packet Sniffing" lại đặc biệt nguy hiểm trên môi trường kết nối Wi-Fi công cộng ở quán cà phê?
A. Vì Wi-Fi công cộng miễn phí cước.
B. Vì sóng Wi-Fi phát tán tứ phía vào không trung. Ai trong quán cũng có thể cài phần mềm bắt được toàn bộ các gói tin bay qua lại của máy tính khác. Nếu không dùng HTTPS, mật khẩu sẽ lộ rõ như ban ngày.
C. Vì Wi-Fi ở quán cafe dùng cáp đồng hỏng.
D. Vì quán cafe thường lắp camera quan sát.
*Đáp án: B*
*Giải thích: Khác với mạng dây (cắm switch) được cô lập, mạng vô tuyến là mạng phát thanh. Hacker chỉ việc dùng card mạng chế độ Promiscuous (Nghe trộm) là thu thập được mọi thứ.*

**Câu 16:** Bạn nhận được email từ ngân hàng yêu cầu nhấp vào link "http://192.168.12.1/login" thay vì "https://bank.com" để cấp lại mật khẩu. Kẻ tấn công đang dùng thủ đoạn nào?
A. DoS Flooding.
B. Man in the Middle.
C. Phishing (Tấn công lừa đảo / Câu cá) kết hợp tạo trang giả.
D. Mã hóa tống tiền.
*Đáp án: C*
*Giải thích: Lợi dụng sự nhẹ dạ và thiếu kỹ năng, hacker gửi một giao diện giống hệt trang thật (nhưng IP/Domain fake) dụ người dùng tự điền pass.*

**Câu 17:** Thuật ngữ "Zero-day exploit" trong an ninh mạng mô tả sự kiện nào?
A. Sự cố mạng mất kết nối vào ngày đầu năm mới.
B. Lỗ hổng bảo mật chưa từng được ai (kể cả nhà sản xuất) biết tới, bị hacker phát hiện và khai thác tận dụng (exploit) trước khi bản vá lỗi kịp tung ra.
C. Mã hóa ổ cứng trong vòng 0 ngày.
D. Việc khởi động lại máy chủ mỗi ngày để xóa bộ nhớ.
*Đáp án: B*
*Giải thích: Zero-day là vũ khí đáng sợ nhất vì không có Antivirus hay Tường lửa nào chặn được nó (vì chưa hề có cơ sở dữ liệu mẫu nhận diện).*

**Câu 18:** Khái niệm "Operational Security" bao gồm các công tác gì để giữ an toàn tổ chức?
A. Cập nhật phần mềm định kỳ, sử dụng Mật khẩu phức tạp đổi định kỳ, sao lưu dữ liệu (Backup), phân quyền hạn chế (Zero Trust), giáo dục nhận thức nhân viên.
B. Chỉ việc mua thiết bị của Cisco.
C. Kéo dây cáp đi qua đường hầm dưới lòng đất.
D. Chỉ sử dụng IPv6.
*Đáp án: A*
*Giải thích: Bạn có thể lắp Tường lửa 1 triệu đô, nhưng nhân viên viết Pass ra giấy nhớ dán lên màn hình thì mạng vẫn sập. Operational Security là việc duy trì quy trình vận hành an toàn.*

**Câu 19:** Mã độc Ransomware hoạt động theo cơ chế nào để tống tiền nạn nhân?
A. Khóa màn hình máy tính lại không cho hiện hình ảnh.
B. Bí mật xâm nhập, lén lút quét tất cả các file tài liệu quan trọng trên đĩa cứng và mã hóa chúng bằng Mã hóa Bất đối xứng (hoặc kết hợp) theo khóa nằm ở máy chủ hacker. Xong xuôi nó xóa file gốc, ép người dùng trả tiền điện tử (Bitcoin) để mua chìa khóa giải mã.
C. Mở loa ngoài to hết cỡ.
D. Truyền vi-rút vào thẻ tín dụng.
*Đáp án: B*
*Giải thích: Mã hóa là công cụ bảo vệ dữ liệu, nhưng Ransomware dùng chính thanh gươm này để phong ấn file nạn nhân thành rác nếu không trả tiền chuộc.*

**Câu 20:** Làm sao để hạn chế cuộc tấn công giả mạo IP (IP Spoofing)?
A. Đóng tất cả các cổng trên Router.
B. Xóa IP cũ nhập IP mới.
C. Các ISP cấu hình Tường lửa/Router kiểm tra tính xác thực của luồng IP: Nếu Router ở mạng nội bộ 10.0.0.x lại nhận được một gói tin có IP Nguồn ghi từ Mỹ đi ra từ mạng nội bộ, router sẽ chặn Drop ngay. Đây gọi là Lọc ở đường ra (Egress Filtering).
D. Không dùng cáp Ethernet.
*Đáp án: C*
*Giải thích: Nhà ai nấy giữ. Router ở mạng X không được phép xuất hành bất kỳ gói tin nào mang IP nguồn mạo danh Y ra ngoài thế giới Internet.*

**Câu 21:** Quá trình "Thỏa thuận khóa phiên" (Session Key Negotiation) trong bước bắt tay giao thức TLS/SSL dùng kỹ thuật gì?
A. Hash mật khẩu của người dùng.
B. Client sinh ngẫu nhiên một Khóa Đối xứng (Session Key), dùng Public Key lấy từ Chứng chỉ số của Server để khóa nó lại, và gửi cục đã khóa lên cho Server.
C. Server sinh ra mã băm MD5 và dùng Private Key mã hóa.
D. IPsec tự động phân phát khóa bằng UDP.
*Đáp án: B*
*Giải thích: Đưa khóa đối xứng qua mạng là điều tối kỵ. Nhưng nhờ Public Key của Server (an toàn tuyệt đối), Client bỏ Session Key vào đó, đóng kín lại. Ai bắt được cục hàng đó trên mạng cũng bó tay, chỉ có Server mới có Private Key để tự mở ra lấy Session Key.*

**Câu 22:** Một Tường lửa (Firewall) cấu hình "Default Deny" (Cấm mặc định) hoạt động theo triết lý gì?
A. Mở cửa tất cả, chỉ cấm các IP nằm trong danh sách đen (Blacklist).
B. Đóng cửa hoàn toàn, không có gói tin nào lọt vào. Bắt buộc phải thêm các ngoại lệ (Whitelist) một cách cực kỳ chi tiết cho những dịch vụ nào được phép lưu thông.
C. Mặc định chỉ cấm ban ngày.
D. Cấm tất cả các lệnh Ping.
*Đáp án: B*
*Giải thích: Tương tự như an ninh sân bay, mặc định là không ai được vào. Chứ không phải thả cửa cho tất cả vào trừ tội phạm truy nã (Default Allow).*

**Câu 23:** Khác biệt giữa Hệ thống phát hiện xâm nhập (IDS) và Hệ thống ngăn chặn xâm nhập (IPS) là gì?
A. Cả hai là một.
B. IDS chỉ cảnh báo (Báo động cho quản trị viên, gửi email), còn IPS thì cảnh báo VÀ tự động đưa ra các hình phạt thực tế (như cắt đứt đường cáp kết nối (Drop) của hacker đang tấn công, cập nhật tường lửa).
C. IPS hoạt động trên Tầng Giao vận, IDS trên Tầng Vật lý.
D. IDS đắt hơn IPS.
*Đáp án: B*
*Giải thích: Detection (Phát hiện) chỉ có chức năng nhìn thấy và la lên. Prevention (Ngăn chặn) có thẩm quyền hành động ngay tại chỗ.*

**Câu 24:** Thuật toán mã hóa khóa Công khai RSA được đặt tên theo điều gì?
A. Thuật toán do Nga thiết kế (Russian Security Algorithm).
B. Tên của trường Đại học nghiên cứu ra nó.
C. Chữ cái đầu tên của 3 nhà phát minh: Ron Rivest, Adi Shamir, và Leonard Adleman.
D. Rất Siêu An toàn.
*Đáp án: C*
*Giải thích: Bộ ba này tại Viện MIT đã tạo ra RSA vào năm 1977, trở thành công nghệ mật mã vĩ đại nhất lịch sử Internet.*

**Câu 25:** Kỹ thuật "Salting" (Rắc muối) khi băm (Hashing) lưu trữ mật khẩu trong cơ sở dữ liệu giải quyết vấn đề gì?
A. Tạo ra mã băm nhỏ hơn.
B. Nếu có hai người dùng đặt cùng một mật khẩu yếu (vd: "123456"), bằng cách ghép thêm một chuỗi "muối" ngẫu nhiên khác nhau vào mật khẩu mỗi người trước khi Hash, mã băm đầu ra sẽ hoàn toàn khác biệt. Giúp chống lại các cuộc tấn công tra bảng băm làm sẵn (Rainbow Tables).
C. Để mật khẩu nhanh được gửi lên hệ thống.
D. Để phá vỡ tường lửa.
*Đáp án: B*
*Giải thích: Muối là chuỗi sinh ngẫu nhiên. Password "123456" + Muối "A" -> Hash X. Password "123456" + Muối "B" -> Hash Y. Hacker trộm data thấy X và Y khác nhau không biết là trùng pass.*

**Câu 26:** Chứng chỉ khóa công khai (X.509) do CA cấp thường bị mất hiệu lực vì nguyên nhân nào phổ biến nhất?
A. CA xóa sổ công ty.
B. Hết thời hạn chứng chỉ (Expiration Date) hoặc bị rò rỉ khóa bí mật của máy chủ khiến CA phải thêm nó vào danh sách Thu hồi Chứng chỉ (CRL - Certificate Revocation List).
C. Thiết bị máy chủ khởi động lại.
D. Bị hacker đổi tên.
*Đáp án: B*
*Giải thích: Tương tự như thẻ ATM, chứng chỉ chỉ sống 1-3 năm. Hoặc nếu bạn báo mất khóa bí mật, CA sẽ đưa chứng chỉ của bạn vào "Danh sách đen" (CRL) để các trình duyệt từ chối.*

**Câu 27:** Các thuật toán mã hóa (AES, RSA) có bị hacker bẻ khóa theo thời gian không?
A. Không bao giờ. Chúng được chứng minh toán học bất khả chiến bại.
B. Có, vì theo Định luật Moore, năng lực vi xử lý (CPU/GPU) tăng liên tục khiến việc Vét cạn (Brute-force) những chiều dài khóa ngắn trở nên khả thi. Và nguy cơ tương lai đến từ sức mạnh của Máy tính Lượng tử.
C. Do máy chủ tự sinh ra lỗi.
D. Tự khóa sẽ hết hạn sau 1 năm.
*Đáp án: B*
*Giải thích: Mã hóa không phải là giấu cách làm (Kerckhoffs's principle). Nó phụ thuộc hoàn toàn vào độ to của chìa khóa. Siêu máy tính cần hàng tỷ năm giải bài toán RSA 2048, nhưng máy lượng tử (Shor's Algorithm) có thể giải trong vài ngày.*

**Câu 28:** VPN (Virtual Private Network) tạo đường hầm ở lớp nào nếu triển khai bằng giao thức IPsec?
A. Lớp Mạng (Network Layer).
B. Lớp Liên kết dữ liệu (Data Link).
C. Lớp Phiên (Session).
D. Lớp Vật lý (Physical).
*Đáp án: A*
*Giải thích: Lớp Mạng (Layer 3) là ngôi nhà của giao thức IP. IPsec hoạt động ở đây che chở trong suốt cho các gói tin Layer 4 bên trên.*

**Câu 29:** Cuộc tấn công Man-in-the-Middle (MITM) là việc hacker chen vào giữa Alice và Bob. Làm sao để chặn triệt để MITM trên kết nối Web?
A. Gửi dữ liệu vào ban đêm.
B. Phân mảnh gói tin làm đôi.
C. Sử dụng Chứng chỉ SSL/TLS được chứng thực bởi CA uy tín, khiến cho hacker không thể làm giả chứng chỉ giả mang Public Key của hắn (vì hacker không có Private Key của CA).
D. Dùng TCP thay cho UDP.
*Đáp án: C*
*Giải thích: Khi hacker chen giữa gửi cái Public Key của hắn cho Alice (giả vờ hắn là Bob), trình duyệt của Alice sẽ báo lỗi ngay lập tức vì cái Public key đó KHÔNG CÓ chữ ký chứng nhận của CA.*

**Câu 30:** Một ứng dụng nhắn tin bảo mật như Signal hay WhatsApp thường quảng bá tính năng E2EE (End-to-End Encryption). Nó có ý nghĩa gì?
A. Nghĩa là ứng dụng miễn phí.
B. Dữ liệu được mã hóa suốt quãng đường. Thậm chí chính máy chủ trung gian của công ty Signal/WhatsApp cũng KHÔNG có chìa khóa để giải mã tin nhắn, mà chỉ có 2 cái điện thoại ở 2 đầu mới có chìa khóa.
C. Nó mã hóa toàn bộ hình ảnh thành văn bản.
D. Nghĩa là gọi video không bị giật lag.
*Đáp án: B*
*Giải thích: E2E có nghĩa mã hóa và giải mã chỉ xảy ra tại thiết bị của người sử dụng (End-systems). Máy chủ của hãng chỉ làm trạm bưu điện chuyển cục gạch mã hóa, nên cảnh sát có đòi thu giữ server cũng vô ích.*

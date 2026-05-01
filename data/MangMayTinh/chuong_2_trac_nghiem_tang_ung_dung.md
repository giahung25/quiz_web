# CHƯƠNG 2: TRẮC NGHIỆM TẦNG ỨNG DỤNG (APPLICATION LAYER)

**Câu 1:** Trong kiến trúc mạng Client-Server, máy chủ (Server) bắt buộc phải có đặc điểm nào sau đây để các máy khách (Client) có thể tìm và kết nối ổn định?
A. Phải luôn thay đổi địa chỉ IP động để tăng tính bảo mật.
B. Phải có một địa chỉ IP tĩnh, cố định và luôn luôn hoạt động (always-on).
C. Phải chủ động khởi tạo liên lạc tới các máy khách.
D. Chỉ hoạt động trong giờ hành chính.
*Đáp án: B*
*Giải thích: Do client luôn là người chủ động gọi kết nối, server phải ở đó chờ sẵn (always-on) và phải giữ nguyên địa chỉ nhà (IP tĩnh) thì client mới gõ cửa được.*

**Câu 2:** Kiến trúc mạng ngang hàng (P2P - Peer-to-Peer) giải quyết vấn đề lớn nhất nào của kiến trúc Client-Server truyền thống?
A. Vấn đề mã hóa dữ liệu.
B. Vấn đề bảo mật chống lại virus.
C. Nút thắt cổ chai (bottleneck) ở máy chủ khi có lượng lớn người dùng tải dữ liệu cùng lúc, nhờ khả năng tự mở rộng băng thông (mỗi client tự làm server cho người khác).
D. Phân giải tên miền (DNS).
*Đáp án: C*
*Giải thích: P2P tự phân phối gánh nặng truyền tải băng thông cho tất cả các máy cùng tải file, biến nhược điểm đông người thành ưu điểm.*

**Câu 3:** Khái niệm "Socket" trong lập trình mạng máy tính là gì?
A. Là cổng kết nối vật lý (RJ45) để cắm dây mạng vào máy tính.
B. Là giao diện phần mềm lập trình (API) kết nối giữa tiến trình của Ứng dụng (Application process) và giao thức tầng Giao vận (Transport layer).
C. Là một cửa sổ của trình duyệt web.
D. Là đoạn mã hóa mật khẩu của Router.
*Đáp án: B*
*Giải thích: Socket là cánh cửa ảo do hệ điều hành cung cấp. Ứng dụng đẩy data vào socket, hệ điều hành sẽ nhặt data đó bỏ vào TCP hoặc UDP để truyền đi.*

**Câu 4:** Để xác định chính xác một tiến trình ứng dụng (ví dụ: máy chủ Web HTTP) đang chạy trên một máy tính từ xa trong hàng chục tiến trình khác, ta cần sử dụng thông tin định danh nào?
A. Địa chỉ IP của máy tính đó.
B. Địa chỉ MAC của máy tính đó.
C. Địa chỉ IP của máy đó kết hợp với Số hiệu cổng (Port Number) của tiến trình.
D. Tên của hệ điều hành.
*Đáp án: C*
*Giải thích: IP dẫn đường gói tin tới đúng chiếc máy tính phần cứng. Port dẫn đường gói tin lọt vào đúng ứng dụng phần mềm bên trong máy tính đó.*

**Câu 5:** Giao thức TCP cung cấp dịch vụ gì cho các ứng dụng ở tầng trên?
A. Không đảm bảo gói tin tới đích.
B. Tốc độ truyền cực kỳ nhanh nhờ bỏ qua kết nối.
C. Truyền tải dữ liệu tin cậy (không lỗi, không mất, đúng thứ tự) và có cơ chế kiểm soát tắc nghẽn luồng.
D. Phân giải tên miền ra địa chỉ IP.
*Đáp án: C*
*Giải thích: TCP là bảo chứng cho sự tin cậy. Dữ liệu ném vào TCP chắc chắn sẽ đến tay người nhận hoàn hảo, hoặc TCP sẽ báo lỗi nếu mạng sập.*

**Câu 6:** Giao thức UDP (User Datagram Protocol) phù hợp nhất với loại ứng dụng mạng nào dưới đây?
A. Gửi email (SMTP)
B. Chuyển tiền ngân hàng
C. Hội thoại Video thời gian thực (Video Call/VoIP)
D. Tải tệp tin (FTP)
*Đáp án: C*
*Giải thích: Video call nhạy cảm với thời gian (delay) hơn là mất mát. UDP nhẹ, nhanh, không bắt tay lằng nhằng, rớt vài khung hình (vài gói tin) không ảnh hưởng nghiêm trọng.*

**Câu 7:** HTTP là giao thức "Phi trạng thái" (Stateless). Điều này có nghĩa là gì đối với máy chủ Web?
A. Máy chủ không mã hóa dữ liệu.
B. Máy chủ không hề lưu giữ thông tin hay ghi nhớ bất kỳ trạng thái nào về các yêu cầu trước đó của cùng một Client.
C. Máy chủ sẽ ngắt kết nối Internet nếu trạng thái đường truyền kém.
D. Trình duyệt không thể lưu Bookmark.
*Đáp án: B*
*Giải thích: Nếu bạn request trang A, sau đó 1 giây lại request trang A, máy chủ Stateless sẽ phục vụ bạn lại từ đầu y hệt một người hoàn toàn lạ mặt.*

**Câu 8:** Công cụ nào sinh ra để vá lại lỗ hổng "Phi trạng thái" của HTTP, giúp các trang web e-commerce có thể nhớ được bạn đã bỏ mặt hàng gì vào giỏ hàng?
A. DNS Records
B. HTML5
C. Caching (Proxy)
D. Cookies
*Đáp án: D*
*Giải thích: Cookies được server đóng dấu lên trình duyệt. Các yêu cầu sau của trình duyệt sẽ mang theo cái dấu đó (Cookie ID) để Server nhận diện người quen.*

**Câu 9:** Chữ "S" trong chuẩn HTTPS đại diện cho giao thức mã hóa nào hoạt động ngay dưới tầng HTTP để bảo vệ dữ liệu khỏi nghe lén?
A. SMTP
B. SSL/TLS
C. SSH
D. SAN
*Đáp án: B*
*Giải thích: HTTPS thực chất là HTTP chạy trên nền Transport Layer Security (TLS), trước đây gọi là SSL.*

**Câu 10:** Sự khác biệt giữa Web Caching (Proxy Server) và Origin Server (Máy chủ gốc) là gì?
A. Origin server nằm ở gần người dùng hơn.
B. Web cache chỉ lưu giữ BẢN SAO của các nội dung web phổ biến, giúp giảm độ trễ cho người dùng nội bộ, trong khi Origin Server là nơi thực sự lưu bản gốc do nhà phát triển web tải lên.
C. Web cache dùng để phát video, Origin server dùng để lưu HTML.
D. Web cache là thuật ngữ khác của thẻ SD.
*Đáp án: B*
*Giải thích: Mạng công ty mua 1 con Proxy làm Web Cache để mọi nhân viên đọc chung báo VnExpress một cách siêu tốc mà không làm tốn băng thông chung ra Internet.*

**Câu 11:** Nếu một trang HTML cơ sở chứa 10 hình ảnh nhúng, khi sử dụng HTTP/1.0 Non-persistent (Không bền bỉ), trình duyệt sẽ phải mở bao nhiêu kết nối TCP?
A. 1 kết nối duy nhất
B. 10 kết nối
C. 11 kết nối (1 cho HTML + 10 cho ảnh)
D. 2 kết nối
*Đáp án: C*
*Giải thích: Non-persistent tức là cứ tải xong 1 file thì đóng luôn TCP. Vậy 11 đối tượng sẽ phải trải qua 11 lần quá trình bắt tay TCP.*

**Câu 12:** Lợi ích của HTTP/1.1 Persistent (Bền bỉ) so với bản Non-persistent là gì?
A. Máy chủ dùng Cookie tốt hơn.
B. Trình duyệt không cần phải xin lại IP từ DNS.
C. Kết nối TCP được giữ MỞ sau khi tải file đầu tiên, giúp tiết kiệm RTT (Round Trip Time) và tài nguyên CPU cho các tệp tin tiếp theo lấy từ cùng một máy chủ.
D. Hình ảnh trên web sẽ tự động nén nhỏ lại.
*Đáp án: C*
*Giải thích: Không phải lặp lại bắt tay 3 bước TCP cho mỗi tấm ảnh, làm tăng tốc độ hiển thị trang lên rất nhiều.*

**Câu 13:** Trong hệ thống Thư điện tử (Email), giao thức SMTP được sử dụng cho giai đoạn nào?
A. Để người dùng đọc thư trên điện thoại di động (Pull).
B. Để đính kèm các tệp tin lớn.
C. Để GỬI ĐẨY (Push) thư từ máy tính của người gửi lên Mail Server và đẩy từ Mail Server này sang Mail Server khác.
D. Để mã hóa thư rác (Spam).
*Đáp án: C*
*Giải thích: SMTP (Simple Mail Transfer Protocol) là một Push Protocol. Nó chỉ có chức năng đẩy thư ra đi.*

**Câu 14:** Giao thức nào thường được sử dụng để KÉO (Pull) thư từ Mail Server về phần mềm như Microsoft Outlook của máy khách?
A. SMTP
B. IMAP hoặc POP3
C. FTP
D. SNMP
*Đáp án: B*
*Giải thích: POP3 (tải về cục bộ rồi xóa trên server) và IMAP (duy trì trạng thái đồng bộ nhiều thư mục trên server) là các Pull protocol dành cho nhận email.*

**Câu 15:** Vì sao ứng dụng truy vấn DNS lại sử dụng tầng giao vận UDP thay vì TCP?
A. Vì dữ liệu truy vấn của DNS thường lớn hàng chục Megabyte.
B. Vì DNS ưu tiên tốc độ phản hồi cực nhanh, không muốn tốn 1 RTT để thiết lập bắt tay, và bản tin DNS nhỏ nên nếu rớt có thể gửi lại ngay lập tức.
C. Vì UDP an toàn và bảo mật hơn chống lại tin tặc.
D. Vì router từ chối các kết nối TCP port 53.
*Đáp án: B*
*Giải thích: Truy vấn DNS là: "Ông ơi IP của google là gì?" - "Đây 142.250.x.x". Thông điệp quá nhỏ, dùng TCP bắt tay sẽ làm chậm đi rất nhiều.*

**Câu 16:** Các máy chủ Root DNS (Gốc) trả về thông tin gì khi được hỏi về một địa chỉ IP (ví dụ www.google.com)?
A. Trả về chính xác địa chỉ IP của www.google.com
B. Trả về địa chỉ IP của một Máy chủ TLD (Top-Level Domain) quản lý đuôi .com.
C. Trả về lỗi 404.
D. Trả về địa chỉ của modem mạng nhà bạn.
*Đáp án: B*
*Giải thích: DNS là hệ thống phân cấp. Root chỉ biết đường chỉ tay đến TLD (.com, .org). TLD lại chỉ tay về Authoritative (máy chủ của Google).*

**Câu 17:** Thuật toán nào giúp hệ thống BitTorrent lựa chọn các máy ngang hàng (Peer) nào để ưu tiên Upload (gửi dữ liệu)?
A. Cây khung (Spanning Tree).
B. FIFO (Đến trước phục vụ trước).
C. Tit-for-tat (Hòn bấc ném đi, hòn chì ném lại) - ưu tiên các máy nào đang download lại cho mình với tốc độ cao nhất.
D. Bầu chọn ngẫu nhiên.
*Đáp án: C*
*Giải thích: Tit-for-tat ngăn chặn hiện tượng "Free-rider" (chỉ tải về không chịu tải lên) trong mạng P2P, ép mọi người phải cống hiến băng thông.*

**Câu 18:** Kỹ thuật DASH (Dynamic Adaptive Streaming over HTTP) dùng trong Netflix và YouTube có nguyên lý gì đặc biệt?
A. Chuyển tín hiệu truyền hình cáp vào trong cáp quang.
B. Video được lưu thành hàng trăm file nhỏ (chunks) với các chất lượng/độ phân giải khác nhau. Trình duyệt tự đo tốc độ mạng hiện tại để linh hoạt chọn tải đoạn file chất lượng cao hay thấp phù hợp để chống giật (buffering).
C. Mã hóa video bằng RSA để chống vi phạm bản quyền.
D. Tự động tắt máy chủ nếu có quá nhiều người xem.
*Đáp án: B*
*Giải thích: Chữ Adaptive (Thích ứng) cho thấy việc chuyển đổi mượt mà giữa mờ/nét tùy vào đường truyền mạng lúc đang xem.*

**Câu 19:** Hạ tầng CDN (Content Delivery Network) mang lại lợi ích gì cho các website toàn cầu?
A. Cấm truy cập từ các quốc gia bị liệt vào sổ đen.
B. Dùng một Server siêu to khổng lồ duy nhất đặt ở Mỹ để phục vụ 8 tỷ người.
C. Giảm đáng kể độ trễ bằng cách đưa các cụm máy chủ lưu trữ bản sao nội dung (Replica Cache) lại gần sát với vị trí địa lý của khách hàng nhất có thể.
D. Giảm dung lượng file video.
*Đáp án: C*
*Giải thích: CDN là chìa khóa để Internet không bị nghẽn cổ chai khi hàng triệu người cùng xem một trận chung kết bóng đá.*

**Câu 20:** Lệnh nào là một HTTP Method dùng để gửi dữ liệu mẫu (Form) của người dùng từ Trình duyệt lên Server?
A. SEND
B. UPLOAD
C. GET
D. POST
*Đáp án: D*
*Giải thích: GET chủ yếu để yêu cầu nội dung (với tham số đính kèm ở URL), còn POST để nộp cục dữ liệu lớn (form, upload) giấu trong phần body của message.*

**Câu 21:** Nếu một bản ghi DNS thuộc kiểu "MX" (Mail Exchanger), trường dữ liệu giá trị (Value) của nó sẽ cung cấp thông tin gì?
A. Địa chỉ IPv4 của trang web.
B. Địa chỉ IP của máy chủ DNS.
C. Tên miền thực (Canonical name) của một bí danh.
D. Tên (Hostname) của hệ thống máy chủ phụ trách nhận Thư điện tử cho tên miền đó.
*Đáp án: D*
*Giải thích: Khi bạn gửi mail tới @gmail.com, giao thức ngầm hỏi DNS "Record MX của gmail.com là gì" để biết Mail Server đích ở đâu mà đẩy tới bằng SMTP.*

**Câu 22:** Máy chủ DNS có thẩm quyền (Authoritative DNS Server) là gì?
A. Máy chủ quản lý các tên miền .com và .org.
B. Máy chủ DNS nội bộ của nhà cung cấp dịch vụ Internet (như VNPT, FPT) đứng ra hỏi giùm bạn.
C. Máy chủ thuộc sở hữu của tổ chức chứa thông tin ánh xạ IP gốc, chính xác tuyệt đối do chính tổ chức đó cấu hình cho website của họ.
D. Máy chủ dùng chung của Google (8.8.8.8).
*Đáp án: C*
*Giải thích: Authoritative là điểm kết thúc cuối cùng của chuỗi tra cứu phân giải tên miền. Tổ chức tự quản lý IP của mình trên máy chủ này.*

**Câu 23:** Cổng (Port) là khái niệm ở Tầng Giao vận, nhưng là thứ sống còn để thiết lập Socket ở Tầng Ứng dụng. Dải cổng được cấp phép chuẩn (Well-known ports) giới hạn từ đâu đến đâu?
A. Từ 0 đến 65535
B. Từ 0 đến 1023
C. Từ 1024 đến 49151
D. Từ 0 đến 255
*Đáp án: B*
*Giải thích: IANA quy định dải port từ 0 đến 1023 cho các giao thức mạng hệ thống phổ biến (HTTP 80, FTP 21, SSH 22).*

**Câu 24:** Thông điệp HTTP Response từ Server mang theo một mã trạng thái "404 Not Found" ở ngay dòng đầu tiên (Status line). Điều này có ý nghĩa gì?
A. Trình duyệt bị mất kết nối mạng.
B. Yêu cầu thành công, dữ liệu nằm ở dưới.
C. Máy chủ không hiểu được cú pháp yêu cầu.
D. Tài liệu (đối tượng) mà trình duyệt yêu cầu không tồn tại trên máy chủ.
*Đáp án: D*
*Giải thích: Mã 2xx là thành công. 3xx là điều hướng. 4xx là lỗi do khách hàng yêu cầu sai (vd: file không có). 5xx là lỗi sập server nội bộ.*

**Câu 25:** Quá trình "Truy vấn đệ quy" (Recursive Query) trong DNS khác với "Truy vấn lặp" (Iterative Query) ở điểm nào?
A. Trong đệ quy, máy chủ DNS được hỏi sẽ tự mình gánh trách nhiệm liên hệ tiếp với máy chủ khác để tìm bằng được kết quả trả về, thay vì chỉ tay "hãy đi hỏi ông kia" như Iterative.
B. Đệ quy chỉ dùng trong mạng LAN, lặp dùng trên Internet.
C. Truy vấn lặp nhanh hơn đệ quy gấp đôi.
D. Truy vấn đệ quy không thể bị bắt gói tin.
*Đáp án: A*
*Giải thích: Cấu hình mặc định thường là máy bạn hỏi đệ quy lên Local DNS. Sau đó Local DNS làm công việc cực nhọc là đi hỏi Lặp (Iterative) lên Root, TLD...*

**Câu 26:** Ứng dụng "Skype" hoặc "Zoom" yêu cầu tiêu chí nào khắt khe nhất từ phía dịch vụ mạng?
A. Không bao giờ được mất một byte dữ liệu nào.
B. Độ trễ và jitter thời gian thực (Timing / Delay) phải cực thấp.
C. Băng thông tối thiểu 1 Gbps.
D. Mã hóa RSA 4096-bit.
*Đáp án: B*
*Giải thích: Ứng dụng đàm thoại trực tiếp đòi hỏi độ trễ thường < 150ms để tạo cảm giác tự nhiên. Mất vài pixel khung hình vẫn chấp nhận được.*

**Câu 27:** Mạng P2P có đặc điểm gì giúp việc phát tán file trở nên "Tự mở rộng" (Self-scalability)?
A. Máy chủ được tự động phân bổ RAM.
B. Khi càng nhiều Peer tham gia mạng để download, tổng nhu cầu tải về tăng, nhưng ĐỒNG THỜI năng lực upload của toàn mạng cũng tăng lên tương xứng do chính các peer đó đóng góp.
C. Mạng dùng cáp quang nên tự động giãn nở băng thông.
D. ISP không thể kiểm soát được dữ liệu.
*Đáp án: B*
*Giải thích: Khác với Client-server, P2P mang theo định lý "mỗi người đến ăn tiệc đều mang theo một đĩa thức ăn".*

**Câu 28:** Trong BitTorrent, thuật ngữ "Choked" và "Unchoked" mô tả trạng thái gì giữa các peer?
A. Mạng bị đứt cáp và mạng đã nối lại.
B. Hành động máy trạm A ngắt không gửi data (Choke) hoặc đồng ý mở vòi gửi data (Unchoke) cho máy trạm B dựa trên thuật toán đánh giá tốc độ trao đổi.
C. Bị nhiễm virus và đã diệt virus.
D. Mã hóa và giải mã file zip.
*Đáp án: B*
*Giải thích: Tit-for-tat duy trì 4 peer "unchoked" (gửi dữ liệu) và choke tất cả những người còn lại để phạt những kẻ xài chùa.*

**Câu 29:** Nếu một Server muốn thông báo cho Client về việc điều hướng trang web (ví dụ truy cập http://abc.com bị đẩy sang https://abc.com), mã phản hồi HTTP nào sẽ được dùng?
A. 200 OK
B. 301 Moved Permanently (Hoặc các mã 3xx)
C. 403 Forbidden
D. 500 Internal Server Error
*Đáp án: B*
*Giải thích: Các mã 3xx dùng cho Redirect. Trình duyệt nhận được sẽ tự động tải địa chỉ mới nằm trong trường header Location.*

**Câu 30:** Ứng dụng mạng (Network Application) chạy trên nền hệ điều hành được gọi chung là gì?
A. Frame
B. Thread
C. Protocol
D. Tiến trình (Process)
*Đáp án: D*
*Giải thích: Bất kỳ phần mềm nào đang được thực thi trên OS (như Chrome, Apache, Zoom) đều là một Process. Các Process này liên lạc qua Socket.*

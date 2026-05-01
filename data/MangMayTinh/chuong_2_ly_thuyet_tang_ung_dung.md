# CHƯƠNG 2: TẦNG ỨNG DỤNG (APPLICATION LAYER)

## 2.1 Nguyên lý của các ứng dụng mạng (Principles of Network Applications)

Tầng ứng dụng là nơi các ứng dụng mạng (network applications) và các giao thức của chúng cư trú. Phát triển một ứng dụng mạng có nghĩa là viết các chương trình phần mềm chạy trên nhiều hệ thống đầu cuối (end systems) khác nhau và giao tiếp với nhau qua mạng. Điểm cốt lõi là bạn KHÔNG cần phải viết phần mềm chạy trên các thiết bị lõi mạng (như router hay switch) vì chúng chỉ hoạt động ở các tầng thấp hơn.

### 2.1.1 Các kiến trúc ứng dụng (Application Architectures)
Khi thiết kế một ứng dụng, nhà phát triển thường chọn một trong hai mô hình kiến trúc phổ biến:

**1. Kiến trúc Client-Server (Khách-Chủ):**
- **Server (Máy chủ):** Là một host luôn luôn hoạt động (always-on), có một địa chỉ IP tĩnh cố định (permanent IP address). Nó chờ đợi các yêu cầu đến từ các client và phục vụ chúng. Khi số lượng client lớn, một server duy nhất không thể kham nổi, người ta sử dụng các cụm máy chủ (server farm/data center) để mở rộng quy mô.
- **Client (Máy khách):** Các thiết bị của người dùng (PC, smartphone) kết nối đến server. Client không cần phải luôn luôn hoạt động và có thể thay đổi địa chỉ IP động. Đáng chú ý, trong kiến trúc này, các client KHÔNG GIAO TIẾP TRỰC TIẾP với nhau (ví dụ: trình duyệt web không liên lạc với trình duyệt web khác, chúng chỉ liên lạc với Web Server).

**2. Kiến trúc P2P (Peer-to-Peer / Ngang hàng):**
- Không có một máy chủ trung tâm luôn hoạt động.
- Các thiết bị đầu cuối, được gọi là các nút mạng ngang hàng (peers), giao tiếp trực tiếp với nhau. Các peers thường là máy tính của người dùng bình thường.
- Đặc tính nổi bật của P2P là **Khả năng tự mở rộng (Self-scalability):** Mỗi peer vừa là người yêu cầu dịch vụ (client) vừa là người cung cấp dịch vụ (server) cho peer khác. Ví dụ, trong BitTorrent, khi một người tải file về, họ đồng thời cũng đang upload file đó cho những người khác.
- Nhược điểm: Phức tạp trong quản lý, bảo mật kém và phụ thuộc vào sự tự nguyện tham gia của các nút.

### 2.1.2 Giao tiếp giữa các tiến trình (Processes Communicating)
Trên một hệ điều hành, chương trình đang chạy được gọi là một **Tiến trình (Process)**. Khi hai tiến trình chạy trên cùng một máy tính, chúng giao tiếp với nhau thông qua cơ chế Inter-Process Communication (IPC) của hệ điều hành. Tuy nhiên, trong mạng máy tính, chúng quan tâm đến việc các tiến trình chạy trên HAI MÁY TÍNH KHÁC NHAU giao tiếp với nhau. Chúng thực hiện điều này bằng cách trao đổi các thông điệp (messages) qua mạng.

**Socket:**
Mọi tiến trình gửi hoặc nhận thông điệp mạng thông qua một giao diện phần mềm gọi là **Socket**. Socket giống như một "cánh cửa" giữa tiến trình ứng dụng và giao thức vận chuyển (Transport protocol).
- Tiến trình đẩy thông điệp ra ngoài cánh cửa (socket).
- Nó dựa vào hạ tầng giao vận bên ngoài cánh cửa đó để mang thông điệp tới socket của tiến trình nhận.
- Giao diện Socket là API (Application Programming Interface) giữa ứng dụng và mạng. Lập trình viên có toàn quyền kiểm soát tầng ứng dụng nhưng chỉ có một chút quyền kiểm soát đối với tầng transport (như chọn TCP hay UDP, thiết lập một số tham số bộ đệm).

**Địa chỉ của Tiến trình (Addressing Processes):**
Để gửi thông điệp cho một tiến trình đích, hệ thống nguồn cần biết hai thông tin:
1. **Địa chỉ IP của Host đích:** (ví dụ: 192.168.1.5) dùng để chuyển gói tin tới đúng chiếc máy tính đó.
2. **Số hiệu Cổng (Port Number):** (ví dụ: Port 80) dùng để xác định chính xác tiến trình/ứng dụng nào trên máy tính đó sẽ nhận dữ liệu. Một máy tính có thể chạy cùng lúc Web server, Mail server, Game server... Port number là định danh cho tiến trình.
   - HTTP Web Server mặc định dùng Port 80.
   - HTTPS dùng Port 443.
   - Mail Server (SMTP) dùng Port 25.

### 2.1.3 Các dịch vụ mà tầng Giao vận cung cấp cho tầng Ứng dụng
Khi ứng dụng đẩy thông điệp qua Socket, nó kỳ vọng tầng Giao vận (Transport Layer) ở dưới thực hiện việc vận chuyển. Các ứng dụng có yêu cầu khác nhau về dịch vụ giao vận, thường chia làm 4 yếu tố:
1. **Truyền dữ liệu tin cậy (Reliable Data Transfer):** Ứng dụng như Web, Email, File transfer yêu cầu 100% dữ liệu phải tới đích không bị lỗi và không bị mất (No data loss). Nếu mạng mất gói, giao thức vận chuyển phải tự truyền lại. Ngược lại, ứng dụng âm thanh/video thời gian thực có thể chấp nhận mất một số dữ liệu (loss-tolerant).
2. **Băng thông (Throughput):** Một số ứng dụng yêu cầu băng thông tối thiểu để hoạt động trơn tru (ví dụ Video 4K cần băng thông lớn). Chúng gọi là bandwidth-sensitive applications. Ngược lại, Elastic applications (như Email, File transfer) có thể chạy với bất kỳ băng thông nào có sẵn.
3. **Thời gian (Timing):** Đảm bảo độ trễ (delay) từ người gửi tới người nhận phải rất thấp. Quan trọng cho ứng dụng gọi thoại (Internet telephony), game online.
4. **Bảo mật (Security):** Mã hóa dữ liệu để chống nghe lén.

---

## 2.2 Các Giao thức Tầng Ứng dụng cốt lõi của Internet

### 2.2.1 TCP và UDP
Internet cung cấp 2 giao thức Transport chính cho ứng dụng sử dụng:
- **Dịch vụ TCP (Transmission Control Protocol):** Cung cấp truyền tải tin cậy (đảm bảo không mất gói, đúng thứ tự), cung cấp cơ chế kiểm soát luồng (flow control) và kiểm soát tắc nghẽn (congestion control). TCP là giao thức Hướng kết nối (Connection-oriented), yêu cầu 2 bên thiết lập kết nối trước (qua cơ chế bắt tay 3 bước - 3-way handshake) rồi mới truyền dữ liệu.
- **Dịch vụ UDP (User Datagram Protocol):** Rất nhẹ và đơn giản. Nó là giao thức Phi kết nối (Connectionless). UDP KHÔNG đảm bảo truyền tin cậy (gói tin có thể mất hoặc sai thứ tự), KHÔNG kiểm soát tắc nghẽn. Ưu điểm của nó là tốc độ cực nhanh, thích hợp cho Streaming Video, DNS.

### 2.2.2 Web và HTTP
**HTTP (HyperText Transfer Protocol)** là giao thức trung tâm của Web. HTTP hoạt động theo mô hình Client-Server.
- Client (thường là Web browser) gửi HTTP Request.
- Server (Web server như Apache, Nginx) phản hồi bằng HTTP Response chứa các đối tượng Web (HTML, ảnh, video).

**Đặc điểm của HTTP:**
- **Sử dụng TCP** làm giao thức giao vận ở tầng dưới (port 80). Nhờ vậy, HTTP không cần lo lắng về việc mất mát dữ liệu.
- **Stateless (Phi trạng thái):** Bản thân HTTP là một giao thức phi trạng thái. Máy chủ HTTP KHÔNG lưu giữ bất kỳ thông tin nào về các yêu cầu trước đó của client. Nếu bạn gửi yêu cầu file A, rồi 2 giây sau lại yêu cầu file A, máy chủ vẫn sẽ phục vụ bạn lại từ đầu như chưa từng quen biết.

**HTTP Non-persistent (Không bền bỉ) vs Persistent (Bền bỉ):**
- *Non-persistent HTTP (HTTP/1.0):* Đối với mỗi đối tượng web (ví dụ 1 trang HTML có 10 bức ảnh), một kết nối TCP riêng biệt phải được tạo lập để tải đối tượng đó. Tải xong 1 file, kết nối TCP bị đóng. Điều này gây ra độ trễ cực lớn do phải lặp lại quá trình thiết lập kết nối (tốn RTT - Round Trip Time) cho mỗi đối tượng.
- *Persistent HTTP (HTTP/1.1):* Máy chủ giữ cho kết nối TCP mở (open) sau khi gửi phản hồi. Các request/response tiếp theo giữa cùng một client-server được gửi qua cùng một kết nối TCP này. Giúp tiết kiệm rất nhiều RTT và CPU.

**Cookies:**
Bởi vì HTTP là stateless, các trang web (như trang mua sắm trực tuyến) cần một cơ chế để theo dõi người dùng. Họ sử dụng Cookies.
Quy trình:
1. HTTP Response từ Server mang theo header `Set-cookie: 1678`.
2. Browser nhận được, lưu cookie `1678` vào ổ cứng.
3. Các HTTP Request sau này từ Browser gửi lên Server sẽ đính kèm header `Cookie: 1678`. Nhờ đó Server nhận diện được người dùng cũ.

**Web Caching (Proxy Server):**
Web cache là một thực thể mạng lưu trữ bản sao của các trang web gần đây. Nó đứng giữa Client và Origin Server.
- Khi Browser cần một trang, nó gửi HTTP Request tới Web Cache.
- Nếu Cache có file đó, nó lập tức gửi lại cho Browser. (Rất nhanh)
- Nếu Cache không có, Cache sẽ gửi Request lên Origin Server lấy file về, lưu lại 1 bản, rồi gửi cho Browser.
Mục đích của Web Cache là giảm đáng kể thời gian phản hồi (response time) cho người dùng và giảm lưu lượng giao thông trên các đường liên kết (link) truy cập ra ngoài Internet của tổ chức. HTTP có cung cấp một header `If-Modified-Since` trong Conditional GET để Cache kiểm tra xem file trên Origin Server có bị thay đổi hay chưa, để quyết định có dùng lại bản lưu nội bộ hay không.

### 2.2.3 Electronic Mail (SMTP, POP3, IMAP)
Hệ thống Email có 3 thành phần chính:
1. **User Agents (Trình đọc mail):** Như Outlook, Apple Mail.
2. **Mail Servers:** Nơi chứa các hộp thư (mailbox) của người dùng.
3. **SMTP (Simple Mail Transfer Protocol):** Giao thức truyền tải mail.

**Quy trình gửi Email:**
Khi Alice gửi mail cho Bob:
1. User Agent của Alice dùng **SMTP** (sử dụng TCP port 25) để đẩy thư lên Mail Server của Alice.
2. Mail Server của Alice đóng vai trò là SMTP Client, dùng **SMTP** chuyển thư tới Mail Server của Bob (đóng vai trò SMTP Server). Thư được lưu vào mailbox của Bob.
3. Bob dùng một *Mail Access Protocol* (Giao thức truy xuất thư) như **POP3** (Post Office Protocol v3), **IMAP** (Internet Message Access Protocol) hoặc **HTTP** (Webmail) để tải hoặc xem thư từ Mail Server của anh ấy về User Agent của mình.

**Lưu ý:** KHÔNG dùng SMTP để kéo (pull) thư từ server về máy. SMTP là một giao thức đẩy (push protocol).

### 2.2.4 DNS (Domain Name System)
Trong mạng, các router định tuyến gói tin dựa vào địa chỉ IP (ví dụ: `142.250.190.46`). Tuy nhiên, con người thích sử dụng các tên miền dễ nhớ (hostname) như `www.google.com`. Nhiệm vụ của DNS là dịch (dịch vụ phân giải) Hostname thành IP address.

DNS là:
1. Một cơ sở dữ liệu phân tán theo cấu trúc phân cấp (distributed, hierarchical database).
2. Một giao thức tầng Ứng dụng cho phép các host truy vấn cơ sở dữ liệu này. Nó sử dụng giao thức **UDP ở port 53**.

**Cấu trúc phân cấp của máy chủ DNS:**
Không có một máy chủ DNS nào chứa toàn bộ bản đồ Internet. Thay vào đó nó phân cấp:
- **Root DNS Servers:** Cấp cao nhất. Trả về địa chỉ của máy chủ TLD.
- **Top-Level Domain (TLD) Servers:** Quản lý các đuôi `.com`, `.org`, `.net`, `.vn`... Trả về địa chỉ của máy chủ Authoritative.
- **Authoritative DNS Servers (Máy chủ có thẩm quyền):** Thuộc về các tổ chức, doanh nghiệp (như máy chủ DNS của Facebook, của trường đại học). Chứa bản đồ mapping chính xác tên miền cụ thể (vd: `www.facebook.com`) sang IP.

Ngoài ra còn có **Local DNS Server** (Máy chủ DNS cục bộ) do ISP cung cấp (ví dụ router wifi nhà bạn). Khi thiết bị của bạn truy vấn DNS, nó sẽ hỏi Local DNS trước. Local DNS sẽ thực hiện các truy vấn đệ quy (recursive) hoặc lặp (iterative) lên hệ thống phân cấp Root -> TLD -> Authoritative để lấy IP về cho bạn.
DNS cũng sử dụng cơ chế Caching một cách sâu rộng để tăng tốc quá trình phân giải và giảm tải cho các Root server.

### 2.2.5 P2P File Distribution (Mạng chia sẻ tệp ngang hàng)
Khác với Client-Server nơi Server gánh toàn bộ tải truyền file, trong P2P, gánh nặng được chia sẻ cho các peers.
Giao thức P2P nổi tiếng nhất là **BitTorrent**.
- Trong BitTorrent, một tệp lớn được chia thành nhiều "chunks" (mảnh) kích thước 256KB.
- Những người dùng tham gia tải/phân phối một file gọi chung là một **Torrent**.
- Khi Alice tham gia một Torrent, ban đầu cô chưa có chunk nào. Cô kết nối vào mạng, hỏi danh sách các peer khác đang giữ các chunk của file từ một máy chủ theo dõi (Tracker).
- Alice song song tải các chunk cô còn thiếu từ các peer khác, và đồng thời đẩy các chunk cô đã có cho người khác.
- Lựa chọn Peer: BitTorrent sử dụng thuật toán "tit-for-tat" (hòn bấc ném đi, hòn chì ném lại). Alice sẽ ưu tiên gửi dữ liệu (unchoke) cho 4 peer nào đang gửi dữ liệu cho cô với tốc độ nhanh nhất.

### 2.2.6 Video Streaming và CDN
**HTTP Streaming (DASH):**
Ngày nay, hầu hết video (như YouTube, Netflix) được phát qua giao thức **DASH** (Dynamic Adaptive Streaming over HTTP).
- Video được chia thành các đoạn nhỏ (ví dụ vài giây).
- Mỗi đoạn được mã hóa (encode) ở nhiều chất lượng/độ phân giải khác nhau (bitrates).
- Một file *Manifest* chứa danh sách các URL tương ứng với từng đoạn và từng chất lượng.
- Client (Trình phát video) liên tục đo lường băng thông hiện tại. Tùy vào mạng đang mạnh hay yếu, Client tự động chủ động yêu cầu tải đoạn video chất lượng cao hay thấp tiếp theo (Adaptive).

**CDN (Content Delivery Networks):**
Để cung cấp lượng dữ liệu video khổng lồ cho người dùng toàn cầu mà không bị nghẽn mạng, các công ty sử dụng CDN. CDN là các hệ thống gồm hàng ngàn máy chủ lưu trữ bản sao nội dung (cache) đặt rải ráp khắp nơi trên thế giới.
- Khi người dùng ở Việt Nam truy cập một video của Mỹ, hệ thống DNS sẽ thông minh điều hướng (redirect) kết nối của người dùng tới cụm máy chủ CDN đặt tại Việt Nam hoặc Singapore gần đó nhất.
- Lợi ích: Giảm độ trễ cực lớn, tăng băng thông, giảm thiểu nguy cơ nghẽn cục bộ tại server gốc.

---
## TÓM TẮT NHỮNG ĐIỂM CHÍNH (KEY TAKEAWAYS)
- Tầng ứng dụng hoạt động thông qua socket, sử dụng IP và Port để giao tiếp.
- Các kiến trúc: Client-Server và P2P.
- HTTP là giao thức web (Port 80, TCP), Stateless. Có Non-persistent (tốn RTT cho mỗi file) và Persistent. Dùng Cookie để quản lý trạng thái, dùng Web Cache để tối ưu.
- Email sử dụng SMTP (để push - Port 25, TCP), POP3/IMAP (để pull/đọc).
- DNS phân giải tên miền sang IP, dùng UDP Port 53, cấu trúc phân cấp (Root, TLD, Authoritative).
- P2P (BitTorrent) tự mở rộng băng thông dựa trên việc các peer đóng vai trò cả client và server. Thuật toán Tit-for-tat.
- Video streaming dùng DASH qua HTTP và CDN để đưa nội dung đến vị trí địa lý gần người dùng nhất.

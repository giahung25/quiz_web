# CHƯƠNG 1: TRẮC NGHIỆM TỔNG QUAN VỀ MẠNG MÁY TÍNH VÀ INTERNET

**Câu 1:** Trong kiến trúc mạng Internet, thuật ngữ "End system" (hệ thống đầu cuối) đồng nghĩa với thuật ngữ nào sau đây?
A. Router (Bộ định tuyến)
B. Switch (Bộ chuyển mạch)
C. Host (Máy chủ/máy trạm)
D. Communication link (Đường truyền)
*Đáp án: C*
*Giải thích: Host là cách gọi khác của end system, ám chỉ các thiết bị đầu cuối như máy tính, điện thoại, máy chủ nằm ở rìa của mạng.*

**Câu 2:** Chức năng cốt lõi của giao thức (protocol) trong mạng máy tính là gì?
A. Điều khiển tốc độ quay của quạt làm mát trong bộ định tuyến.
B. Định nghĩa định dạng (format), thứ tự của các thông điệp được gửi/nhận và các hành động xử lý các thông điệp đó.
C. Mã hoá toàn bộ dữ liệu trước khi truyền đi để chống lại hacker.
D. Thay thế hoàn toàn phần cứng mạng bằng các đoạn mã lập trình phần mềm.
*Đáp án: B*
*Giải thích: Giao thức mạng đóng vai trò như ngôn ngữ giao tiếp, quy định cấu trúc và cách thức các thiết bị nói chuyện với nhau.*

**Câu 3:** Theo kiến trúc phân tầng Internet (TCP/IP), tầng nào chịu trách nhiệm tìm đường (định tuyến) cho gói tin từ trạm nguồn tới trạm đích thông qua mạng lưới các router trên toàn cầu?
A. Tầng Ứng dụng (Application Layer)
B. Tầng Giao vận (Transport Layer)
C. Tầng Mạng (Network Layer)
D. Tầng Liên kết (Link Layer)
*Đáp án: C*
*Giải thích: Tầng mạng (Network Layer) sử dụng các giao thức định tuyến và địa chỉ IP để chuyển datagram xuyên qua mạng lõi (routers).*

**Câu 4:** Trong các công nghệ mạng truy cập sau đây, công nghệ nào cung cấp đường truyền bằng sợi cáp quang trực tiếp tới tận nhà người dùng?
A. DSL (Digital Subscriber Line)
B. Cable (Hệ thống truyền hình cáp)
C. Ethernet LAN
D. FTTH (Fiber to the Home)
*Đáp án: D*
*Giải thích: FTTH (Fiber to the Home) là mạng cáp quang kéo trực tiếp đến hộ gia đình, cung cấp băng thông rất lớn so với cáp đồng hay cáp đồng trục.*

**Câu 5:** Kỹ thuật nào được thiết kế để dành riêng (reserve) toàn bộ tài nguyên trên tuyến đường từ nguồn đến đích trong suốt thời gian kết nối, giống như mạng điện thoại truyền thống?
A. Chuyển mạch gói (Packet Switching)
B. Chuyển mạch kênh (Circuit Switching)
C. Chuyển mạch thông điệp (Message Switching)
D. Lưu và chuyển tiếp (Store-and-forward)
*Đáp án: B*
*Giải thích: Circuit Switching dành riêng tài nguyên (băng thông) trong suốt phiên kết nối, đảm bảo tốc độ nhưng gây lãng phí nếu không có dữ liệu truyền.*

**Câu 6:** Internet ngày nay sử dụng phương pháp chuyển mạch nào làm nền tảng cốt lõi?
A. Chuyển mạch kênh bằng FDM
B. Chuyển mạch gói (Packet Switching)
C. Chuyển mạch kênh bằng TDM
D. Mạng điện thoại chuyển mạch công cộng (PSTN)
*Đáp án: B*
*Giải thích: Internet dựa trên Packet Switching, chia sẻ băng thông theo nhu cầu (statistical multiplexing), linh hoạt nhưng có thể xảy ra trễ hàng đợi.*

**Câu 7:** Một gói tin có kích thước L = 10,000 bits được đẩy vào một liên kết có tốc độ R = 10 Mbps. Bỏ qua các loại độ trễ khác, thời gian cần thiết để bộ định tuyến đẩy toàn bộ gói tin này lên đường dây (Transmission Delay) là bao nhiêu?
A. 1 ms (miligiây)
B. 10 ms
C. 0.1 ms
D. 100 ms
*Đáp án: A*
*Giải thích: Transmission Delay = L / R = 10,000 bits / 10,000,000 bps = 0.001 giây = 1 ms.*

**Câu 8:** Khoảng cách giữa hai thành phố là 2.000 km. Tốc độ lan truyền của tín hiệu trong cáp quang là $2*10^8$ m/s. Trễ lan truyền (Propagation Delay) giữa hai thành phố này là:
A. 10 ms
B. 1 ms
C. 100 ms
D. 20 ms
*Đáp án: A*
*Giải thích: Propagation Delay = Khoảng cách (d) / Tốc độ truyền (v) = 2,000,000 m / (2*10^8 m/s) = 0.01 giây = 10 ms.*

**Câu 9:** Hiện tượng mất gói tin (Packet Loss) xảy ra tại một router chủ yếu là do nguyên nhân nào?
A. Router bị mất điện đột ngột.
B. Cáp quang bị đứt do thi công.
C. Tốc độ gói tin tới cổng vào của router quá lớn, làm tràn bộ đệm hàng đợi (buffer overflow) khiến router phải loại bỏ các gói tin đến sau.
D. Gói tin có chứa mã độc (virus) nên bị router tiêu diệt.
*Đáp án: C*
*Giải thích: Khi hàng đợi đầy, router không còn chỗ lưu trữ tạm thời các gói tin mới tới, dẫn đến việc phải drop (loại bỏ) chúng.*

**Câu 10:** Quá trình một bộ định tuyến (router) nhận một gói tin ĐẦY ĐỦ từ cổng vào, sau đó mới tiến hành đẩy gói tin đó ra cổng đích được gọi là nguyên lý gì?
A. Phân mảnh gói tin
B. Lưu và chuyển tiếp (Store-and-Forward)
C. Định tuyến đa đường (Multipath routing)
D. Chuyển mạch tế bào (Cell switching)
*Đáp án: B*
*Giải thích: Hầu hết các packet switch sử dụng cơ chế lưu-và-chuyển-tiếp, tạo ra một độ trễ bằng L/R tại mỗi chặng.*

**Câu 11:** Trong mô hình TCP/IP, đơn vị dữ liệu (PDU) tại tầng Giao vận (Transport Layer) được gọi là gì?
A. Message (Bản tin)
B. Datagram (Gói tin)
C. Segment (Đoạn tin)
D. Frame (Khung)
*Đáp án: C*
*Giải thích: Đơn vị dữ liệu: Application -> Message, Transport -> Segment, Network -> Datagram, Link -> Frame.*

**Câu 12:** Lớp nào CÓ trong mô hình OSI 7 tầng nhưng KHÔNG được tách biệt rõ ràng trong mô hình TCP/IP 5 tầng?
A. Tầng Ứng dụng (Application)
B. Tầng Giao vận (Transport)
C. Tầng Phiên (Session) và Tầng Trình diễn (Presentation)
D. Tầng Mạng (Network)
*Đáp án: C*
*Giải thích: Trong TCP/IP, chức năng của tầng Session và Presentation được gộp chung vào tầng Application.*

**Câu 13:** Giao thức nào dưới đây KHÔNG hoạt động ở tầng Ứng dụng?
A. HTTP
B. SMTP
C. FTP
D. IP
*Đáp án: D*
*Giải thích: IP (Internet Protocol) là giao thức cốt lõi của tầng Mạng (Network Layer).*

**Câu 14:** Khi bạn tải một file có dung lượng F = 32 Megabits mất 8 giây. Thông lượng trung bình (Average Throughput) của quá trình tải file này là bao nhiêu?
A. 4 Megabytes/s
B. 4 Megabits/s (Mbps)
C. 8 Megabits/s
D. 256 Megabits/s
*Đáp án: B*
*Giải thích: Average Throughput = Kích thước file / Thời gian = 32 Mbits / 8 s = 4 Mbps.*

**Câu 15:** Trên tuyến đường từ Client tới Server có 3 đoạn mạng với tốc độ lần lượt là R1 = 10 Mbps, R2 = 5 Mbps, R3 = 100 Mbps. Thông lượng đầu cuối tới đầu cuối (end-to-end throughput) lớn nhất xấp xỉ bằng bao nhiêu?
A. 115 Mbps
B. 10 Mbps
C. 100 Mbps
D. 5 Mbps
*Đáp án: D*
*Giải thích: Throughput bị giới hạn bởi liên kết có băng thông thấp nhất trên tuyến đường (bottleneck link), ở đây là 5 Mbps.*

**Câu 16:** Hành động thay đổi trái phép địa chỉ IP nguồn trong Header của gói tin để giả mạo là một người dùng hợp pháp được gọi là gì?
A. Packet Sniffing (Nghe lén gói tin)
B. IP Spoofing (Giả mạo IP)
C. DoS (Từ chối dịch vụ)
D. Man in the middle (Người đứng giữa)
*Đáp án: B*
*Giải thích: Spoofing là hành vi mạo danh địa chỉ IP nguồn để đánh lừa hệ thống đích.*

**Câu 17:** Các mạng máy tính ma (Botnet) gồm hàng trăm ngàn máy bị nhiễm malware thường bị hacker huy động để thực hiện cuộc tấn công nào sau đây?
A. SQL Injection
B. Đánh cắp mật khẩu ngân hàng
C. DDoS (Từ chối dịch vụ phân tán)
D. Thay đổi giao diện website (Defacement)
*Đáp án: C*
*Giải thích: Hacker điều khiển botnet cùng lúc gửi hàng triệu gói tin rác về một máy chủ để làm quá tải băng thông và sập dịch vụ (DDoS).*

**Câu 18:** Kỹ thuật ghép kênh theo tần số (FDM) trong chuyển mạch kênh hoạt động như thế nào?
A. Chia thời gian thành các khe, mỗi kết nối dùng 1 khe.
B. Băng thông của liên kết cáp được chia thành nhiều dải tần số nhỏ, mỗi kết nối được sử dụng riêng một dải tần số trong suốt phiên kết nối.
C. Mọi kết nối cùng dùng chung toàn bộ băng thông và phát sinh va chạm.
D. Gửi gói tin ngẫu nhiên lên đường cáp.
*Đáp án: B*
*Giải thích: FDM (Frequency-Division Multiplexing) cắt dọc băng thông thành các làn đường song song, mỗi cuộc gọi chạy trên một làn riêng.*

**Câu 19:** Khi một máy tính đóng gói (encapsulate) một bản tin để gửi đi, thứ tự thêm các lớp Header từ trên xuống dưới (từ ứng dụng ra cáp vật lý) là:
A. Application -> Link -> Network -> Transport -> Physical
B. Application -> Transport -> Network -> Link -> Physical
C. Link -> Network -> Transport -> Application
D. Transport -> Application -> Network -> Link
*Đáp án: B*
*Giải thích: Dữ liệu đi từ tầng cao xuống tầng thấp: Ứng dụng tạo Message, Giao vận thêm header tạo Segment, Mạng thêm header tạo Datagram, Liên kết thêm header/trailer tạo Frame.*

**Câu 20:** Độ trễ xử lý nút (Nodal Processing Delay) tại một router bao gồm những công việc gì?
A. Chờ đợi ở hàng đợi cho đến khi đường cáp rảnh.
B. Thời gian đẩy tín hiệu điện từ lên cáp quang.
C. Kiểm tra lỗi bit (checksum) ở header và quyết định cổng đầu ra cho gói tin.
D. Thời gian tín hiệu ánh sáng truyền trong cáp.
*Đáp án: C*
*Giải thích: Trễ xử lý là thời gian CPU của router đọc header, kiểm tra lỗi và tra bảng định tuyến. Thời gian này thường rất nhỏ (cỡ microsecond).*

**Câu 21:** Giao thức nào ở tầng Liên kết (Data Link Layer) được sử dụng phổ biến nhất trong các mạng LAN có dây?
A. Wi-Fi (IEEE 802.11)
B. 4G LTE
C. Ethernet (IEEE 802.3)
D. PPP
*Đáp án: C*
*Giải thích: Ethernet là chuẩn công nghệ thống trị tuyệt đối trong các mạng LAN nội bộ có dây.*

**Câu 22:** Việc chuẩn hóa các giao thức Internet để đảm bảo mọi thiết bị trên thế giới có thể giao tiếp với nhau được thực hiện bởi tổ chức nào, và tài liệu chuẩn hóa đó gọi là gì?
A. Tổ chức IEEE, gọi là chuẩn 802.
B. Tổ chức IETF, gọi là tài liệu RFC (Request for Comments).
C. Tổ chức ISO, gọi là mô hình OSI.
D. Tổ chức W3C, gọi là HTML.
*Đáp án: B*
*Giải thích: IETF (Internet Engineering Task Force) là nơi thảo luận và phê duyệt các chuẩn Internet dưới dạng tài liệu RFC.*

**Câu 23:** Khái niệm "Rìa mạng" (Network Edge) bao gồm những thiết bị nào?
A. Các bộ định tuyến (Router) đường trục quốc gia.
B. Các cáp quang dưới đáy biển.
C. Các thiết bị đầu cuối (Host) như máy tính cá nhân, điện thoại di động, máy chủ Web.
D. Các trạm phát sóng vệ tinh.
*Đáp án: C*
*Giải thích: Rìa mạng là nơi người dùng và các ứng dụng trực tiếp tương tác, gồm các hệ thống đầu cuối (client và server).*

**Câu 24:** Một phần mềm gián điệp bí mật ghi lại thao tác bàn phím của người dùng để trộm mật khẩu được xếp vào nhóm nào?
A. DoS
B. Packet Sniffer
C. Malware (Mã độc) dạng Spyware.
D. Worm
*Đáp án: C*
*Giải thích: Spyware là một loại mã độc được cài lén lút vào máy nạn nhân để theo dõi hành vi.*

**Câu 25:** Đặc điểm nào sau đây mô tả đúng nhất về mạng Truyền hình cáp (Cable access network) dùng để truy cập Internet?
A. Là môi trường truyền thông chuyên biệt không chia sẻ.
B. Là môi trường truyền thông chia sẻ (Shared medium), nơi tất cả các hộ gia đình dùng chung một đường cáp sẽ cùng chia sẻ tổng băng thông tải xuống.
C. Tốc độ tải lên (Upload) luôn bằng hoặc lớn hơn tải xuống (Download).
D. Không thể truyền đồng thời tín hiệu tivi và tín hiệu Internet.
*Đáp án: B*
*Giải thích: Khác với FTTH nối cáp quang riêng đến tận nhà, cáp đồng trục truyền hình là một bus chung, các nhà trong khu phố cùng chia sẻ băng thông.*

**Câu 26:** Hai chức năng chính của Lõi mạng (Network Core) là gì?
A. Định tuyến (Routing) và Chuyển tiếp (Forwarding).
B. Mã hóa (Encryption) và Giải mã (Decryption).
C. Hiển thị trang web và nén tệp tin.
D. Phát sóng Wi-Fi và quản lý pin thiết bị di động.
*Đáp án: A*
*Giải thích: Routing giúp tìm đường trên toàn cục, Forwarding giúp đẩy gói tin qua thiết bị nội bộ.*

**Câu 27:** Mạng riêng của tổ chức (Intranet) khác Internet ở điểm nào?
A. Dùng các giao thức hoàn toàn khác biệt với TCP/IP.
B. Là mạng khép kín của một cơ quan/doanh nghiệp, bị giới hạn truy cập từ bên ngoài, nhưng vẫn dùng chung kiến trúc và giao thức như Internet.
C. Tốc độ luôn luôn cao hơn Internet.
D. Không cần dùng Router.
*Đáp án: B*
*Giải thích: Intranet bản chất là một mạng IP nội bộ, bị tường lửa cô lập với Internet công cộng để bảo mật.*

**Câu 28:** Đơn vị đo lường cơ bản của băng thông (Bandwidth) mạng máy tính là gì?
A. Byte (B)
B. bit trên giây (bps)
C. Hertz (Hz)
D. Frame trên giây (fps)
*Đáp án: B*
*Giải thích: Tốc độ truyền dẫn trên mạng đo bằng số lượng bit đẩy lên đường cáp trong 1 giây (bps, Kbps, Mbps, Gbps).*

**Câu 29:** Nếu trễ lan truyền (Propagation Delay) quá lớn (ví dụ truyền qua vệ tinh địa tĩnh), nó sẽ ảnh hưởng tiêu cực nhất đến loại ứng dụng nào?
A. Truyền nhận Email
B. Tải tệp tin (File Download)
C. Gọi thoại hoặc Video thời gian thực (VoIP/Video Call)
D. Đọc báo điện tử
*Đáp án: C*
*Giải thích: Độ trễ vài trăm miligiây của vệ tinh khiến giọng nói bị delay, gây gián đoạn và cực kỳ khó chịu khi đàm thoại trực tiếp.*

**Câu 30:** Thiết bị nào sau đây thường được triển khai Tường lửa (Firewall) để bảo vệ mạng cục bộ khỏi Internet?
A. Edge Router (Bộ định tuyến biên)
B. Laptop của khách hàng
C. Cáp đồng trục
D. Trạm phát sóng Wi-Fi (AP)
*Đáp án: A*
*Giải thích: Tường lửa thường được cài đặt ở cửa ngõ giao tiếp giữa LAN và Internet, tức là trên Edge Router.*

**Câu 31:** Để xác định được đường đi ngắn nhất hoặc tốt nhất cho gói tin, các Router thực thi điều gì?
A. Thuật toán kiểm tra lỗi CRC
B. Thuật toán định tuyến (Routing Protocols/Algorithms)
C. Các hàm băm mật mã MD5
D. Giao thức DHCP
*Đáp án: B*
*Giải thích: Routing protocols (như OSPF, BGP) chạy các thuật toán để tìm và cấu hình đường đi cho gói tin.*

**Câu 32:** Yếu tố nào sau đây quyết định kích thước của Cửa sổ tắc nghẽn (Congestion Window) nếu TCP nằm trong Mạng Truy cập Không dây? (Câu hỏi mở rộng khái niệm)
A. Trễ hàng đợi
B. Tín hiệu RTS/CTS
C. Cơ chế chống rớt mạng của ứng dụng
D. Các phản hồi ACK hoặc Timeout (Mất gói)
*Đáp án: D*
*Giải thích: Hiện tượng mất gói, gây ra do tắc nghẽn hoặc do nhiễu không dây, đều sẽ dẫn đến Timeout hoặc thiếu ACK, khiến TCP thu hẹp cửa sổ truyền.*

**Câu 33:** Ứng dụng P2P (Peer-to-Peer) khác ứng dụng Client-Server ở điểm cốt lõi nào?
A. P2P cần một máy chủ cực mạnh để điều phối.
B. P2P cho phép máy tính cá nhân tự cung cấp tài nguyên trực tiếp cho nhau thay vì dựa vào máy chủ trung tâm.
C. P2P chỉ chạy trên cáp quang.
D. P2P không thể truyền tệp lớn.
*Đáp án: B*
*Giải thích: Mọi máy (Peer) trong mạng ngang hàng vừa là Client vừa là Server.*

**Câu 34:** ISP Tier-1 (Nhà cung cấp dịch vụ Internet cấp 1) có đặc điểm gì?
A. Cung cấp mạng trực tiếp cho các hộ gia đình ở nông thôn.
B. Phải trả tiền để kết nối với mạng của người khác.
C. Có mạng lưới đường trục quang phủ sóng toàn cầu và kết nối ngang hàng (peering) với các ISP Tier-1 khác mà không phải trả phí trung chuyển.
D. Chỉ cung cấp dịch vụ mạng di động vô tuyến.
*Đáp án: C*
*Giải thích: Tier-1 là tầng cao nhất của cấu trúc Internet, họ kết nối miễn phí với nhau và thu phí từ các ISP cấp dưới (Tier-2, Access ISP).*

**Câu 35:** Tại sao Packet Switching lại được cho là hiệu quả hơn Circuit Switching trong việc sử dụng băng thông Internet?
A. Vì nó không chia nhỏ gói tin.
B. Do hiện tượng "Statistical Multiplexing" (Ghép kênh thống kê), cho phép nhiều người dùng tận dụng khoảng thời gian rảnh rỗi của đường truyền, thay vì cấp phát cứng tài nguyên như Circuit Switching.
C. Vì Packet Switching đảm bảo gói tin không bao giờ bị trễ.
D. Vì nó dùng được trên mạng điện thoại bàn.
*Đáp án: B*
*Giải thích: Do dữ liệu máy tính thường truyền theo đợt (bursty), khi máy này ngưng truyền thì máy khác lập tức dùng được phần băng thông đó.*

**Câu 36:** Để giảm thiểu độ trễ xử lý (Nodal Processing Delay), các Router lõi hiện đại thường áp dụng biện pháp gì?
A. Cài đặt hệ điều hành Windows Server.
B. Sử dụng hoàn toàn cấu trúc phần mềm (Software) để chạy linh hoạt.
C. Sử dụng các mạch tích hợp phần cứng chuyên dụng (Hardware/ASIC) để tăng tốc độ tra cứu và chuyển mạch.
D. Gộp tầng Mạng và tầng Giao vận lại với nhau.
*Đáp án: C*
*Giải thích: Bảng định tuyến được đẩy vào phần cứng phần cứng chuyên dụng để xử lý gói tin ở tốc độ nanosecond.*

**Câu 37:** Kẻ tấn công dùng phương pháp "Packet Sniffing" có thể làm được điều gì?
A. Giả mạo địa chỉ IP để vượt qua tường lửa.
B. Làm ngập lụt băng thông của mạng.
C. Nghe trộm và sao chép toàn bộ nội dung của các gói tin truyền không mã hóa qua mạng cục bộ (ví dụ mạng Wi-Fi công cộng).
D. Đưa máy tính vào botnet.
*Đáp án: C*
*Giải thích: Sniffer đọc lén dòng dữ liệu chạy qua đường cáp/sóng không trung để dò mật khẩu nếu người dùng không dùng HTTPS.*

**Câu 38:** Sự cố nào dưới đây KHÔNG do nguyên nhân tràn hàng đợi (buffer overflow) gây ra?
A. Gói tin bị vứt bỏ (Packet Loss).
B. Tăng trễ hàng đợi (Queuing Delay).
C. Trễ lan truyền (Propagation Delay) tăng lên đột biến.
D. Ứng dụng phía trên (như TCP) phải truyền lại dữ liệu.
*Đáp án: C*
*Giải thích: Propagation delay phụ thuộc cứng vào khoảng cách cáp và tốc độ ánh sáng, không phụ thuộc vào tình trạng kẹt xe của router.*

**Câu 39:** Đơn vị đo đạc tốc độ lan truyền tín hiệu (v) trong cáp quang hoặc cáp đồng xấp xỉ bằng bao nhiêu?
A. Tốc độ âm thanh (340 m/s)
B. Bằng tốc độ ánh sáng trong chân không (3 * 10^8 m/s)
C. Tốc độ ánh sáng trong môi trường chất rắn (khoảng 2 * 10^8 m/s)
D. 100 Mbps
*Đáp án: C*
*Giải thích: Ánh sáng truyền trong cáp quang hay điện truyền trong đồng chậm hơn một chút so với tốc độ ánh sáng chân không, khoảng 2/3.*

**Câu 40:** Mô hình OSI phân bổ chức năng chuyển định dạng dữ liệu (ví dụ mã hóa văn bản, nén ảnh) vào tầng nào?
A. Application
B. Presentation (Trình diễn)
C. Session
D. Transport
*Đáp án: B*
*Giải thích: Tầng Presentation (Tầng 6 của OSI) có chức năng trình bày dữ liệu cho ứng dụng (mã hóa, nén).*

**Câu 41:** Một liên kết mạng bị "Nút thắt cổ chai" (Bottleneck) khi nào?
A. Khi kích thước gói tin lớn hơn MTU.
B. Khi liên kết đó có băng thông nhỏ nhất trên toàn bộ con đường từ nguồn đến đích, khiến nó giới hạn thông lượng tối đa của toàn mạng.
C. Khi liên kết đó kết nối với một máy chủ hỏng.
D. Khi cáp mạng bị thắt nút vật lý.
*Đáp án: B*
*Giải thích: Giống như ống nước, chỗ nhỏ nhất quyết định lượng nước chảy qua tối đa.*

**Câu 42:** Đâu là đặc trưng của mạng truy cập Không dây diện rộng (Wide-area wireless access networks)?
A. Phạm vi phủ sóng nhỏ, chỉ vài chục mét (Wi-Fi).
B. Được cung cấp bởi công ty điện lực qua đường dây điện.
C. Phủ sóng bán kính rộng hàng chục km nhờ các trạm thu phát của nhà mạng di động viễn thông (ví dụ 3G, 4G, 5G).
D. Phải dùng cáp đồng trục để nối vào điện thoại.
*Đáp án: C*
*Giải thích: 4G/5G là mạng truy cập vô tuyến bao trùm diện rộng ngoài trời.*

**Câu 43:** Kỹ thuật FDM và TDM thường thuộc kiến trúc mạng nào?
A. Chuyển mạch gói mạng máy tính.
B. Chuyển mạch kênh mạng viễn thông.
C. Mạng cảm biến không dây.
D. Chuyển đổi mã hóa.
*Đáp án: B*
*Giải thích: FDM (chia tần số) và TDM (chia khe thời gian) là hai cách để cắt nhỏ tài nguyên vật lý cố định cho các cuộc gọi thoại.*

**Câu 44:** Worm khác Virus máy tính ở điểm nào?
A. Worm làm cháy ổ cứng, Virus chỉ làm chậm máy.
B. Virus cần có sự thao tác/tương tác của người dùng (như mở file đính kèm, chạy ứng dụng) để lây nhiễm. Worm có khả năng lợi dụng lỗ hổng mạng để tự động lây nhiễm sang máy khác mà không cần người dùng can thiệp.
C. Worm chỉ lây trên điện thoại, Virus lây trên máy tính.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: Sự nguy hiểm của Worm (như WannaCry) là nó tự rà quét mạng và nhân bản tự động vào máy nạn nhân qua các cổng dịch vụ hở.*

**Câu 45:** Khi bạn mở một trang web, một gói HTTP Request sẽ được chuyển dần xuống qua bao nhiêu tầng của giao thức TCP/IP trước khi truyền vào cáp?
A. 4 tầng (Transport, Network, Link, Physical)
B. 3 tầng (Network, Link, Physical)
C. 5 tầng (Application, Session, Transport, Network, Link)
D. Chạy thẳng qua tầng Vật lý.
*Đáp án: A*
*Giải thích: Gói HTTP nằm ở tầng Application, nó sẽ đi xuống 4 tầng còn lại: Giao vận -> Mạng -> Liên kết -> Vật lý.*

**Câu 46:** Các trung tâm dữ liệu (Datacenter) khổng lồ của Google thường xây dựng hệ thống mạng kết nối riêng (Private network) để làm gì?
A. Để thu phí mạng của người dùng.
B. Bỏ qua hoàn toàn các chuẩn TCP/IP để dùng chuẩn riêng nhanh hơn.
C. Tránh phải trả cước phí lưu lượng trung chuyển khổng lồ cho các ISP Tier-1 và tăng cường độ ổn định, kiểm soát khi kết nối toàn cầu.
D. Để hạn chế số người dùng tìm kiếm.
*Đáp án: C*
*Giải thích: Google/Microsoft tự rải cáp quang xuyên biển tạo Content Provider Network riêng, bypass hệ thống Internet công cộng ở nhiều quốc gia để tự quản lý lưu lượng.*

**Câu 47:** Gói tin ở Tầng Mạng (Network Layer) gọi là Datagram. Vậy Datagram bị bóc Header khi nó đi tới thiết bị mạng nào?
A. Link-layer Switch
B. Máy tính nguồn
C. Router (Bộ định tuyến)
D. Hub
*Đáp án: C*
*Giải thích: Router hoạt động đến Tầng 3. Nó lột lớp vỏ Link-layer Frame ra, đọc Header của Datagram Tầng 3, xử lý, rồi đóng vỏ Link-layer mới trước khi truyền đi.*

**Câu 48:** Băng thông (Bandwidth) khác với Thông lượng (Throughput) như thế nào?
A. Không khác biệt gì.
B. Băng thông là dung lượng đo được trên ổ cứng, Thông lượng đo trên cáp.
C. Băng thông là tốc độ truyền dữ liệu LÝ THUYẾT tối đa của đường truyền vật lý, trong khi Thông lượng là lượng dữ liệu THỰC TẾ truyền được ở một thời điểm, có tính đến nhiễu và chia sẻ mạng.
D. Thông lượng chỉ dành cho gói tin bị lỗi.
*Đáp án: C*
*Giải thích: Giống như đường cao tốc có 4 làn xe (Băng thông), nhưng vì kẹt xe nên tốc độ chạy thực tế chỉ đạt 20km/h (Thông lượng).*

**Câu 49:** Theo định nghĩa của IETF, tài liệu đặc tả chi tiết về cách hoạt động của một giao thức Internet như TCP hay HTTP được gọi là gì?
A. Giao diện (Interface)
B. Bằng sáng chế (Patent)
C. RFC (Request for Comments)
D. IEEE Document
*Đáp án: C*
*Giải thích: Các tài liệu chuẩn của tổ chức kỹ thuật Internet IETF được ban hành dưới cái tên truyền thống là RFC.*

**Câu 50:** Sự kết hợp giữa Giao thức (Protocol) và Phân tầng (Layering) mang lại lợi thế lớn nhất nào cho việc phát triển Internet?
A. Tăng tính phức tạp để ngăn hacker tìm hiểu.
B. Cố định hoàn toàn kiến trúc mạng, không bao giờ thay đổi.
C. Tính Module hóa. Các nhà phát triển ứng dụng (trên tầng Application) chỉ cần giao tiếp qua giao diện chuẩn mà không cần quan tâm đến việc ở dưới cáp quang hay sóng Wi-Fi (Physical Layer) truyền tín hiệu như thế nào.
D. Giảm số lượng thiết bị vật lý.
*Đáp án: C*
*Giải thích: Module hóa nhờ layering giúp công nghệ phần mềm và công nghệ vật liệu mạng (cáp quang, wifi) có thể phát triển độc lập mà vẫn tương thích với nhau qua TCP/IP.*

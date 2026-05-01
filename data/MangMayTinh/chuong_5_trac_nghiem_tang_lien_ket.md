# CHƯƠNG 5: TRẮC NGHIỆM TẦNG LIÊN KẾT (DATA LINK LAYER) VÀ LAN

**Câu 1:** Đơn vị dữ liệu (PDU) của Tầng Liên kết (Data Link Layer) được gọi là gì?
A. Datagram
B. Segment
C. Frame (Khung)
D. Message
*Đáp án: C*
*Giải thích: Đơn vị ở tầng Liên kết là Khung. Khung này chứa Payload là IP Datagram từ tầng Mạng chuyển xuống.*

**Câu 2:** Tầng Liên kết thường được thực thi và xử lý hoàn toàn bởi bộ phận cứng nào trên máy tính?
A. Ổ cứng HDD
B. Cạc mạng (Network Interface Card - NIC) hoặc Chipset mạng.
C. Bàn phím
D. Card đồ họa (VGA)
*Đáp án: B*
*Giải thích: Do tính chất tốc độ cực cao, việc đóng khung, tính toán mã lỗi CRC, dò tìm xung đột mạng được "đúc cứng" vào mạch chip của NIC thay vì chạy trên CPU phần mềm.*

**Câu 3:** Kỹ thuật phát hiện lỗi bằng "Mã kiểm tra chẵn lẻ hai chiều" (Two-dimensional parity) có tính năng ưu việt gì so với chẵn lẻ một chiều?
A. Tiết kiệm dung lượng gói tin hơn.
B. Không những phát hiện được có lỗi, mà còn chỉ ra tọa độ CHÍNH XÁC của 1 bit bị lỗi để phần cứng có thể tự động LẬT NGƯỢC bit đó (Tự Sửa Lỗi - FEC).
C. Có thể phát hiện và sửa được 100 bit lỗi liên tiếp.
D. Có khả năng mã hóa dữ liệu thành văn bản bí mật.
*Đáp án: B*
*Giải thích: Xếp bit thành ma trận (hàng ngang, cột dọc). Giao điểm của hàng báo lỗi và cột báo lỗi chính là vị trí của cái bit bị lật. Máy nhận tự sửa mà không cần báo gửi lại.*

**Câu 4:** Khi hệ thống tính toán mã CRC (Cyclic Redundancy Check) ở tầng Liên kết, dữ liệu được nhìn nhận dưới con mắt toán học như thế nào?
A. Một ma trận chữ số.
B. Một phương trình vi phân.
C. Một đa thức nhị phân (Binary Polynomial).
D. Một con số Hexadecimal.
*Đáp án: C*
*Giải thích: Các bit dữ liệu (vd: 1011) được coi là hệ số của đa thức (x^3 + x + 1). Gói tin chia cho đa thức sinh G, phần dư D là mã CRC.*

**Câu 5:** Hiện tượng "Xung đột" (Collision) trong một mạng cục bộ (LAN) mang ý nghĩa vật lý là gì?
A. Tường lửa chặn gói tin.
B. Router không biết đường đi.
C. Khi hai hay nhiều máy tính CÙNG phát tín hiệu năng lượng (sóng vô tuyến hoặc điện áp) vào CÙNG một môi trường truyền thông dùng chung (Shared medium), làm cho các tín hiệu điện từ hòa trộn, bóp méo và triệt tiêu nhau.
D. Khi máy tính cắm nhầm dây nguồn.
*Đáp án: C*
*Giải thích: Trong cáp đồng trục cũ hoặc sóng Wi-Fi, hai máy nói cùng lúc thì tín hiệu dội vào nhau thành đống nhiễu loạn.*

**Câu 6:** CSMA/CD (Carrier Sense Multiple Access with Collision Detection) là giao thức nổi tiếng giải quyết đa truy cập. Cụm từ "Collision Detection" đóng vai trò tiết kiệm băng thông như thế nào?
A. Tránh va chạm xảy ra.
B. Thiết bị trong khi đang phát sẽ dò mức điện áp của dây cáp. Nếu vọt lên, nó biết là có đụng độ. Nó HỦY ngay việc phát nốt các bit còn lại của khung (tránh phí thời gian) và báo tín hiệu nhiễu để mọi người đều ngưng.
C. Giới hạn số lượng máy tính kết nối vào LAN.
D. Xóa bộ nhớ đệm của Switch.
*Đáp án: B*
*Giải thích: Ethernet rất nhạy, đang nói mà thấy có tiếng hét của đứa khác là cúp miệng luôn, không bướng bỉnh nói đến cùng.*

**Câu 7:** Sau khi phát hiện đụng độ (Collision) bằng CSMA/CD, máy tính phải chờ bao lâu trước khi cố gắng thử gửi lại?
A. Chờ 1 giây.
B. Chờ 1 mili-giây.
C. Áp dụng thuật toán "Lùi lại ngẫu nhiên nhị phân" (Binary Exponential Backoff): Lấy ngẫu nhiên số lần trễ trong khoảng mốc rộng dần (từ 0 đến 2^n - 1) với n là số lần đụng độ liên tiếp.
D. Lập tức gửi lại không cần chờ.
*Đáp án: C*
*Giải thích: Đụng 1 lần, chờ từ {0, 1} slot. Đụng 2 lần, chờ từ {0, 1, 2, 3}. Đụng càng nhiều mạng càng nghẽn, thời gian chờ càng phải dàn đều để giảm nhiệt.*

**Câu 8:** Các giao thức như "Polling" (Hỏi dò vòng quanh từ Master) hoặc "Token Passing" (Truyền thẻ bài) thuộc nhóm giải pháp nào để ngăn ngừa va chạm mạng?
A. Nhóm Truy cập ngẫu nhiên (Random Access).
B. Nhóm Định tuyến động (Dynamic Routing).
C. Nhóm Luân phiên (Taking-Turns).
D. Nhóm Phân chia tần số (Frequency Partitioning).
*Đáp án: C*
*Giải thích: Nhóm này yêu cầu trật tự xếp hàng: Đến lượt mới được nói. Ưu điểm là không có va chạm, nhưng bị "Điểm yếu độc tôn": Rớt thẻ bài hoặc Master chết là hỏng toàn bộ mạng.*

**Câu 9:** Đặc trưng cốt lõi của một thiết bị Hub (Bộ tập trung) là gì?
A. Cực kỳ thông minh, hoạt động ở Tầng mạng.
B. Thiết bị ở Tầng Vật lý (Layer 1), nó nhận tín hiệu điện từ 1 cổng, sao chép tín hiệu đó và khuếch đại ném thẳng ra TẤT CẢ các cổng còn lại một cách hoàn toàn vô điều kiện.
C. Chỉ chuyển tiếp tín hiệu ra 1 cổng duy nhất.
D. Có bảng học địa chỉ IP.
*Đáp án: B*
*Giải thích: Hub là thiết bị "mù", làm việc thuần vật lý. Do tính khuếch đại bừa bãi nên nó biến toàn bộ mạng LAN thành một Môi trường xung đột (Collision Domain) khổng lồ.*

**Câu 10:** Khác với Hub, thiết bị Switch (Bộ chuyển mạch) thông minh hơn ở điểm nào?
A. Switch hoạt động ở Tầng Giao vận.
B. Switch đọc trường IP đích.
C. Switch hoạt động ở Tầng 2, biết đọc Địa chỉ MAC đích của Khung Ethernet, kiểm tra "Bảng địa chỉ MAC" của mình và chỉ ĐẨY KHUNG CÓ CHỌN LỌC ra ĐÚNG cổng nối với máy nhận.
D. Switch rẻ tiền hơn Hub rất nhiều.
*Đáp án: C*
*Giải thích: Switch chia rẽ các Miền Xung Đột (Collision Domain). Nếu A gửi cho B qua Switch, thì C cũng có thể gửi cho D ngay lúc đó mà không hề đụng độ với luồng A-B.*

**Câu 11:** Thiết bị Switch xây dựng "Bảng địa chỉ MAC" (Switch Table) bằng thuật toán Tự Học (Self-Learning) như thế nào?
A. Nhờ kỹ thuật viên nhập tay từng dòng lệnh.
B. Switch đọc trường ĐỊA CHỈ MAC NGUỒN của mọi khung tin khi nó vừa chui vào Cổng (Port) nào đó, và học lỏm ghi lại "À, máy có MAC này nằm ở nhánh Cổng này".
C. Bằng cách gửi gói tin BGP.
D. Switch kết nối lên Google để tải về.
*Đáp án: B*
*Giải thích: Switch là thiết bị cắm-và-chạy (Plug-and-play). Không cần ai dạy, nó tự nhìn trộm MAC nguồn để vẽ nên bản đồ các cổng nối với các máy.*

**Câu 12:** Khi Switch gặp một Khung có MAC Đích mà trong bảng học lỏm của nó CHƯA CÓ, nó phản ứng thế nào?
A. Vứt (Drop) gói tin đó ngay.
B. Báo lỗi về máy nguồn.
C. Lập tức biến thành Hub tạm thời: Flood (Phát tán) gói tin đó ra TẤT CẢ các cổng còn lại ngoại trừ cổng nó vừa nhận, để đảm bảo máy đích có nhận được.
D. Tự tạo ra một MAC ngẫu nhiên.
*Đáp án: C*
*Giải thích: Trạng thái mù đường. Khi máy đích nhận được và trả lời lại, lập tức Switch sẽ học được máy đích nằm ở cổng nào, lần sau sẽ không Flood nữa.*

**Câu 13:** ARP (Address Resolution Protocol) giải quyết nhiệm vụ gì trong mạng cục bộ?
A. Cấp phát IP tự động.
B. Dịch địa chỉ IP của một máy tính (đã biết trước) ra thành địa chỉ vật lý MAC tương ứng để có thể đóng khung Ethernet.
C. Chống xung đột cáp quang.
D. Giám sát băng thông video.
*Đáp án: B*
*Giải thích: Tầng 3 có IP, nhưng để đi ra cáp đồng của Tầng 2 phải có MAC. ARP là quyển sổ danh bạ tra cứu IP -> MAC trong cùng 1 LAN.*

**Câu 14:** Thông điệp truy vấn ARP (ARP Query) được phát đi dưới định dạng nào?
A. Unicast
B. Multicast
C. Broadcast (Gửi đến MAC đích FF:FF:FF:FF:FF:FF) tới tất cả các thiết bị trong mạng con (Subnet).
D. Anycast
*Đáp án: C*
*Giải thích: Vì không biết máy kia MAC gì nên phải la làng lên (Broadcast): "Ê, anh nào mang IP 192.168.1.100 khai báo MAC cho tôi với!". Chỉ máy nào đúng IP đó mới trả lời.*

**Câu 15:** Điều gì ngăn cách hai miền phát tán (Broadcast Domains) khác nhau?
A. Hub
B. Switch Tầng 2
C. Cáp đồng
D. Router (Bộ định tuyến)
*Đáp án: D*
*Giải thích: Tín hiệu ARP Broadcast chỉ lanh quanh trong LAN. Router khi nhận được gói Broadcast FF:FF:FF... nó sẽ chặn đứng lại (Drop), không bao giờ cho rò rỉ sang mạng LAN khác. Router chia cắt Broadcast domains.*

**Câu 16:** Địa chỉ MAC khác với địa chỉ IP ở cấu trúc hình thức như thế nào?
A. MAC không thay đổi, IP có thay đổi.
B. MAC dài 128 bit, IP dài 32 bit.
C. Địa chỉ MAC dài 48 bit (6 bytes) và thường được viết theo định dạng Thập lục phân (Hexadecimal), ví dụ: 00:1A:2B:3C:4D:5E.
D. IP ghi cứng vào phần cứng, MAC cấu hình bằng phần mềm.
*Đáp án: C*
*Giải thích: Kích thước 48 bit cho phép tạo ra khoảng 281 nghìn tỷ MAC duy nhất do nhà sản xuất (như Intel, Broadcom) gán chết vào card mạng (burned in ROM).*

**Câu 17:** Payload (Dữ liệu chở kèm) TỐI THIỂU của một khung Ethernet chuẩn (ví dụ mang IP Datagram) là bao nhiêu byte?
A. 0 byte
B. 20 bytes
C. 46 bytes (Nếu ít hơn, phải thêm các bit đệm - Padding).
D. 1500 bytes.
*Đáp án: C*
*Giải thích: Thiết kế của Ethernet chuẩn hóa kích thước gói tin tối thiểu để sóng đụng độ CSMA/CD có đủ thời gian quay về máy phát. Do đó payload bèo nhất phải 46 byte. Nhỏ quá thì chèn thêm dữ liệu rác.*

**Câu 18:** Công nghệ VLAN (Virtual LAN) trên Switch cho phép quản trị viên làm được việc gì?
A. Gộp 10 Switch lại thành 1 siêu Switch.
B. Dùng một Switch phần cứng (Physical Switch) duy nhất để phân chia logic thành NHIỀU mạng LAN nhỏ, tách biệt hoàn toàn các miền Broadcast và tăng tính bảo mật nội bộ.
C. Biến mạng dây thành mạng Wi-Fi.
D. Bỏ qua hoàn toàn địa chỉ MAC.
*Đáp án: B*
*Giải thích: VLAN giúp cắm phòng Kế toán và phòng Kỹ thuật chung 1 cái Switch 24 port nhưng Kỹ thuật không thể ping được Kế toán (trừ khi dùng Router) và Broadcast của Kế toán không bay sang phòng Kỹ thuật.*

**Câu 19:** Khái niệm "Trunk Port" trong mô hình có VLAN dùng để làm gì?
A. Cắm trực tiếp vào máy tính giám đốc.
B. Chỉ định cổng phát Wi-Fi.
C. Nối đường truyền cáp DUY NHẤT kết nối hai Switch VLAN với nhau, mang trên nó các khung thuộc ĐA DẠNG nhiều VLAN khác nhau bằng cách gán thêm thẻ định danh 802.1Q (VLAN Tag).
D. Dùng để cấu hình IP cho Router.
*Đáp án: C*
*Giải thích: Nếu không có Trunk, bạn phải cắm 1 sợi dây riêng cho VLAN Kế toán, 1 sợi cho Kỹ thuật giữa 2 Switch. Trunk port dồn hết vào 1 sợi dây, thêm cái thẻ 4-byte VLAN ID vào Frame để đầu kia bóc ra phân loại.*

**Câu 20:** Nếu máy tính của bạn ở Hà Nội gửi gói tin đến một máy tính ở New York, địa chỉ MAC đích của khung Ethernet khởi hành từ máy bạn là gì?
A. Địa chỉ MAC của máy New York.
B. Địa chỉ MAC của cáp quang biển.
C. Địa chỉ MAC của chính máy tính bạn.
D. Địa chỉ MAC của Cổng vào (Interface) trên Default Gateway Router nhà bạn.
*Đáp án: D*
*Giải thích: Rất quan trọng! Địa chỉ MAC KHÔNG ĐI XA ĐƯỢC. Khung Ethernet chỉ đi đến trạm trung chuyển (Router nhà bạn). Máy bạn sẽ dùng ARP hỏi MAC của Router và gửi khung cho Router. Sau đó Router xé khung, định tuyến IP, đóng Khung mới và nhắm tới Router tiếp theo.*


**Câu 21:** Trong một miền đụng độ (Collision Domain) sử dụng CSMA/CD, khi số lượng máy tính muốn truyền dữ liệu cùng lúc tăng lên rất nhiều, hiện tượng gì sẽ xảy ra đối với băng thông thực tế (Throughput) khả dụng?
A. Throughput không thay đổi vì băng thông được chia đều.
B. Throughput tăng lên do có nhiều máy tham gia.
C. Throughput giảm sút nghiêm trọng do phần lớn thời gian đường truyền bị lãng phí cho các vụ đụng độ (Collisions) và khoảng thời gian lùi lại ngẫu nhiên chờ đợi (Backoff).
D. Giao thức chuyển sang dùng Token Passing tự động.
*Đáp án: C*
*Giải thích: Hiệu suất (Efficiency) của CSMA/CD đi xuống khi mạng tải quá cao vì va chạm xảy ra liên tục, máy tính chỉ mải miết chờ lùi lại mà không truyền được dữ liệu hữu ích.*

**Câu 22:** Công thức để tính số trạm (host) tối thiểu cần cung cấp mã MAC là:
A. Mọi trạm đều dùng IP, không cần MAC.
B. MAC chỉ có trên Router.
C. Mỗi bộ chuyển đổi mạng (Network Adapter/Interface) gắn vào thiết bị đều phải có một địa chỉ MAC duy nhất toàn cầu.
D. Mọi trạm trong cùng LAN có chung 1 MAC.
*Đáp án: C*
*Giải thích: Laptop của bạn có 1 MAC cho cổng dây LAN (Ethernet NIC), và 1 MAC hoàn toàn khác cho cạc không dây (Wi-Fi NIC).*

**Câu 23:** Cấu trúc khung Ethernet chuẩn của IEEE 802.3 chứa một trường gọi là "Preamble" (Tiền tố) dài 8 byte ở đầu khung. Mục đích của Preamble là gì?
A. Để chứa địa chỉ IP Nguồn.
B. Đánh thức phần cứng máy nhận, đồng bộ hóa nhịp đồng hồ (clock synchronization) giữa máy phát và máy thu bằng chuỗi bit 10101010 trước khi đổ dữ liệu thực sự vào.
C. Kiểm tra lỗi phần cứng.
D. Báo hiệu cho các máy khác im lặng.
*Đáp án: B*
*Giải thích: Do không có đồng hồ chung, máy thu cần một đoạn nhạc dạo đầu (101010...) nhịp nhàng để khóa khớp tốc độ bắt bit của nó với tốc độ bit của máy phát.*

**Câu 24:** Một giao thức MAC theo phương pháp "Channel Partitioning" (Phân chia kênh) như TDM (Time Division) có ưu điểm và nhược điểm nào rõ nét nhất?
A. Ưu: Rất phức tạp. Nhược: Xung đột liên tục.
B. Ưu: Tận dụng 100% băng thông khi chỉ có 1 người dùng. Nhược: Chia không công bằng.
C. Ưu: Chia sẻ hoàn toàn công bằng và KHÔNG bao giờ có va chạm. Nhược: Lãng phí vô ích khi mạng ít người tải (VD có 10 khe nhưng 9 người im lặng, 1 người có nhiều data vẫn chỉ được dùng 1/10 băng thông).
D. Ưu: Truyền song song IP và MAC. Nhược: Bị Hacker dễ tấn công.
*Đáp án: C*
*Giải thích: Phân chia kênh (TDMA, FDMA) cứng ngắc giống như chia làn đường cố định. Làn xe buýt trống rỗng nhưng xe con vẫn kẹt, không được lấn làn.*

**Câu 25:** Vì sao ngày nay trong mạng nội bộ (LAN) của các doanh nghiệp, hiện tượng đụng độ (Collision) dường như KHÔNG còn tồn tại?
A. Vì họ dùng giao thức IP bản mới.
B. Vì tất cả doanh nghiệp đều dùng cấu trúc mạng sao (Star topology) xoay quanh các thiết bị Hub truyền thống.
C. Vì doanh nghiệp sử dụng toàn bộ cáp quang.
D. Vì họ triển khai các bộ chuyển mạch Switch hoạt động ở chế độ Full-Duplex (Song công toàn phần), mỗi nút mạng có sợi truyền và sợi nhận riêng biệt tới cổng Switch, cách ly hoàn toàn Collision Domain.
*Đáp án: D*
*Giải thích: Switched Ethernet với Full-duplex khiến card mạng vừa truyền vừa nhận cùng lúc mà không chạm sóng, loại bỏ vĩnh viễn CSMA/CD khỏi cuộc sống thực tế.*

**Câu 26:** Mối tương quan giữa ARP Table và Switch Table (MAC Table) là gì?
A. Chúng là một. Cả hai đều ánh xạ IP sang MAC.
B. Switch Table chứa cấu hình IP của nhà mạng.
C. ARP Table nằm trong Máy tính cá nhân / Router dùng để ánh xạ (IP -> MAC). Switch Table nằm trong Switch dùng để ánh xạ (MAC -> Cổng vật lý số mấy).
D. Chạy ở Tầng Giao vận.
*Đáp án: C*
*Giải thích: Máy tính cần ARP để biết ghi MAC Đích là gì vào Frame. Switch nhận được Frame đó cần Switch Table để biết xuất cái Frame đó ra lỗ nào.*

**Câu 27:** Mạng Token Ring sử dụng cơ chế nào để giải quyết vấn đề đa truy cập?
A. Lắng nghe sóng mạng (Carrier Sense).
B. Tự động tránh va chạm.
C. Có một Master dò quanh các máy.
D. Truyền tay một "thẻ bài" (Token) luân phiên. Máy nào nắm thẻ bài mới có quyền bơm khung dữ liệu lên vòng cáp.
*Đáp án: D*
*Giải thích: Kiến trúc Taking-turns (luân phiên) bằng thẻ bài ngăn đụng độ tuyệt đối, nhưng nếu máy cầm thẻ bị sập nguồn làm mất thẻ thì mạng "chết lâm sàng".*

**Câu 28:** Mạng Ethernet chuẩn 1000BASE-T sử dụng loại cáp truyền thông nào?
A. Cáp quang đa mốt.
B. Cáp đồng trục.
C. Cáp đồng đôi xoắn (Twisted-pair copper wire) tốc độ 1 Gigabit/giây.
D. Sóng vô tuyến.
*Đáp án: C*
*Giải thích: "T" ám chỉ Twisted-pair. 1000 chỉ 1000 Mbps = 1 Gbps.*

**Câu 29:** Nếu một thiết bị đang thực hiện CSMA/CD và đụng độ lần thứ 3 liên tiếp, khoảng lùi thời gian ngẫu nhiên (Backoff) của nó sẽ được rút từ tập số nào?
A. {0, 1, 2, 3}
B. {0, 1, 2, 3, 4, 5, 6, 7}
C. {0, 1, ..., 15}
D. Cố định 3 giây.
*Đáp án: B*
*Giải thích: Công thức là rút ngẫu nhiên K từ {0, 1, ..., 2^n - 1}. Với n = 3, $2^3 - 1 = 7$. Vậy tập là {0..7}.*

**Câu 30:** Khi Máy A khởi động và có IP tĩnh, nhưng nó không biết IP đó có bị máy nào khác trong LAN đang dùng trùng hay không. Nó dùng cơ chế ARP đặc biệt nào để dò tìm sự trùng lặp (Duplicate IP)?
A. Proxy ARP.
B. Gratuitous ARP (Gửi ARP Request truy vấn chính địa chỉ IP của bản thân mình).
C. Reverse ARP (RARP).
D. Gửi email lên máy chủ.
*Đáp án: B*
*Giải thích: Gratuitous ARP la lên "Ai dùng IP 192.168.1.10 thì lên tiếng". Vì nó chính là thằng 10, nếu không ai lên tiếng nghĩa là IP chưa bị trùng.*

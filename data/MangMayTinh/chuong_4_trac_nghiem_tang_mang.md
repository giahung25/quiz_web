# CHƯƠNG 4: TRẮC NGHIỆM TẦNG MẠNG (NETWORK LAYER)

**Câu 1:** Trong khái niệm mạng hiện đại, Data Plane (Mặt phẳng Dữ liệu) chịu trách nhiệm cho chức năng cơ bản nào của Router?
A. Định tuyến (Routing) tính toán toàn bộ bản đồ.
B. Chuyển tiếp gói tin (Forwarding) cục bộ từ cổng vào sang cổng ra của chính bộ định tuyến đó.
C. Cấp phát địa chỉ IP cho máy chủ.
D. Mã hóa luồng truyền thông.
*Đáp án: B*
*Giải thích: Data plane chỉ làm công việc "cơ bắp": nhặt gói tin ở ngõ vào, nhìn IP đích, tra Forwarding table và đẩy ra ngõ ra tương ứng (diễn ra trong vài nanosecond).*

**Câu 2:** Tầng Mạng (Network Layer) sử dụng đơn vị dữ liệu (PDU) được gọi là gì?
A. Segment
B. Frame
C. Datagram (Gói tin)
D. Message
*Đáp án: C*
*Giải thích: Tại Tầng mạng, Segment từ trên chuyển xuống được đóng gói IP Header tạo thành Datagram.*

**Câu 3:** Theo kiến trúc truyền thống, Bảng chuyển tiếp (Forwarding Table) của một Router được xây dựng từ đâu?
A. Do người dùng tự lập trình bằng tay.
B. Router ngẫu nhiên đoán đường.
C. Từ việc bộ định tuyến chạy các thuật toán định tuyến (Routing Algorithms) trong Mặt phẳng điều khiển (Control Plane).
D. Do nhà mạng gọi điện báo.
*Đáp án: C*
*Giải thích: Data Plane và Control Plane dù nằm chung trong con Router truyền thống, nhưng quá trình Control plane chạy các thuật toán (như OSPF, BGP) mới tính ra được bảng Forwarding table.*

**Câu 4:** Kiến trúc SDN (Software-Defined Networking) tách rời bộ phận nào ra khỏi Router vật lý?
A. Tách Data Plane ra khỏi Router, đặt trên mây.
B. Tách Control Plane (Não bộ định tuyến) ra khỏi Router vật lý và đem nó gộp lên các Máy chủ Điều khiển (Remote Controller) trung tâm bằng phần mềm.
C. Tách ăng ten thu phát Wi-Fi.
D. Tách RAM của Router.
*Đáp án: B*
*Giải thích: Trong SDN, Router trở thành các thiết bị đơn giản "dumb switches", chỉ biết tuân lệnh (OpenFlow) đẩy gói tin, còn phần thuật toán khổng lồ nằm ở Server tập trung.*

**Câu 5:** Thông số TTL (Time To Live) trong Header của IPv4 có công dụng lớn nhất là gì?
A. Chỉ định ngày giờ sản xuất gói tin.
B. Chống sự tồn tại lặp đi lặp lại vô hạn (Routing Loops) của một Datagram trên mạng do lỗi định tuyến sai bằng cách trừ 1 giá trị mỗi khi đi qua một Router.
C. Cảnh báo quá tải RAM cho máy chủ.
D. Tăng thời gian lưu trữ ở Router.
*Đáp án: B*
*Giải thích: Giả sử Router A định tuyến đến Router B, B lại bị lỗi chỉ ngược lại A. Gói tin sẽ chạy A-B-A-B mãi mãi. TTL = 64, mỗi lần qua router trừ 1, đến 0 thì gói tin bị tiêu diệt, trả lại băng thông cho Internet.*

**Câu 6:** Địa chỉ IPv4 có tổng độ dài bao nhiêu bits?
A. 16 bits
B. 32 bits
C. 64 bits
D. 128 bits
*Đáp án: B*
*Giải thích: IPv4 có 32 bit, thể hiện dưới dạng 4 con số từ 0-255 cách nhau bởi dấu chấm (ví dụ 192.168.1.1).*

**Câu 7:** Một mạng cục bộ có ký hiệu địa chỉ là `192.168.10.0/24`. Nếu mạng này không dùng Subnet nào khác, có tối đa bao nhiêu địa chỉ IP khả dụng có thể gán cho các thiết bị (Hosts)?
A. 256
B. 255
C. 254
D. 24
*Đáp án: C*
*Giải thích: Mạng /24 có 8 bit phần Host (32-24=8). Tổng IP là 2^8 = 256. Bỏ địa chỉ đầu (Network Address 192.168.10.0) và địa chỉ cuối (Broadcast 192.168.10.255), còn 254 IP khả dụng.*

**Câu 8:** Bạn vừa cắm cáp mạng vào máy tính mới. Máy tính sẽ dùng giao thức Tầng Ứng dụng nào để xin tự động một địa chỉ IP nội bộ, Subnet mask, Default Gateway từ mạng đó?
A. NAT
B. ARP
C. DHCP (Dynamic Host Configuration Protocol)
D. ICMP
*Đáp án: C*
*Giải thích: DHCP là giao thức cấp phát địa chỉ IP động cho mạng nội bộ hoạt động theo nguyên tắc DORA (Discover, Offer, Request, ACK).*

**Câu 9:** Chức năng NAT (Network Address Translation) giải quyết khủng hoảng thiếu địa chỉ IPv4 toàn cầu thông qua cách nào?
A. Tự động chuyển đổi máy tính dùng IPv4 sang IPv6.
B. Nén nội dung gói tin lại.
C. Cho phép toàn bộ mạng LAN nội bộ phía sau Router (dùng Private IP 192.168.x.x) ẩn đi, chỉ đại diện duy nhất bởi 1 IP Public của Router khi giao tiếp với Internet. Router ánh xạ các máy nội bộ này bằng Số hiệu Cổng (Port).
D. Chặn các quảng cáo để giảm lưu lượng.
*Đáp án: C*
*Giải thích: Nhờ NAT, hàng triệu nhà mạng, công ty chỉ cần tốn 1 vài IP Public, còn hàng tỷ thiết bị bên trong dùng IP Private không đụng hàng với ai ngoài Internet.*

**Câu 10:** Quá trình "IP Fragmentation" (Phân mảnh IP) diễn ra khi nào?
A. Khi gói tin muốn mã hóa làm nhiều mảnh.
B. Khi kích thước Datagram quá lớn, vượt qua mức giới hạn truyền tải tối đa (MTU) của liên kết phía trước, bắt buộc Router phải băm Datagram gốc thành nhiều phần nhỏ hơn.
C. Khi đường cáp bị đứt làm đứt gói tin.
D. Khi tín hiệu Wi-Fi yếu đi.
*Đáp án: B*
*Giải thích: Ethernet thường có MTU = 1500 bytes. Nếu Datagram 4000 bytes lao tới, Router phải dùng cờ Fragmentation Offset băm nhỏ Datagram ra mới đẩy lọt đường ống đó.*

**Câu 11:** Trong quy trình Phân mảnh IP (IP Fragmentation), các mảnh vỡ của gói tin sẽ được ráp nối lại (Reassembly) nguyên vẹn tại đâu?
A. Tại Router trạm kế tiếp.
B. Tại Mọi Router trên đường dẫn.
C. Tại Thiết bị nhận cuối cùng (Destination Host).
D. Tại Switch.
*Đáp án: C*
*Giải thích: Để các Router lõi hoạt động cực nhanh, nhà thiết kế mạng đẩy gánh nặng ráp mảnh vỡ (Reassembly) về phía thiết bị nhận (End-system) cuối cùng, dựa theo ID của gói tin.*

**Câu 12:** So với IPv4, giao thức IPv6 có thay đổi mang tính cách mạng nào dưới đây?
A. IPv6 hỗ trợ phân mảnh ở Router linh hoạt hơn IPv4.
B. Địa chỉ IP mở rộng từ 32 bit lên 128 bit, Header cố định 40 byte và LOẠI BỎ hoàn toàn trường Header Checksum lẫn việc Phân mảnh ở Router nhằm tăng tốc độ xử lý.
C. IPv6 không dùng được cho các thiết bị di động.
D. IPv6 ghép MAC và IP làm một.
*Đáp án: B*
*Giải thích: IPv6 tối giản để xử lý siêu tốc, không cần Checksum (do Tầng 2, 4 làm rồi). Cấm phân mảnh: Gói quá to thì drop, gửi lỗi ICMP về bắt thằng gửi tự chia nhỏ.*

**Câu 13:** "Đường hầm" (Tunneling) là một chiến lược phổ biến trong mạng tầng 3 để giải quyết vấn đề gì?
A. Cho phép kết nối 2 thiết bị không dùng chung dải IP.
B. Truyền gói tin IPv6 vượt qua các khu vực toàn là Router thế hệ cũ chỉ hiểu IPv4 bằng cách đóng gói nguyên con Datagram IPv6 nhét vào trong Payload của Datagram IPv4.
C. Mã hóa kết nối TCP cục bộ.
D. Bảo vệ đường cáp vật lý.
*Đáp án: B*
*Giải thích: Tunneling lừa các router IPv4 cũ bằng cách ngụy trang IPv6 thành tải trọng (Payload) mang bởi xe tải IPv4.*

**Câu 14:** Giao thức định tuyến nội vùng (Intra-AS) "OSPF" sử dụng dạng thuật toán định tuyến nào làm nền tảng?
A. Distance Vector (Ví dụ: phương trình Bellman-Ford).
B. Link State (Trạng thái liên kết - Sử dụng thuật toán tìm đường ngắn nhất Dijkstra trên biểu đồ có sẵn).
C. BGP Policy Routing.
D. K-Nearest Neighbor.
*Đáp án: B*
*Giải thích: OSPF bắt mọi Router phát tán bản tin Broadcast toàn mạng (LSA). Cuối cùng, mọi Router nắm trong tay bản đồ chi tiết của toàn mạng rồi tự chạy thuật toán Dijkstra để vẽ đường ngắn nhất.*

**Câu 15:** Trái ngược với Link State, thuật toán định tuyến Distance Vector (như RIP) có đặc điểm gì?
A. Router phải tải toàn bộ bản đồ Internet.
B. Router không có tầm nhìn toàn cục. Nó chỉ biết thông tin từ các router láng giềng kề sát vách, chia sẻ qua lại các bảng ước tính khoảng cách, và dùng phương trình quy hoạch động Bellman-Ford để cập nhật đường đi.
C. Có tốc độ chạy nhanh hơn Dijkstra hàng trăm lần.
D. Tuyệt đối không bao giờ bị lỗi lặp vòng định tuyến (Routing loop).
*Đáp án: B*
*Giải thích: Distance Vector giống như việc hỏi đường người dân dọc đường, không ai có bản đồ cả nhưng truyền miệng nhau sẽ tính ra khoảng cách. Tuy nhiên nó dễ bị hiện tượng "Tin dữ truyền chậm" (Count to infinity).*

**Câu 16:** Hiện tượng "Đếm đến vô cực" (Count-to-infinity) trong mạng máy tính là gì?
A. Vòng lặp đếm địa chỉ MAC không dừng.
B. Là lỗi của thuật toán Link State khi dùng thuật toán Dijkstra sai lệch trọng số.
C. Lỗi kinh điển của thuật toán Distance Vector, khi một liên kết bị đứt (chi phí tăng vọt), các router lân cận trao đổi các ước lượng sai lạc vòng quanh nhau, khiến khoảng cách đường đi tăng từ từ đến vô cực.
D. Bộ nhớ của router đếm số IP hết giới hạn.
*Đáp án: C*
*Giải thích: Khi cáp đứt, A không báo "Đường hỏng rồi", B tưởng đường cũ qua A vẫn ngon, A lại tưởng B còn đường khác. Cả hai cứ cộng dồn chi phí mãi.*

**Câu 17:** Giao thức nào là "Chất keo dính" duy nhất định tuyến các mạng liên vùng (Inter-AS Routing), kết nối các mạng của các ISP trên toàn thế giới với nhau?
A. OSPF
B. RIP
C. BGP (Border Gateway Protocol)
D. SDN
*Đáp án: C*
*Giải thích: BGP chịu trách nhiệm định tuyến giữa Hệ thống tự trị Viettel với Hệ thống tự trị AT&T Mỹ, quy mô toàn cầu.*

**Câu 18:** Khác với OSPF chỉ quan tâm đến tốc độ/chi phí đường truyền, giao thức BGP định tuyến dựa trên yếu tố trọng yếu nào?
A. Chiều dài cáp quang là duy nhất.
B. Khoảng cách địa lý vật lý (GPS).
C. Các chính sách về mặt chính trị và kinh tế (Policy Routing), ví dụ: AS không muốn làm phương tiện trung chuyển miễn phí cho AS đối thủ.
D. Thuật toán Dijkstra.
*Đáp án: C*
*Giải thích: BGP mang bản chất của kinh doanh. Đường ngắn nhất chưa chắc được chọn nếu đi đường đó tốn nhiều tiền cước thuê nhà mạng đối thủ.*

**Câu 19:** Các bản ghi quảng bá (BGP Advertisements) truyền thông điệp cốt lõi gì cho các Router BGP khác?
A. Báo hiệu bị tấn công DDoS.
B. Chia sẻ băng thông cục bộ.
C. "Reachability" (Khả năng tiếp cận): Tôi có thể dẫn gói tin đi đến Dải mạng Subnet X thông qua danh sách các AS-PATH này.
D. Truyền lại khóa mật mã.
*Đáp án: C*
*Giải thích: BGP quảng bá tuyến đường: "Đường tới mạng của Đại học Bách Khoa có thể đi qua tôi (AS1) rồi đến AS2, AS3".*

**Câu 20:** Khi một Router BGP biên (Gateway) học được đường đi tới một mạng ngoài từ BGP, nó dùng giao thức nội bộ nào để thông báo cho các Router bên TRONG tổ chức của nó biết lối ra?
A. eBGP (External BGP)
B. iBGP (Internal BGP)
C. SNMP
D. ICMP
*Đáp án: B*
*Giải thích: Sau khi Router biên đứng ngoài cổng nhận tin từ eBGP, nó rải tin đó cho anh em trong nhà thông qua các session iBGP.*

**Câu 21:** Ping và Traceroute là hai công cụ chuẩn đoán mạng vô cùng phổ biến. Cả hai hoạt động dựa trên cơ chế của giao thức nào?
A. ARP
B. TCP
C. UDP
D. ICMP (Internet Control Message Protocol)
*Đáp án: D*
*Giải thích: ICMP là "công cụ gỡ rối" của IP. Ping gửi các gói Echo Request để chờ ICMP Echo Reply báo mạng đang sống.*

**Câu 22:** Công cụ Traceroute thực hiện vẽ bản đồ đường đi của gói tin tới đích bằng một "mẹo" thông minh nào?
A. Dùng GPS của máy gửi.
B. Cố tình gửi các gói tin có giá trị TTL (Time-To-Live) lần lượt tăng dần: 1, 2, 3... Khi mỗi gói tin chết ở một Router nào đó, Router đó sẽ gửi thông điệp báo lỗi ICMP (Time Exceeded) về, nhờ vậy lộ diện địa chỉ IP của Router đó.
C. Mã hóa toàn bộ đường truyền.
D. Yêu cầu từng Router chụp ảnh cấu hình gửi về.
*Đáp án: B*
*Giải thích: Lần đầu gửi TTL=1, tới trạm đầu tiên chết, trạm báo về. Lần 2 gửi TTL=2, tới trạm 2 chết, trạm 2 báo về. Cứ thế, Traceroute lần ra toàn bộ các chặng.*

**Câu 23:** Sự phân biệt rõ nhất giữa eNodeB (Mạng 4G) và Router BGP (Internet Core) là gì?
A. Cả hai đều thuộc về Control Plane.
B. BGP là mạng có dây, eNodeB là không dây.
C. eNodeB quản lý Mạng Truyền dẫn Vô tuyến, cung cấp truy cập vật lý cho thiết bị di động, còn BGP định tuyến logic cho toàn bộ gói tin đi trên lõi cáp quang toàn cầu.
D. Không có khác biệt vì chúng dùng chung một dải băng tần.
*Đáp án: C*
*Giải thích: Vị trí của eNodeB là ở Access Network (Rìa), trong khi BGP cấu trúc mạng Network Core (Lõi).*

**Câu 24:** Nếu Data Plane được thực thi bằng phần cứng tốc độ rất cao (như FPGA/ASIC), thì Control Plane trong các Router truyền thống được chạy ở đâu?
A. Trong dây cáp mạng.
B. Bằng phần mềm trên bộ vi xử lý (CPU) đa dụng tích hợp bên trong bộ định tuyến đó, tốc độ có thể chậm hơn phần cứng.
C. Trên máy chủ Google.
D. Không cần thiết phải có.
*Đáp án: B*
*Giải thích: Control plane yêu cầu giải các bài toán quy hoạch động, thuật toán đồ thị rất phức tạp. Nó cần CPU chạy hệ điều hành (như Cisco IOS) thay vì phần cứng cứng.*

**Câu 25:** Vì sao NAT lại bị coi là vi phạm nghiêm trọng tính kiến trúc phân tầng gốc của Internet?
A. Vì nó gây ô nhiễm sóng vô tuyến.
B. Vì router (thiết bị Tầng 3 - Tầng Mạng) lại xâm phạm vào việc lấy thông tin và thay đổi cả Số hiệu Cổng (Port Number - vốn thuộc độc quyền Tầng 4 - Tầng Giao Vận) của gói tin.
C. Vì nó quá đắt tiền.
D. Vì không dùng được IPv6.
*Đáp án: B*
*Giải thích: Nguyên lý thiết kế ban đầu là Tầng nào xử lý Tầng đó. Router chỉ được bóc tới lớp IP, cấm sờ vào Port của TCP/UDP. Nhưng NAT vì lý do sinh tồn phải sửa Port.*

**Câu 26:** Mạng nào dưới đây thuộc địa chỉ Private IP do IANA quy định, không thể định tuyến tự do ngoài Internet toàn cầu?
A. 8.8.8.8
B. 10.0.0.0/8
C. 142.250.0.0/16
D. 210.245.0.0/24
*Đáp án: B*
*Giải thích: Các dải IP Private thông dụng gồm 10.0.0.0/8, 172.16.0.0/12, và 192.168.0.0/16. Chúng được dùng ở mạng LAN đằng sau cục NAT router.*

**Câu 27:** Các thiết bị phần cứng thực thi Tường lửa Lọc gói tin (Packet Filter Firewall) cần can thiệp kiểm tra đến tầng nào trong mô hình mạng?
A. Chỉ kiểm tra tầng vật lý (Physical).
B. Kiểm tra tầng Liên kết (Data Link).
C. Kiểm tra tầng Mạng (Network) và tầng Giao vận (Transport) để xem xét các quy tắc IP Nguồn/Đích và Cổng Nguồn/Đích.
D. Kiểm tra sâu vào tầng Ứng dụng (Application).
*Đáp án: C*
*Giải thích: Tường lửa lọc thông thường phải bóc đến lớp IP (Tầng 3) và TCP/UDP (Tầng 4) để thực thi nguyên tắc Allow/Drop (VD: Cấm IP 10.0.0.5 truy cập Port 80).*

**Câu 28:** Trong Bảng Định Tuyến OSPF, "Cost" (Chi phí) của một liên kết thường được quản trị viên đặt tỷ lệ nghịch với thông số nào?
A. Độ dài vật lý của cáp.
B. Tốc độ/Băng thông của liên kết đó.
C. Địa chỉ IP của cáp.
D. Phiên bản của hệ điều hành.
*Đáp án: B*
*Giải thích: Liên kết có băng thông càng cao (như cáp quang 10Gbps) thì chi phí (Cost) càng thấp, OSPF sẽ ưu tiên chọn những liên kết này làm đường đi.*

**Câu 29:** Điều gì làm cho IPv6 không hoàn toàn tương thích ngược với IPv4, dẫn đến quá trình chuyển đổi gian nan?
A. IPv6 viết địa chỉ bằng chữ cái.
B. Độ dài Header của IPv6 (40 bytes cố định) và cấu trúc các trường hoàn toàn khác với Header của IPv4 (20 bytes biến đổi). Router IPv4 thuần túy nhìn gói IPv6 sẽ không hiểu gì.
C. IPv6 không hoạt động trên cáp quang.
D. IPv6 yêu cầu dùng trình duyệt mới.
*Đáp án: B*
*Giải thích: Sự thay đổi cốt lõi trong phần móng của giao thức khiến các thiết bị phần cứng cũ bị mù màu khi gặp IPv6, phải dùng đường hầm (Tunneling).*

**Câu 30:** Một Router OSPF trong tổ chức bỗng nhiên bị hỏng dây mạng. Nó sẽ xử lý theo cơ chế gì?
A. OSPF tự động sửa dây.
B. Không làm gì, để mặc gói tin thất lạc.
C. Gửi bản tin trạng thái liên kết (Link State Update) phát tán Broadcast tới toàn bộ mạng nội bộ, báo tin xấu để các Router khác cập nhật lại cơ sở dữ liệu và chạy lại thuật toán Dijkstra tìm đường tránh khúc hỏng.
D. Tự động chuyển sang BGP.
*Đáp án: C*
*Giải thích: OSPF rất nhạy cảm với thay đổi cấu trúc mạng lưới (topology). Bản tin báo cáo sẽ làm mạng hội tụ (converge) lại đường đi mới khá nhanh.*

# CHƯƠNG 4: TẦNG MẠNG (NETWORK LAYER) - DATA PLANE VÀ CONTROL PLANE

Tầng mạng (Network Layer) là tầng phức tạp nhất trong toàn bộ mô hình TCP/IP vì nó liên quan đến TẤT CẢ các thiết bị đầu cuối và TẤT CẢ các bộ định tuyến (router) tạo nên mạng lưới toàn cầu Internet.
Chức năng duy nhất và quan trọng nhất của tầng mạng là: **Chuyển các gói tin (Datagram) từ host gửi (sender) đến host nhận (receiver)**.

Để làm được điều đó, mạng lưới chia các chức năng của router thành 2 mặt phẳng hoàn toàn tách biệt: Data Plane và Control Plane.

---

## 4.1 Data Plane (Mặt phẳng Dữ liệu) và Chức năng Forwarding

Data Plane (Mặt phẳng dữ liệu) phụ trách xử lý công việc "địa phương" ngay bên trong mỗi router đơn lẻ. Chức năng chính của nó là **Forwarding (Chuyển tiếp)**.
- **Forwarding:** Là hành động vật lý khi một router lấy gói tin từ cổng đầu vào (input link) và đẩy gói tin đó sang cổng đầu ra (output link) thích hợp. Nó diễn ra trong khoảng thời gian siêu ngắn (nanoseconds) và thường được thực thi cứng bằng phần cứng (Hardware).
- Khi gói tin tới, router sẽ trích xuất một phần thông tin trong header (chẳng hạn như địa chỉ IP đích). Sau đó router tra cứu trong **Bảng chuyển tiếp (Forwarding Table)** để tìm cổng đầu ra tương ứng.

### 4.1.1 Kiến trúc bên trong của Router
Router gồm 4 thành phần chính:
1. **Input Ports (Cổng đầu vào):** Thực hiện kết thúc liên kết vật lý (physical layer), xử lý liên kết dữ liệu (link layer), và tra cứu (lookup) xem gói tin phải chuyển ra cổng nào dựa vào Forwarding table. Nếu gói tin đến quá nhanh, cổng vào sẽ đưa gói tin vào hàng đợi (Input Queue).
2. **Switching Fabric (Mạng chuyển mạch lõi):** Trái tim của router. Nó là hệ thống kết nối vật lý nối tất cả cổng đầu vào với tất cả cổng đầu ra. Có 3 kiểu Switching Fabric: Chuyển mạch qua Memory (bộ nhớ), qua Bus (đường truyền chung), qua Crossbar (ma trận).
3. **Output Ports (Cổng đầu ra):** Nhận các gói tin từ switching fabric, đưa vào hàng đợi nếu cần, xử lý liên kết dữ liệu và đẩy tín hiệu ra vật lý.
4. **Routing Processor (Bộ xử lý định tuyến):** Bộ脑 thực hiện chức năng Control Plane, tính toán các thuật toán định tuyến, cấu hình Forwarding Table cho các cổng.

### 4.1.2 Đóng gói ở tầng Mạng (IP Datagram)
Giao thức cốt lõi của Data Plane Internet là **IPv4 (Internet Protocol version 4)** và **IPv6**.
Đơn vị dữ liệu của tầng mạng gọi là Datagram.

**Cấu trúc IPv4 Datagram Header (Cơ bản 20 bytes):**
- **Version (4 bits):** Phiên bản IP (IPv4 hay IPv6).
- **Header Length (4 bits):** Độ dài header.
- **TOS - Type of Service (8 bits):** Mức độ ưu tiên.
- **Datagram Length (16 bits):** Tổng độ dài của header và payload (Tối đa 65,535 bytes).
- **Identifier, Flags, Fragmentation Offset (32 bits):** Các trường dùng cho phân mảnh (Fragmentation) các gói tin quá lớn.
- **TTL - Time-To-Live (8 bits):** Chỉ số "Sống sót". Mỗi khi gói tin đi qua một router, TTL giảm đi 1. Nếu TTL = 0, router sẽ tiêu diệt gói tin để tránh trường hợp gói tin lặp vòng lặp (routing loop) vĩnh viễn trên mạng.
- **Protocol (8 bits):** Xác định giao thức tầng Giao vận ở payload là gì (TCP = 6, UDP = 17).
- **Header Checksum (16 bits):** Kiểm tra lỗi cho Header IP.
- **Source IP Address (32 bits):** Địa chỉ nguồn.
- **Destination IP Address (32 bits):** Địa chỉ đích (Rất quan trọng cho Forwarding).

### 4.1.3 Phân mảnh IP (IP Fragmentation)
Mỗi liên kết mạng tầng dưới (VD: Ethernet) có một quy định về kích thước khung lớn nhất được phép gọi là MTU (Maximum Transmission Unit). Thông thường MTU là 1500 bytes.
Nếu IP Datagram có kích thước 4000 bytes, Router bắt buộc phải băm nó ra thành 3 mảnh (fragments) nhỏ hơn để chui lọt qua MTU. Quá trình chia nhỏ này gọi là Phân mảnh.
- Đáng chú ý: Quá trình Rắp ráp (Reassembly) các mảnh này lại thành Datagram nguyên vẹn KHÔNG diễn ra ở các Router tiếp theo, mà chỉ được thực hiện tại Host nhận cuối cùng (Destination).

---

## 4.2 Địa chỉ IPv4 (IPv4 Addressing)

Mọi host và router giao diện mạng (interface) phải có địa chỉ IP để tham gia Internet. Địa chỉ IPv4 dài **32 bits** (thường viết dưới dạng 4 số thập phân cách nhau bởi dấu chấm, ví dụ: `192.168.1.1`).

### 4.2.1 Subnet (Mạng con) và Mặt nạ mạng (Subnet Mask)
Mạng Internet không nhìn IP như một số ngẫu nhiên. Nó chia IP làm 2 phần: **Subnet part** (Phần định danh mạng) và **Host part** (Phần định danh máy trong mạng).
Để biết đâu là phần Subnet, người ta dùng Subnet Mask.
Theo quy chuẩn **CIDR (Classless Inter-Domain Routing)**, IP được viết dưới dạng `a.b.c.d/x`, trong đó `x` là số bit làm tiền tố mạng (network prefix).
- Ví dụ: `192.168.1.0/24` nghĩa là 24 bit đầu tiên là địa chỉ Subnet.
- Mọi thiết bị gắn vào chung một bộ chuyển mạch (LAN) mà không đi qua router thì phải nằm trong chung 1 Subnet.

### 4.2.2 DHCP (Dynamic Host Configuration Protocol)
Làm sao một máy tính mới nối cáp vào mạng lại có địa chỉ IP? Có thể cài tĩnh (Manual), hoặc cấp phát động bằng DHCP.
DHCP là giao thức ứng dụng (dùng UDP) thực hiện theo 4 bước (DORA):
1. **D**iscover: Host gửi gói tin broadcast "Ai là DHCP server?".
2. **O**ffer: DHCP Server trả lời "Tôi đây, bạn dùng IP này nhé".
3. **R**equest: Host gửi "Ok, tôi xin lấy IP đó".
4. **A**CK: Server xác nhận "IP đó giờ là của bạn, xài trong 24h nhé".
DHCP cung cấp không chỉ IP, mà còn cung cấp Subnet mask, IP của Router mặc định (Default Gateway) và địa chỉ DNS server.

### 4.2.3 NAT (Network Address Translation)
Cạn kiệt địa chỉ IPv4 là một vấn đề lớn (chỉ có khoảng 4 tỷ địa chỉ). NAT là giải pháp tạm thời cứu sống Internet.
Một mạng gia đình dùng NAT, cục router được cấp đúng 1 địa chỉ IP Public cho toàn bộ nhà giao tiếp với Internet. Nhưng bên trong nhà, Router dùng DHCP phát cho các máy tính các địa chỉ IP Private cục bộ (ví dụ: `10.0.0.0/8`, `192.168.x.x`).
- Khi một gói tin từ máy cục bộ đi ra ngoài, Router sẽ thay thế IP Nguồn (Private IP) và Port Nguồn thành IP Public của nó và một Port Nguồn do nó tự sinh ra. Nó lưu lại bảng dịch này (NAT Translation Table).
- Khi có gói tin phản hồi về mang địa chỉ IP Public và Port đó, Router dò bảng NAT và tự động dịch ngược lại đẩy về đúng máy cục bộ.
NAT bị lên án vì vi phạm quy tắc "Network layer không đụng vào Port của Transport layer", phá vỡ tính end-to-end. Tuy nhiên nó rất phổ biến.

### 4.2.4 IPv6
Để thay thế IPv4, IPv6 ra đời với không gian địa chỉ khổng lồ **128 bits**.
- Header IPv6 được tối giản, cố định độ dài là 40 bytes.
- Không có trường Checksum ở IPv6 để tăng tốc độ xử lý router.
- IPv6 KHÔNG cho phép router phân mảnh gói tin trên đường truyền. Nếu quá lớn, router drop gói và báo lỗi ICMP để máy gửi tự chia nhỏ.

Sự chuyển đổi IPv4 lên IPv6 quá chậm. Giải pháp phổ biến để tương thích là **Tunneling (Đường hầm)**: Gói tin IPv6 được đóng gói, nhét vào bên trong phần payload của gói tin IPv4 để đi qua những router chỉ hiểu IPv4.

---

## 4.3 Control Plane (Mặt phẳng Điều khiển) và Routing

Mặt phẳng điều khiển (Control Plane) là bộ não của mạng lưới. Chức năng chính của nó là **Routing (Định tuyến)**.
- **Routing:** Xác định ĐƯỜNG ĐI TOÀN CỤC (path) cho các gói tin từ nguồn tới đích đi qua mạng lưới các bộ định tuyến. Thuật toán định tuyến tính toán và từ đó đổ cấu hình xuống bảng chuyển tiếp (Forwarding table) của từng router ở mặt phẳng dữ liệu.

Có 2 cách tiếp cận cấu trúc Control Plane:
1. **Theo hướng truyền thống (Per-router control):** Mỗi router đều có một bộ não điều khiển chạy chung một thuật toán định tuyến để tự cấu hình forwarding table cho chính mình (như OSPF, BGP).
2. **Theo hướng SDN (Software-Defined Networking):** Tách não (Control Plane) ra khỏi cơ bắp (Router). Bảng chuyển tiếp được tính toán tại một hệ thống Máy chủ điều khiển từ xa (Remote Controller). Router chỉ việc nhận bảng này về và làm nhiệm vụ đẩy gói tin.

### 4.3.1 Các Thuật toán Định tuyến (Routing Algorithms)
Mạng lưới router được biểu diễn như một đồ thị Graph G = (N, E), với N là nút, E là cạnh (chi phí). Thuật toán tìm đường đi ngắn nhất giữa nguồn và đích.
Có 2 nhóm thuật toán chính:
**1. Thuật toán Trạng thái Liên kết (Link State - LS):**
- *Kiến thức toàn cục:* Router phải có toàn bộ cấu trúc mạng lưới, biết chi phí của tất cả các liên kết bằng cách phát tán thông điệp quảng bá cho tất cả các nút (Link State Broadcast).
- Chạy thuật toán **Dijkstra** trên cơ sở dữ liệu đó để tính đường đi ngắn nhất.
- Giao thức thực tế: **OSPF (Open Shortest Path First)**.

**2. Thuật toán Vector Khoảng cách (Distance Vector - DV):**
- *Kiến thức cục bộ:* Router không biết toàn bộ mạng. Nó chỉ biết chi phí kết nối tới người láng giềng kề cận nó, và nhận bảng thông tin từ người láng giềng đó.
- Sử dụng phương trình **Bellman-Ford**: Khoảng cách ngắn nhất từ x đến y = min (chi phí từ x tới v + khoảng cách ngắn nhất từ v tới y).
- Giao thức thực tế: **RIP, BGP**.
- Nhược điểm: Phản ứng chậm khi liên kết bị đứt, dễ bị lỗi "Đếm đến vô cùng" (Count-to-infinity).

### 4.3.2 Định tuyến nội vùng (Intra-AS) và Định tuyến liên vùng (Inter-AS)
Internet quá lớn, không thể để mọi router biết mọi đường đi (bảng định tuyến sẽ tốn hàng Terabytes và việc tìm kiếm cực lâu). Mạng Internet được phân chia thành các Hệ thống tự trị (Autonomous Systems - AS), mỗi AS do một tổ chức/ISP (như Viettel) quản lý.

1. **Intra-AS Routing (Định tuyến nội vùng):**
- Là việc tìm đường đi giữa các router nằm TRONG CÙNG MỘT AS. Người quản trị mạng toàn quyền quyết định thuật toán.
- Giao thức tiêu biểu là **OSPF** (Link State) và **RIP** (Distance Vector).

2. **Inter-AS Routing (Định tuyến liên vùng):**
- Là việc tìm đường đi cho một gói tin đi GIỮA CÁC AS (VD: Gói tin từ mạng FPT sang mạng của AT&T ở Mỹ).
- Giao thức DUY NHẤT kết dính Internet toàn cầu là **BGP (Border Gateway Protocol)**.
- BGP không hoàn toàn tìm đường đi ngắn nhất, mà nó định tuyến dựa trên **CHÍNH SÁCH (Policy)** và kinh tế. AS quyết định sẽ định tuyến gói tin theo đường nào đem lại lợi nhuận, hoặc chặn không cho lưu lượng của kẻ thù mượn đường cáp của mình.
- BGP quảng bá khả năng tiếp cận (Reachability) của các Subnet. Một BGP router thông báo "Tôi có thể đi đến mạng `192.168.0.0/16` thông qua đường đi (AS-PATH) gồm các AS 1, AS 4, AS 7".

---
## TÓM TẮT (KEY TAKEAWAYS)
- Network layer: Data Plane (Forwarding - cục bộ ở router, chuyển từ input ra output) và Control Plane (Routing - tìm đường toàn cục).
- IPv4 (32 bit), IPv6 (128 bit). Cấu trúc packet (Datagram).
- Chức năng trường TTL: Diệt gói lặp vòng. Checksum: Bắt lỗi.
- NAT che giấu toàn bộ IP Private, chia sẻ 1 IP Public bằng cách sửa Port.
- DHCP cấp IP động, Subnet Mask chia mạng con.
- Thuật toán định tuyến: Link State (Biết toàn cục mạng, Dijkstra, OSPF) và Distance Vector (Chỉ giao tiếp láng giềng, Bellman-Ford, BGP).
- BGP kết nối các AS bằng định tuyến theo chính sách. OSPF định tuyến theo chi phí trong một AS.

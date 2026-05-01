# CHƯƠNG 1: TỔNG QUAN VỀ MẠNG MÁY TÍNH VÀ INTERNET

## 1.1 Khái quát về Internet và Mạng máy tính

### 1.1.1 Internet là gì?
Internet là mạng lưới khổng lồ kết nối hàng tỷ thiết bị điện toán trên toàn cầu. Các thiết bị này không chỉ giới hạn ở máy tính để bàn (desktop) hay máy tính xách tay (laptop), mà còn bao gồm điện thoại thông minh (smartphone), tivi thông minh, máy chủ web (web server), các cảm biến IoT (Internet of Things) và cả ô tô tự lái. Trong thuật ngữ chuyên ngành mạng, tất cả các thiết bị kết nối vào mạng này được gọi chung là **host** (máy chủ/máy trạm) hoặc **end system** (hệ thống đầu cuối).

Các end system kết nối với nhau thông qua mạng lưới các **communication link** (đường truyền truyền thông) và **packet switch** (bộ chuyển mạch gói).
- **Communication link**: Được làm từ nhiều loại phương tiện vật lý khác nhau, chẳng hạn như cáp đồng trục (coaxial cable), cáp đồng bện (copper wire), cáp quang (optical fiber) và phổ vô tuyến (radio spectrum). Mỗi loại đường truyền có một tốc độ truyền tải dữ liệu nhất định, được đo bằng bit/giây (bits per second - bps), gọi là **transmission rate** hoặc **bandwidth** (băng thông).
- **Packet switch**: Khi một hệ thống đầu cuối gửi dữ liệu đến một hệ thống đầu cuối khác, thiết bị gửi phân chia dữ liệu thành các đoạn nhỏ và thêm header (phần tiêu đề) vào mỗi đoạn. Các gói dữ liệu này được gọi là **packet** (gói tin). Packet switch nhận các gói tin trên một trong các đường truyền đầu vào và chuyển tiếp chúng ra một trong các đường truyền đầu ra. Hai loại packet switch nổi bật nhất trong mạng Internet ngày nay là **router** (bộ định tuyến) và **link-layer switch** (bộ chuyển mạch tầng liên kết). Switch thường được sử dụng trong các mạng truy cập (access network), trong khi router thường được sử dụng ở lõi mạng (network core).

Đường dẫn mà một gói tin đi từ hệ thống nguồn đến hệ thống đích thông qua chuỗi các đường truyền và packet switch được gọi là **route** (tuyến đường) hoặc **path** (đường đi).

Internet, về cơ bản, là mạng lưới của các mạng (network of networks). Các end system truy cập vào Internet thông qua các **Internet Service Provider (ISP)** (Nhà cung cấp dịch vụ Internet). Các ISP cung cấp quyền truy cập mạng lưới cho các hộ gia đình (ví dụ: VNPT, Viettel, FPT), cung cấp truy cập mạng di động, và truy cập mạng cho doanh nghiệp/trường học. Bản thân các ISP cũng phải kết nối với nhau để cho phép người dùng ở bất kỳ ISP nào cũng có thể tương tác với người dùng ở ISP khác. Do đó, mạng lưới ISP là một cấu trúc phân cấp, bao gồm các ISP cấp dưới (như ISP khu vực) và các ISP cấp trên (ISP quốc gia/quốc tế hay còn gọi là Tier-1 ISP).

### 1.1.2 Giao thức (Protocol) là gì?
Trong mạng máy tính, các end system, packet switch và mọi mảnh ghép của Internet đều hoạt động dưới sự điều khiển của các **protocol** (giao thức). Giao thức kiểm soát việc gửi và nhận thông tin bên trong mạng lưới.

Một định nghĩa dễ hiểu về giao thức trong thế giới thực là các quy tắc ứng xử của con người. Ví dụ, khi bạn hỏi giờ một người, bạn tuân theo quy tắc: gửi lời chào, sau đó hỏi giờ. Người kia sẽ đáp lại bằng câu trả lời thời gian hiện tại. Tương tự, giao thức mạng định nghĩa định dạng (format), thứ tự (order) của các thông điệp được gửi và nhận giữa các thực thể trên mạng, cũng như các hành động được thực hiện (actions taken) khi truyền/nhận các thông điệp đó.

Một số giao thức nổi tiếng như: TCP (Transmission Control Protocol), IP (Internet Protocol), HTTP (HyperText Transfer Protocol), Ethernet, Wi-Fi (802.11). Trong đó, IP là giao thức đóng vai trò vô cùng quan trọng vì nó xác định định dạng của các gói tin được định tuyến qua mạng Internet từ nguồn tới đích. Kết hợp lại, TCP và IP là các giao thức cốt lõi nhất của Internet, dẫn đến việc kiến trúc của Internet được gọi chung là kiến trúc TCP/IP.

Để đảm bảo tính tương thích và khả năng làm việc cùng nhau của mọi thiết bị và phần mềm từ các nhà sản xuất khác nhau, các giao thức được chuẩn hóa bởi tổ chức IETF (Internet Engineering Task Force). Các tài liệu chuẩn của IETF được gọi là RFC (Request for Comments).

---

## 1.2 Rìa mạng (The Network Edge)

Hệ thống mạng được phân chia thành rìa mạng và lõi mạng. Rìa mạng bao gồm các thiết bị đầu cuối (end systems / hosts). Các host thường được chia thành 2 loại: **client** (máy khách) và **server** (máy chủ).
- Client: Là những thiết bị như PC, điện thoại di động yêu cầu và tiếp nhận dịch vụ từ các thiết bị khác.
- Server: Thường là những máy tính mạnh mẽ lưu trữ và phân phối tài nguyên (Web page, Video, Email) phục vụ yêu cầu từ client. Hầu hết các server ngày nay nằm trong các data center (trung tâm dữ liệu) khổng lồ của Google, Amazon, Microsoft,...

### 1.2.1 Mạng truy cập (Access Networks)
Mạng truy cập là mạng vật lý kết nối end system vào edge router (bộ định tuyến biên) – router đầu tiên trên con đường từ hệ thống đầu cuối nguồn đi đến hệ thống đầu cuối đích.

**1. Mạng truy cập hộ gia đình (Home Access):**
- **DSL (Digital Subscriber Line):** Truy cập băng thông rộng qua đường dây điện thoại bằng đồng. ISP cấp dịch vụ Internet cũng chính là công ty cung cấp dịch vụ điện thoại nội hạt. DSL sử dụng kỹ thuật ghép kênh phân chia tần số (Frequency Division Multiplexing - FDM) để truyền đồng thời dữ liệu mạng, âm thanh điện thoại. DSL có đặc điểm bất đối xứng (asymmetric), tốc độ tải xuống (download) thường cao hơn tốc độ tải lên (upload).
- **Cable (Mạng cáp):** Tận dụng hệ thống truyền hình cáp. Thay vì dây đồng đôi xoắn, cáp đồng trục và sợi quang được sử dụng. Đặc trưng của cable là chia sẻ môi trường truyền thông (shared medium) – tất cả các hộ gia đình dùng chung một đường cáp sẽ cùng chia sẻ băng thông.
- **FTTH (Fiber to the Home):** Kéo trực tiếp sợi cáp quang từ văn phòng trung tâm của ISP đến nhà người dùng. Cung cấp tốc độ cực cao. Kỹ thuật chia sẻ tín hiệu quang phổ biến là PON (Passive Optical Network) và AON (Active Optical Network). Hiện nay mạng truy cập ở Việt Nam hầu hết sử dụng công nghệ FTTH.

**2. Mạng truy cập doanh nghiệp (Enterprise Access):**
Doanh nghiệp và trường học thường sử dụng Local Area Network (LAN) để kết nối máy tính của người dùng tới edge router. Công nghệ LAN phổ biến nhất là Ethernet, hoạt động dựa trên môi trường dây đồng bện hoặc cáp quang với tốc độ 100 Mbps, 1 Gbps, 10 Gbps và thậm chí cao hơn.

**3. Mạng truy cập không dây (Wireless Access Networks):**
- **Wireless LAN (WLAN):** Mạng không dây cục bộ hoạt động trong một phạm vi nhỏ (như nhà riêng, văn phòng, quán cà phê). Phổ biến nhất là Wi-Fi (chuẩn IEEE 802.11).
- **Wide-area wireless access networks:** Mạng di động diện rộng được cung cấp bởi các nhà mạng viễn thông (telcos) và trải dài trên hàng chục kilomet (ví dụ 3G, 4G LTE, 5G).

### 1.2.2 Phương tiện vật lý (Physical Media)
Bit dữ liệu được truyền từ nguồn đến đích bằng cách lan truyền qua các phương tiện vật lý. Các phương tiện này được chia làm hai loại:
- **Guided media (Phương tiện hữu tuyến/dẫn hướng):** Sóng tín hiệu truyền dọc theo một môi trường vật lý rắn, ví dụ như dây đồng bện (twisted-pair copper wire), cáp đồng trục (coaxial cable), sợi cáp quang (fiber optics).
  - Cáp quang: Mang ánh sáng xung, mỗi xung là một bit. Cáp quang có khả năng miễn nhiễm với nhiễu điện từ, tín hiệu ít bị suy hao với cự ly xa, mang lại tốc độ có thể lên tới Tbps.
- **Unguided media (Phương tiện vô tuyến/không dẫn hướng):** Sóng điện từ truyền lan trong không gian tự do. Ví dụ: Radio mặt đất, Radio vệ tinh (Geostationary satellites và Low-earth orbiting - LEO satellites như Starlink). Môi trường vô tuyến gặp phải các thách thức về sự phản xạ, che khuất vật lý, và nhiễu sóng (interference).

---

## 1.3 Lõi mạng (The Network Core)

Lõi mạng là mảng lưới các bộ định tuyến (router) và liên kết (link) dùng để kết nối những rìa mạng của Internet lại với nhau. Câu hỏi mấu chốt là làm sao dữ liệu đi xuyên qua hệ thống mạng lõi đồ sộ này? Có hai phương pháp chuyển mạch cốt lõi là **Packet Switching** (Chuyển mạch gói) và **Circuit Switching** (Chuyển mạch kênh).

### 1.3.1 Packet Switching (Chuyển mạch gói)
Trong các ứng dụng mạng, end systems trao đổi các bản tin (message). Để gửi một bản tin, thiết bị nguồn cắt bản tin đó ra thành các khối nhỏ hơn gọi là packet (gói tin). Giữa điểm nguồn và đích, gói tin được đi qua nhiều liên kết truyền thông (communication link) và packet switch (thường là router). Gói tin sẽ được truyền với tốc độ tối đa của liên kết vật lý (link transmission rate).

**Store-and-Forward Transmission (Lưu và chuyển tiếp):**
Hầu hết các packet switch đều sử dụng nguyên lý truyền lưu-và-chuyển-tiếp. Tức là bộ chuyển mạch phải nhận ĐẦY ĐỦ toàn bộ gói tin từ đường dẫn đầu vào trước khi nó có thể bắt đầu đẩy byte đầu tiên của gói tin đó ra đường dẫn đầu ra. Điều này gây ra một độ trễ gọi là Store-and-Forward delay. Chẳng hạn, gửi gói tin có kích thước L (bits) qua đường truyền tốc độ R (bps) thì độ trễ của nguyên lý lưu-chuyển-tiếp trên 1 link là L/R giây.

**Queuing Delay và Packet Loss (Độ trễ hàng đợi và mất gói tin):**
Mỗi packet switch có nhiều liên kết, mỗi liên kết có một bộ đệm đầu ra (output buffer) hoặc hàng đợi (queue). Nếu một gói tin đi đến và thấy đường truyền đầu ra đang bận rộn vì đang phải gửi các gói tin khác, nó sẽ phải chờ trong hàng đợi. Độ trễ chờ đợi này được gọi là queuing delay. Nếu hàng đợi đã đầy mà một gói tin mới lại đến, bộ đệm không còn chỗ chứa, gói tin đó sẽ bị loại bỏ (drop), hiện tượng này gọi là packet loss (mất gói tin).

**Forwarding và Routing (Chuyển tiếp và Định tuyến):**
Tại router, mỗi gói tin đều mang địa chỉ đích đến (destination IP address). Router sở hữu một **forwarding table** (bảng chuyển tiếp) giúp ánh xạ địa chỉ đích (hoặc dải địa chỉ) đến đường dẫn đầu ra tương ứng. Khi gói tin tới, router dựa vào địa chỉ đích để tra bảng và đẩy gói tin vào giao diện đầu ra thích hợp.
- **Routing protocols**: Là những giao thức tự động cấu hình các bảng chuyển tiếp trong router (như OSPF, BGP) dựa trên giải thuật để tìm ra con đường ngắn nhất và tối ưu nhất từ nguồn tới đích.

### 1.3.2 Circuit Switching (Chuyển mạch kênh)
Trái với chuyển mạch gói, trong chuyển mạch kênh, tài nguyên (như băng thông) trên toàn bộ tuyến đường từ nguồn đến đích được DÀNH RIÊNG (reserved) trước khi diễn ra việc truyền tải dữ liệu, và tồn tại trong suốt phiên giao tiếp (session). Mạng điện thoại truyền thống là ví dụ điển hình của Circuit Switching.

Các kỹ thuật để chia sẻ băng thông trong chuyển mạch kênh bao gồm:
- **FDM (Frequency-Division Multiplexing):** Băng thông của liên kết chia thành các dải tần số nhỏ hơn (frequency bands), mỗi kết nối (kênh) dùng riêng một dải tần số ổn định suốt thời gian kết nối.
- **TDM (Time-Division Multiplexing):** Thời gian truyền được chia thành các khung hình (frames) có kích thước cố định, trong mỗi frame lại chia ra các khe thời gian (slots). Mỗi kết nối được cấp phép sử dụng 1 khe thời gian trong 1 frame để truyền. Do đó tốc độ sẽ bằng tốc độ đường link chia cho số khe thời gian trong khung.

**Packet Switching vs Circuit Switching:**
Packet switching không yêu cầu thiết lập mạch riêng ảo. Nó linh hoạt hơn, sử dụng tài nguyên hiệu quả hơn (statistical multiplexing) và phục vụ được nhiều người dùng hơn. Tuy nhiên, chuyển mạch gói không thể đảm bảo chắc chắn về độ trễ, tốc độ, nên không phù hợp hoàn toàn với các yêu cầu thời gian thực khắt khe. Ngược lại, circuit switching đảm bảo được tài nguyên truyền tải, nhưng làm lãng phí rất nhiều tài nguyên (silent periods - người dùng không truyền thì tài nguyên cũng không ai được dùng). Internet ngày nay dựa hoàn toàn trên nền tảng chuyển mạch gói (Packet Switching).

---

## 1.4 Độ trễ (Delay), Mất gói (Loss) và Băng thông (Throughput) trong mạng Packet-Switched

Hiểu về hiệu năng mạng đồng nghĩa với việc hiểu về 3 yếu tố quan trọng nhất: Delay, Loss và Throughput.

### 1.4.1 Bốn nguồn gốc của độ trễ (Delay)
Khi một gói tin di chuyển từ một node sang node tiếp theo dọc con đường, gói tin sẽ gặp phải nhiều loại độ trễ khác nhau:
1. **Nodal Processing Delay (Trễ xử lý tại nút):** Thời gian cần thiết để router kiểm tra header của gói tin và quyết định cổng đầu ra nào cần chuyển tới. Nó cũng bao gồm thời gian kiểm tra lỗi bit ở cấp độ link-layer. Trễ xử lý thường rất nhỏ (vài microsecond).
2. **Queuing Delay (Trễ hàng đợi):** Thời gian gói tin phải chờ ở hàng đợi đầu ra trước khi đến lượt được phát lên đường truyền. Độ trễ này phụ thuộc vào tình trạng tắc nghẽn của mạng, có thể dao động từ 0 đến vài milisecond.
3. **Transmission Delay (Trễ truyền đi):** Hay còn gọi là độ trễ đẩy (push delay). Là thời gian để router đẩy toàn bộ L bits của gói tin lên đường liên kết vật lý. Nếu R là transmission rate (bps), thì Trễ truyền đi = L / R. Tốc độ R phụ thuộc vào dung lượng mạng (VD: 10Mbps tới 10Gbps).
4. **Propagation Delay (Trễ lan truyền):** Thời gian để một bit sau khi lên đường truyền có thể chạy qua môi trường vật lý từ node A sang node B. Phụ thuộc vào khoảng cách (d) giữa 2 node và tốc độ truyền tín hiệu điện từ qua môi trường đó (v, xấp xỉ tốc độ ánh sáng ~ 2x10^8 đến 3x10^8 m/s). Propagation Delay = d / v.

**Phân biệt Transmission Delay và Propagation Delay:**
Transmission Delay là thời gian router đẩy gói tin vào đường dây (phụ thuộc vào chiều dài gói tin L và băng thông R, không phụ thuộc khoảng cách). Propagation Delay là thời gian tín hiệu bit trôi trong cáp từ node này sang node kia (phụ thuộc khoảng cách d, không phụ thuộc kích cỡ gói tin và tốc độ link R).

*Tổng Nodal Delay = Nodal Processing Delay + Queuing Delay + Transmission Delay + Propagation Delay*

### 1.4.2 Mất gói tin (Packet Loss)
Nếu tỉ lệ các gói tin đến router quá lớn trong một khoảng thời gian dài, hàng đợi (queue) sẽ bị đầy (buffer overflow). Vì khả năng lưu trữ là có hạn, một gói tin đến nơi khi hàng đợi không còn chỗ chứa sẽ bị "drop" (bị loại bỏ) và gây ra hiện tượng mất gói tin.
Để xử lý, các gói tin bị mất đôi khi có thể được re-transmitted (gửi lại) từ các thiết bị end systems nhờ các giao thức ở tầng trên (như TCP). Tuy nhiên điều này lại làm tăng delay nói chung cho toàn bộ luồng truyền.

### 1.4.3 Thông lượng (Throughput)
Thông lượng là tốc độ truyền dữ liệu THỰC TẾ đang diễn ra trên mạng (số bits / giây) giữa tiến trình gửi và tiến trình nhận.
- **Instantaneous throughput (Thông lượng tức thời):** Tốc độ truyền ở một khoảng thời gian cực ngắn nào đó.
- **Average throughput (Thông lượng trung bình):** Tốc độ truyền trên một khoảng thời gian dài hơn (Tổng file size F / Thời gian truyền T).
- **Nút thắt cổ chai (Bottleneck link):** Giả sử file đi qua 1 link Rc, một link Rs. Nếu Rs < Rc, throughput của kết nối đầu cuối (end-to-end throughput) sẽ bị giới hạn bởi Rs. Liên kết có tốc độ thấp nhất trên path cản trở toàn bộ throughput được gọi là bottleneck link. Trên mạng Internet ngày nay, bottleneck link thường nằm tại các mạng truy cập (Access network).

---

## 1.5 Kiến trúc phân tầng và Mô hình tham chiếu (Protocol Layers and Service Models)

Vì mạng máy tính và Internet là một hệ thống cực kỳ phức tạp bao gồm ứng dụng, hệ điều hành, vô vàn các giao thức, thiết bị kết nối. Các nhà thiết kế mạng đã dùng cách **Phân tầng (Layering)** để thiết kế hệ thống. Mỗi tầng giải quyết một vấn đề nhỏ hẹp của quá trình kết nối và cung cấp dịch vụ (service) cho tầng nằm ngay trên nó dựa vào những dịch vụ của tầng nằm dưới.

Lợi ích của phân tầng:
- Cấu trúc hoá công việc phức tạp, cho phép xác định rõ mối quan hệ tương tác giữa các phần tử.
- Thiết kế theo dạng module, dễ dàng cập nhật và bảo trì. Thay đổi chi tiết thực thi của một tầng không làm ảnh hưởng đến các tầng khác.

Có hai mô hình phân tầng phổ biến: Mô hình OSI và Mô hình TCP/IP.

### 1.5.1 Mô hình Internet (TCP/IP)
Kiến trúc Internet ngày nay dựa trên 5 tầng (layers):

1. **Tầng ứng dụng (Application Layer):**
   - Đây là nơi các ứng dụng mạng (Network applications) và giao thức ở tầng ứng dụng cư trú.
   - Các giao thức nổi bật: HTTP (để truyền tải Web), SMTP (truyền email), FTP (truyền file), DNS (phân giải tên miền).
   - Đơn vị dữ liệu: **Message** (Bản tin).
2. **Tầng giao vận (Transport Layer):**
   - Nhiệm vụ chuyển bản tin của Application layer từ một process (tiến trình) của máy này tới một process ở máy khác.
   - Hai giao thức chính là TCP và UDP. TCP đảm bảo truyền tin tin cậy, không mất gói, đúng thứ tự, và có kiểm soát luồng/tắc nghẽn. UDP truyền tin phi kết nối, không đáng tin cậy nhưng tốc độ nhanh (phù hợp truyền video/âm thanh).
   - Đơn vị dữ liệu: **Segment** (Đoạn tin).
3. **Tầng mạng (Network Layer):**
   - Chịu trách nhiệm chuyển một gói tin của mạng (Datagram) từ một host (máy chủ) này đến một host khác ở đâu đó trên toàn cầu thông qua nhiều router.
   - Giao thức cốt lõi là giao thức IP (Internet Protocol) định nghĩa cấu trúc của datagram và cách đánh địa chỉ. Cùng với đó là các giao thức định tuyến (Routing protocols) giúp tìm đường đi tốt nhất.
   - Đơn vị dữ liệu: **Datagram** (Gói tin).
4. **Tầng liên kết (Link Layer):**
   - Để đẩy packet từ một node tới node kề cận theo một đường dẫn, network layer giao datagram cho link layer. Link layer chịu trách nhiệm truyền datagram giữa các nút (node) đứng liền kề qua link vật lý.
   - Các giao thức tiêu biểu: Ethernet, Wi-Fi 802.11, DOCSIS, PPP.
   - Đơn vị dữ liệu: **Frame** (Khung).
5. **Tầng vật lý (Physical Layer):**
   - Chuyển tiếp các bits trong frame từ node này sang node tiếp theo. Giao thức ở tầng này hoàn toàn phụ thuộc vào đặc tính của môi trường truyền vật lý (cáp đồng, cáp quang, sóng vô tuyến).

### 1.5.2 Mô hình tham chiếu OSI (OSI Model)
Vào cuối thập niên 1970, Tổ chức Tiêu chuẩn Quốc tế (ISO) đề xuất mô hình 7 tầng gọi là OSI (Open Systems Interconnection). Dù hiện nay TCP/IP đã là tiêu chuẩn thực tế của Internet, mô hình OSI vẫn có ý nghĩa hàn lâm rất lớn trong đào tạo. 7 tầng của OSI gồm có:

1. **Physical Layer**: Truyền bit trên môi trường vật lý.
2. **Data Link Layer**: Khung hóa, địa chỉ vật lý (MAC), kiểm soát lỗi node-to-node.
3. **Network Layer**: Định tuyến và địa chỉ logic (IP).
4. **Transport Layer**: Truyền tải tin cậy end-to-end, gộp kênh.
5. **Session Layer (Tầng phiên):** Cung cấp các công cụ cấu trúc dữ liệu, đồng bộ hóa, thiết lập, quản lý và kết thúc các phiên làm việc giữa các ứng dụng. (Trong TCP/IP, vai trò này được đẩy lên cho tầng Application quyết định).
6. **Presentation Layer (Tầng trình diễn):** Cho phép các ứng dụng diễn giải ý nghĩa của dữ liệu được truyền, giải quyết các khác biệt về định dạng dữ liệu như mã hóa dữ liệu (encryption), nén dữ liệu (compression). (Trong TCP/IP, vai trò này cũng thuộc tầng Application).
7. **Application Layer**: Giao diện với người dùng/ứng dụng.

### 1.5.3 Quá trình Đóng gói (Encapsulation)
Tại host gửi, một *Message* từ application layer được gửi xuống transport layer. Transport layer đính kèm thông tin header của nó (như port number) vào message tạo thành một *Segment*. Sau đó transport layer gửi segment xuống network layer.
Network layer thêm header của nó (như địa chỉ IP nguồn/đích) tạo thành *Datagram* rồi gửi xuống link layer. Link layer lại thêm header (như MAC address) để tạo thành *Frame* trước khi được chuyển đổi thành chuỗi bit truyền qua Physical layer. Quá trình bọc các lớp header này vào payload gọi là **Đóng gói (Encapsulation)**. Tại host nhận, quá trình ngược lại gọi là Giải đóng gói (Decapsulation) được thực hiện. Các packet switch, như router chỉ giải mã tới tầng Network, trong khi link-layer switch chỉ giải mã tới tầng Link.

---

## 1.6 An ninh Mạng cơ bản (Network Security)

Mạng Internet ban đầu được thiết kế với tư duy về một nhóm người dùng tin cậy với nhau. Thật không may, Internet ngày nay có vô vàn các nguy cơ đe dọa bảo mật. Những kẻ tấn công (hackers, botnet) luôn rình rập và có thể tấn công từ bất kỳ đâu.

### 1.6.1 Mã độc (Malware)
Hacker có thể đính kèm mã độc vào các thiết bị. Mã độc có thể xóa tập tin, thu thập mật khẩu, theo dõi bàn phím (spyware). Mã độc có thể xâm nhập bằng cách lừa người dùng tải về file độc hại. Khi đã xâm nhập vào thiết bị, malware có thể lây lan cho các host khác thành mạng lưới **botnet** dùng cho các cuộc tấn công DDoS hay phát tán spam email. Các loại malware lây lan nhanh được gọi là **virus** (cần sự tương tác của con người để lây nhiễm, VD mở file đính kèm email) hoặc **worm** (có thể tự lây nhiễm từ máy này sang máy khác qua lỗ hổng mà không cần người thao tác).

### 1.6.2 Tấn công Từ chối dịch vụ (Denial of Service - DoS)
Tấn công DoS có thể làm sập một hệ thống mạng, một server hoặc một ứng dụng khiến dịch vụ không thể phục vụ người dùng hợp pháp. Tấn công DoS gồm ba loại hình chính:
- **Vulnerability attack:** Khai thác lỗi phần mềm/hệ điều hành bằng vài message dị biệt làm sập hệ thống.
- **Bandwidth flooding:** Hacker gửi lượng lớn gói tin liên tục nhắm vào đường truyền để bóp chết băng thông (ví dụ UDP flooding).
- **Connection flooding:** Hacker thiết lập hàng ngàn kết nối TCP một nửa (half-open) làm máy chủ hết cạn kiệt tài nguyên duy trì các kết nối ma này.

Một biến thể rất khó chống đỡ là **DDoS (Distributed DoS)**, nơi kẻ tấn công điều khiển hàng trăm ngàn máy tính bị nhiễm malware (botnet) cùng tập trung gửi traffic rác về mục tiêu duy nhất cùng một lúc.

### 1.6.3 Sniffing (Nghe lén) và Spoofing (Giả mạo)
- **Packet Sniffing (Nghe lén gói tin):** Kẻ tấn công đặt thiết bị ở gần và trong cùng một môi trường mạng LAN, có khả năng lấy cắp được mọi bản sao của gói tin đang truyền. Những dữ liệu nhạy cảm nếu không được mã hóa (ví dụ dùng HTTP thay vì HTTPS) sẽ bị lộ hoàn toàn mật khẩu.
- **IP Spoofing (Giả mạo IP):** Hacker thay đổi Header của IP, tạo ra một gói tin có địa chỉ IP nguồn (Source IP) giả mạo, giả vờ là mình là một người dùng đáng tin cậy hợp pháp trong mạng để xâm nhập. Các bộ lọc firewall tiên tiến mới có thể ngăn cản được phần nào kiểu giả mạo IP bằng giải pháp end-point authentication (chứng thực người dùng cuối ở mức chữ ký số).

---

## TÓM TẮT NHỮNG ĐIỂM CHÍNH (KEY TAKEAWAYS)
- Internet là một mạng của các mạng kết nối thiết bị đầu cuối với nhau thông qua mạng ISP, router, link.
- Giao thức định nghĩa các quy tắc giao tiếp. Cốt lõi của Internet là TCP/IP.
- Rìa mạng gồm các Host (End system) chia làm Client, Server.
- Lõi mạng sử dụng Packet switching (chuyển mạch gói), tối ưu và chia sẻ tài nguyên động nhưng không bảo đảm chất lượng thời gian thực thay vì Circuit switching (chuyển mạch kênh).
- Router thực hiện Forwarding (đẩy gói tin ở mức địa phương) và Routing (tìm đường liên kết mức toàn cục).
- 4 loại độ trễ mạng: Nodal processing, Queuing, Transmission (L/R) và Propagation (d/v). Nút thắt cổ chai quyết định Throughput.
- Mô hình kiến trúc phân tầng Internet có 5 tầng (Application, Transport, Network, Link, Physical), tương ứng các gói tin là Message, Segment, Datagram, Frame, và Bits. OSI model có thêm tầng Session và Presentation.
- Có ba mối đe dọa chính là Malware, DoS/DDoS và Packet Sniffing/IP Spoofing.

*Tài liệu được thiết kế riêng dành cho việc ôn thi trắc nghiệm học phần Mạng máy tính dựa trên giáo trình tiêu chuẩn Kurose & Ross.*

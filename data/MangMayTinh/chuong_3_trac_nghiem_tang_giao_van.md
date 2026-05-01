# CHƯƠNG 3: TRẮC NGHIỆM TẦNG GIAO VẬN (TRANSPORT LAYER)

**Câu 1:** Trong kiến trúc mạng TCP/IP, Tầng Giao vận (Transport Layer) có nhiệm vụ chính là gì?
A. Tìm đường đi ngắn nhất giữa hai router.
B. Cung cấp liên kết truyền thông logic trực tiếp giữa các TIẾN TRÌNH ỨNG DỤNG (Process-to-Process) chạy trên các máy khác nhau.
C. Mã hóa tín hiệu nhị phân thành sóng ánh sáng.
D. Sửa lỗi vật lý của cáp đồng.
*Đáp án: B*
*Giải thích: Nếu Tầng Mạng cung cấp giao tiếp Host-to-Host (nhà với nhà), thì Tầng Giao vận đi sâu hơn, chuyển thư tới tận tay từng người trong nhà (Process).*

**Câu 2:** Thuật ngữ "Multiplexing" (Ghép kênh) tại máy phát (Sender) ở Tầng Giao vận có nghĩa là gì?
A. Giải nén dữ liệu video trước khi phát.
B. Lấy các gói tin từ tầng Mạng, kiểm tra lỗi và đẩy lên đúng socket của phần mềm.
C. Thu thập các thông điệp từ nhiều Socket khác nhau, bọc chúng bằng Transport Header (để đánh dấu Port) rồi tạo thành các Segment đẩy xuống tầng mạng.
D. Tăng gấp đôi tốc độ đồng hồ của máy tính.
*Đáp án: C*
*Giải thích: Gom nhiều luồng dữ liệu từ các ứng dụng khác nhau thành một luồng xuống cáp mạng là quá trình ghép kênh.*

**Câu 3:** Giao thức nào ở Tầng Giao vận cung cấp dịch vụ Truyền dữ liệu KHÔNG ĐÁNG TIN CẬY (Unreliable) và PHI KẾT NỐI (Connectionless)?
A. HTTP
B. TCP
C. ICMP
D. UDP
*Đáp án: D*
*Giải thích: UDP gửi dữ liệu mà không cần thiết lập kết nối trước, không bận tâm dữ liệu có tới nơi hay có bị lỗi hay không.*

**Câu 4:** Socket của kết nối UDP được định danh bởi bao nhiêu tham số?
A. 2 tham số: Địa chỉ IP đích và Số hiệu cổng đích.
B. 4 tham số: IP nguồn, Cổng nguồn, IP đích, Cổng đích.
C. 1 tham số: Cổng đích.
D. 6 tham số.
*Đáp án: A*
*Giải thích: Do tính phi kết nối, hệ điều hành chỉ dùng 2 tuple (IP Đích, Port Đích) để nhét chung mọi thông điệp UDP vào cùng 1 socket.*

**Câu 5:** Máy chủ Web (Apache/Nginx) sử dụng TCP. Khi có 100 máy khách (Client) cùng kết nối đến Port 80 của máy chủ này, điều gì sẽ xảy ra ở tầng Giao vận của Server?
A. Server chỉ tạo 1 Socket TCP duy nhất để nhận 100 kết nối.
B. Xảy ra xung đột mạng do trùng Port.
C. Server sẽ sinh ra 100 Socket TCP khác nhau, mỗi Socket quản lý một phiên làm việc độc lập vì TCP dùng cơ chế 4-tuple (IP nguồn, Port nguồn, IP đích, Port đích) để phân kênh.
D. Server chuyển 99 kết nối sang UDP.
*Đáp án: C*
*Giải thích: Sức mạnh của TCP demultiplexing. IP nguồn và Cổng nguồn của mỗi client là khác nhau nên tạo ra bộ tứ (4-tuple) khác nhau.*

**Câu 6:** Trong UDP Header (dài 8 byte), trường Checksum có mục đích gì?
A. Đếm số lượng gói tin bị mất trên mạng.
B. Kiểm tra xem các bit trong đoạn tin (Segment) có bị lỗi (lật bit) do nhiễu vật lý trên đường truyền hay không.
C. Mã hóa mật khẩu người dùng.
D. Giới hạn băng thông của ứng dụng.
*Đáp án: B*
*Giải thích: Checksum sử dụng bù 1 để bắt lỗi. Mặc dù UDP không đảm bảo tin cậy, nó vẫn check lỗi cơ bản, nếu lỗi nó sẽ vứt gói tin đó đi.*

**Câu 7:** Để xây dựng một Giao thức truyền tin cậy (RDT) trên một đường truyền hay mất gói, phía gửi (Sender) BẮT BUỘC phải dùng công cụ nào để tự động gửi lại gói bị mất?
A. Bộ đếm thời gian (Timeout Timer).
B. Tín hiệu CTS/RTS.
C. Hàm băm SHA-256.
D. Bộ định tuyến không dây.
*Đáp án: A*
*Giải thích: Khi ném gói tin vào "hố đen" mạng mà không thấy ACK báo về, Sender sẽ bị kẹt mãi mãi nếu không có đồng hồ Timer để kích hoạt truyền lại.*

**Câu 8:** Số thứ tự (Sequence Number) được sinh ra để khắc phục vấn đề gì của đường truyền mạng?
A. Tăng kích thước bộ đệm.
B. Giúp bộ định tuyến chạy nhanh hơn.
C. Giúp phía nhận (Receiver) phân biệt được một gói tin gửi đến là dữ liệu MỚI hay chỉ là Bản sao gửi lặp lại (Duplicate) do phía gửi bị Timeout.
D. Giúp phân mảnh gói tin IP.
*Đáp án: C*
*Giải thích: ACK của Receiver có thể bị mất trên đường về. Sender tưởng mất gói nên gửi lại. Receiver phải xem số thứ tự để biết "À gói này mình nhận rồi, vứt đi, gửi lại cái ACK".*

**Câu 9:** Kỹ thuật Pipelining (Đường ống) trong truyền dữ liệu mạng có nghĩa là gì?
A. Nén dữ liệu xuống mức thấp nhất.
B. Nối nhiều đoạn cáp với nhau.
C. Phía gửi được phép gửi nhiều gói tin liên tiếp vào đường truyền mà KHÔNG CẦN phải chờ nhận được ACK của gói tin trước đó.
D. Chỉ cho phép gửi từng byte một.
*Đáp án: C*
*Giải thích: Trái ngược với Stop-and-wait, Pipelining giúp liên kết truyền dẫn luôn "đầy ắp" dữ liệu, tăng hiệu suất tận dụng băng thông (Utilization).*

**Câu 10:** Giao thức Go-Back-N (GBN) quản lý các báo nhận (ACK) theo cơ chế nào?
A. Báo nhận độc lập từng gói (Individual ACK).
B. Không sử dụng báo nhận.
C. Báo nhận lũy kế (Cumulative ACK) - Khi gửi ACK(n), có nghĩa là đã nhận thành công TẤT CẢ các gói từ n trở xuống.
D. Gửi ACK chung cho cả file.
*Đáp án: C*
*Giải thích: GBN có tính chất dồn cục. Nếu mất gói số 3, nhận được gói 4, 5, 6, nó sẽ bỏ qua và chỉ gào thét ACK(2) (Tới gói 2 là hết rồi). Timeout, gửi lại cả chùm từ 3.*

**Câu 11:** Khác biệt giữa Selective Repeat (SR) và Go-Back-N (GBN) khi xảy ra mất một gói tin là gì?
A. GBN gửi lại tất cả từ gói bị lỗi trở về sau; SR chỉ gửi lại ĐÚNG DUY NHẤT gói tin bị lỗi đó.
B. GBN gửi qua TCP, SR gửi qua UDP.
C. SR không dùng Timer.
D. SR không dùng bộ đệm ở máy nhận.
*Đáp án: A*
*Giải thích: Tên gọi "Phát lại có chọn lọc" (Selective Repeat) nói lên tất cả. Đổi lại, máy nhận phải có bộ đệm phức tạp để giữ các gói "vượt rào" chờ gói bị rớt tới.*

**Câu 12:** Trong TCP, quá trình thiết lập kết nối (3-way handshake) gồm các bước nào?
A. SYN -> SYN/ACK -> ACK
B. FIN -> ACK -> FIN -> ACK
C. RTS -> CTS -> DATA
D. GET -> POST -> OK
*Đáp án: A*
*Giải thích: Máy khách gửi SYN. Máy chủ đáp bằng SYN/ACK. Máy khách xác nhận lại bằng ACK. Hoàn tất quá trình tạo đường ống 2 chiều.*

**Câu 13:** Trường Acknowledgment Number (Số báo nhận) trong header của một TCP Segment từ máy B gửi cho máy A có giá trị là 1000. Nó mang thông điệp gì?
A. B đã gửi cho A 1000 byte.
B. B vừa nhận được byte số 1000 từ A.
C. B mong chờ nhận được byte tiếp theo từ A có số thứ tự (Sequence Number) bắt đầu từ 1000.
D. Kích thước cửa sổ của B là 1000 byte.
*Đáp án: C*
*Giải thích: TCP sử dụng số ACK lũy kế dự kiến. ACK=1000 ngầm hiểu "Tôi đã ôm trọn đến byte 999. Hãy ném cho tôi cục data bắt đầu bằng byte 1000".*

**Câu 14:** Sự kiện "Truyền lại nhanh" (Fast Retransmit) của TCP xảy ra khi nào?
A. Khi TCP đếm ngược Timer về 0.
B. Khi bộ đệm máy nhận báo đầy.
C. Khi phía gửi nhận được 3 gói ACK lặp lại (3 Duplicate ACKs) của cùng một số liệu.
D. Khi kết nối Wi-Fi bị yếu.
*Đáp án: C*
*Giải thích: Thay vì mỏi mòn chờ Timeout, nếu thấy Receiver liên tục hét "Gửi tôi gói 100" tới 3 lần, Sender tự hiểu gói 100 đã bốc hơi và truyền lại ngay.*

**Câu 15:** Kiểm soát luồng (Flow Control) trong TCP được sinh ra để bảo vệ đối tượng nào?
A. Bảo vệ cáp quang dưới biển.
B. Bảo vệ toàn bộ mạng lưới Router khỏi bị quá tải.
C. Bảo vệ Máy nhận (Receiver) khỏi việc bị tràn bộ đệm do Máy gửi bơm dữ liệu quá nhanh.
D. Bảo vệ Máy gửi khỏi bị nóng CPU.
*Đáp án: C*
*Giải thích: Cứ mỗi gói ACK, Receiver sẽ đính kèm thông số Receive Window (rwnd) báo cho Sender biết "Tao chỉ còn trống 5MB RAM thôi nhé, liệu mà gửi".*

**Câu 16:** Kiểm soát tắc nghẽn (Congestion Control) bảo vệ ai?
A. Bảo vệ Máy gửi.
B. Bảo vệ Máy nhận.
C. Bảo vệ sự ổn định của TOÀN MẠNG INTERNET bằng cách điều tiết lượng truy cập bơm vào hệ thống để các Router không bị sập.
D. Chống lại Hacker.
*Đáp án: C*
*Giải thích: Khác Flow control (1 đấu 1), Congestion control là trách nhiệm xã hội. Nếu mạng bị kẹt (thấy qua việc rớt gói tin), mọi TCP phải đồng loạt giảm ga.*

**Câu 17:** Pha Khởi động chậm (Slow Start) của thuật toán TCP Congestion Control tăng kích thước cửa sổ tắc nghẽn (cwnd) theo hình thức nào?
A. Tăng tuyến tính (Cộng thêm 1 mỗi lần).
B. Tăng theo cấp số nhân (Nhân đôi sau mỗi RTT) cho đến khi gặp ngưỡng ssthresh hoặc xảy ra mất gói.
C. Không tăng, giữ nguyên 1 MSS.
D. Tăng ngẫu nhiên.
*Đáp án: B*
*Giải thích: Cái tên "Chậm" chỉ đúng ở vạch xuất phát (cwnd=1). Nhưng nó tăng trưởng theo hàm mũ ($2^n$) nên thực chất vận tốc bứt tốc cực kỳ gắt.*

**Câu 18:** Khi TCP nhận thấy có mất gói do Timeout, nó phạt biến cwnd như thế nào?
A. Chỉ giảm đi một nửa.
B. Giảm đi 10%.
C. Hạ ssthresh xuống một nửa, và bóp nghẹt cwnd về vạch xuất phát 1 MSS (Quay lại Slow Start).
D. Không làm gì cả.
*Đáp án: C*
*Giải thích: Timeout là báo hiệu một vụ tắc đường thảm khốc, chả có gói nào về được. TCP bóp phanh lút cán về 1 MSS.*

**Câu 19:** Hành vi đồ thị của TCP Congestion Control được gọi là AIMD (Additive Increase, Multiplicative Decrease). Điều này tạo ra hình dạng đồ thị gì cho Thông lượng (Throughput)?
A. Đường thẳng đi lên mãi mãi.
B. Hình răng cưa (Saw-tooth).
C. Hình Sin tròn.
D. Đường cong parabol.
*Đáp án: B*
*Giải thích: TCP từ từ tăng ga (Tuyến tính - Additive), đến lúc đụng trần gây mất gói, nó bóp phanh cắt nửa (Multiplicative), rồi lại rà ga lên từ từ. Đồ thị y như cái răng cưa.*

**Câu 20:** Nếu máy A gửi cho máy B một Segment chứa 100 bytes dữ liệu, có Sequence Number = 300. Dữ liệu đến an toàn. Vậy máy B sẽ gửi gói ACK có số hiệu là bao nhiêu?
A. 300
B. 100
C. 400
D. 401
*Đáp án: C*
*Giải thích: Segment A mang các byte từ 300 đến 399. Byte tiếp theo mà B cần là 400. Do đó Acknowledgment Number = 400.*

**Câu 21:** Cơ chế thiết lập kết nối của TCP rất dễ bị lợi dụng để thực hiện cuộc tấn công Từ chối dịch vụ (DoS) kiểu nào sau đây?
A. UDP Flooding
B. SYN Flooding
C. Ping of Death
D. MAC Spoofing
*Đáp án: B*
*Giải thích: Hacker gửi hàng vạn gói SYN nhưng dùng IP giả. Máy chủ trả lời SYN-ACK và cấp phát sẵn tài nguyên (buffer/RAM) để chờ ACK cuối cùng. Khách không bao giờ gửi ACK, làm máy chủ cạn kiệt bộ nhớ.*

**Câu 22:** Giai đoạn "Tránh tắc nghẽn" (Congestion Avoidance) của TCP hoạt động như thế nào?
A. Tăng kích thước cửa sổ cwnd lên gấp đôi sau mỗi RTT.
B. Tăng kích thước cwnd một cách tuyến tính, thêm 1 MSS cho mỗi RTT trôi qua.
C. Giảm cửa sổ cwnd đi 1 MSS mỗi khi nhận được ACK.
D. Khóa chặn ứng dụng để không cho tải thêm dữ liệu.
*Đáp án: B*
*Giải thích: Sau khi cwnd vượt qua ngưỡng ssthresh (Slow Start Threshold), TCP chuyển từ tăng mũ sang tăng tuyến tính rà dậm chân để thăm dò giới hạn cuối cùng.*

**Câu 23:** Quá trình giải phóng kết nối (Ngắt kết nối) của TCP diễn ra như thế nào?
A. Gửi 1 gói tin EXIT và ngắt ngay lập tức.
B. Diễn ra theo quy trình 4 bước (4-way handshake) trao đổi cờ FIN và ACK. Cả hai phía đều phải báo gửi FIN để chấm dứt phiên truyền dữ liệu.
C. Máy chủ cắt điện mạng.
D. Rút dây mạng.
*Đáp án: B*
*Giải thích: Kết nối TCP là Full-duplex (2 chiều). A gửi FIN để báo A xong rồi. Nhưng B vẫn có thể tiếp tục gửi nốt dữ liệu cho A cho đến khi B cũng gửi FIN.*

**Câu 24:** Biến cwnd (Congestion Window) và rwnd (Receive Window) có mối liên hệ như thế nào trong việc quyết định lượng dữ liệu tối đa (Unacknowledged data) mà Máy gửi được phép bơm ra mạng?
A. Dữ liệu tối đa = cwnd + rwnd.
B. Dữ liệu tối đa = Min (cwnd, rwnd).
C. Dữ liệu tối đa = Max (cwnd, rwnd).
D. Dữ liệu tối đa = rwnd / cwnd.
*Đáp án: B*
*Giải thích: TCP phải tuân thủ nghiêm ngặt theo kẻ yếu nhất. Nếu mạng báo chỉ cho đi 10MB (cwnd), nhưng máy nhận báo RAM chỉ còn 2MB (rwnd), thì Máy gửi chỉ được xuất xưởng 2MB.*

**Câu 25:** Ưu điểm của kiến trúc UDP so với TCP là gì?
A. Đảm bảo dữ liệu đến đúng thứ tự.
B. Kích thước Header nhỏ bé (8 byte) giúp tiết kiệm băng thông và không mất thời gian thiết lập kết nối (RTT ban đầu = 0).
C. Có chức năng mã hóa dữ liệu mặc định.
D. Chống lại cuộc tấn công DDoS.
*Đáp án: B*
*Giải thích: Sự gọn nhẹ của UDP là lý tưởng cho các luồng dữ liệu liên tục như video streaming hoặc truy vấn DNS siêu tốc.*

**Câu 26:** Trong giao thức TCP, để tính toán thời gian Timeout (Hẹn giờ hết hạn), máy tính phải dựa trên thông số nào?
A. Tốc độ quay của quạt tản nhiệt.
B. Thời gian RTT (Round Trip Time) đo lường được trên mạng (EstimatedRTT) cộng với sai số biên độ biến thiên (DevRTT).
C. Khoảng cách địa lý bằng km đo bằng GPS.
D. Dung lượng RAM của thiết bị.
*Đáp án: B*
*Giải thích: Mạng có lúc nhanh lúc chậm, TCP không thể set cứng Timeout = 1 giây. Nó liên tục đo RTT để tính ra Timeout Interval tối ưu, đảm bảo không bắt chờ quá lâu cũng không quá vội vã.*

**Câu 27:** Một ứng dụng tải phim từ Server qua HTTP (dùng TCP). Đột nhiên có một người tải file cực kỳ lớn qua đường liên kết bên cạnh dùng UDP khiến tắc nghẽn cục bộ. Điều gì sẽ xảy ra?
A. TCP sẽ tự động nâng băng thông lên để đè UDP.
B. Kênh TCP sẽ ngoan ngoãn tự bóp băng thông (giảm cwnd) do có rơi vãi gói tin, trong khi UDP vẫn xả láng với tốc độ ứng dụng. Kết quả UDP sẽ bóp nghẹt TCP.
C. UDP tự động nhường đường cho TCP.
D. Cả hai cùng bị rớt mạng hoàn toàn.
*Đáp án: B*
*Giải thích: Đây là một vấn đề bất công (fairness) nổi tiếng. UDP không có cơ chế Congestion Control, nó giống xe biển xanh ưu tiên, cứ thế lao vào điểm nghẽn, ép các ứng dụng TCP phải tự phanh lại.*

**Câu 28:** Giao thức nào hoạt động ở cả Mạng máy tính có dây và Mạng di động không dây (4G/Wi-Fi)?
A. CSMA/CD
B. ARP
C. TCP và UDP
D. OSPF
*Đáp án: C*
*Giải thích: TCP và UDP chạy ở tầng Transport (cấp ứng dụng), chúng không hề quan tâm thiết bị dưới dây cáp là đồng, quang hay vô tuyến.*

**Câu 29:** Để một máy khách biết được một cổng (Port) của máy chủ có đang sẵn sàng phục vụ dịch vụ hay không, thao tác kỹ thuật thường dùng là gì?
A. Ping IP
B. Port Scanning (Quét cổng)
C. Phân giải DNS
D. Gửi gói ICMP
*Đáp án: B*
*Giải thích: Hacker hoặc quản trị viên dùng nmap (Port scanner) gửi các gói SYN tới từng port từ 1 đến 65535. Nếu Port nào có trả về SYN-ACK nghĩa là cửa đó đang mở.*

**Câu 30:** Trạng thái TIME_WAIT cuối quá trình ngắt kết nối TCP của máy chủ chủ động ngắt có ý nghĩa gì?
A. Chờ người dùng thanh toán tiền mạng.
B. Bắt máy chủ nhận nốt dữ liệu còn thiếu.
C. Đợi 1 khoảng thời gian (thường là 2 lần MSL) để đảm bảo các gói tin cũ bị lạc (delayed segments) có thời gian bốc hơi khỏi mạng hoàn toàn, tránh ảnh hưởng tới phiên làm việc mới nếu xài lại port đó.
D. Cập nhật bảng định tuyến nội bộ.
*Đáp án: C*
*Giải thích: Trên Internet hay có những gói tin bị kẹt trong router 1 thời gian dài rồi mới tới. TIME_WAIT giúp cái ống nước thật sự sạch sẽ trước khi đóng cửa.*

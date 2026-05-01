# CHƯƠNG 3: TẦNG GIAO VẬN (TRANSPORT LAYER)

## 3.1 Dịch vụ Tầng Giao vận (Transport-Layer Services)

Tầng giao vận cung cấp **dịch vụ giao tiếp logic (logical communication)** trực tiếp giữa các tiến trình (processes) ứng dụng chạy trên các host khác nhau. Nhờ có dịch vụ này, dưới con mắt của ứng dụng, hai tiến trình dường như được kết nối trực tiếp với nhau, cho dù chúng có cách xa nhau nửa vòng trái đất và phải vượt qua hàng chục bộ định tuyến.

### 3.1.1 Sự khác biệt giữa Network Layer và Transport Layer
Để hiểu rõ, hãy dùng hình ảnh ẩn dụ: Mạng lưới bưu chính.
- *Host (Thiết bị)* là các ngôi nhà.
- *Process (Tiến trình)* là những người sống trong nhà.
- *Application Message (Bản tin)* là những bức thư trong phong bì.
- *Network Layer (Tầng mạng)*: Là những người đưa thư, xe bưu điện. Chịu trách nhiệm vận chuyển bưu phẩm từ **Nhà này đến Nhà kia** (từ Host tới Host).
- *Transport Layer (Tầng giao vận)*: Là anh chị em đại diện trong gia đình có nhiệm vụ thu thập thư từ các thành viên trong nhà gửi cho bưu điện, và nhận thư từ bưu điện để chia về tay chính xác từng người trong nhà. Nghĩa là giao vận từ **Người đến Người** (từ Process tới Process).

Giao thức của Transport layer KHÔNG được phép can thiệp vào các bộ định tuyến trong lõi mạng (core routers). Nó chỉ được triển khai tại các thiết bị đầu cuối (end systems).
- Tại host gửi: Nó cắt các Application messages ra thành nhiều phần, thêm Transport header tạo thành các **Segment** rồi đẩy xuống Network layer (IP).
- Tại host nhận: Nó nhận các Datagram từ Network layer, lấy ra các Segment, rắp ráp lại và chuyển đến đúng ứng dụng qua Socket.

### 3.1.2 Multiplexing và Demultiplexing (Ghép kênh và Phân kênh)
Làm thế nào để Transport Layer biết chuyển dữ liệu cho ứng dụng nào trong máy (vì một máy tính có thể mở cùng lúc Web, Game, Skype)? Trả lời: Nhờ vào **Socket** và **Port Number (Số hiệu cổng)**.
- **Demultiplexing (Phân kênh ở máy nhận):** Quá trình Transport layer kiểm tra thông tin Port Number trong Segment đến, và điều hướng Segment đó vào đúng socket của tiến trình phù hợp.
- **Multiplexing (Ghép kênh ở máy gửi):** Quá trình thu gom dữ liệu từ nhiều socket của nhiều tiến trình, gói gọn chúng bằng cách gắn Header (có chứa Source Port và Destination Port) để tạo thành Segment, rồi chuyển xuống Network layer.

Số hiệu cổng (Port) là một số 16-bit, từ 0 đến 65535. Các port từ 0 - 1023 là Well-known ports (Cổng được cấp phép chặt chẽ cho các ứng dụng tiêu chuẩn như HTTP 80, FTP 21, SSH 22).

**Phân kênh không kết nối (UDP Demultiplexing):**
Socket UDP được định danh bởi một bộ 2 thông số (two-tuple): `(Destination IP, Destination Port)`. Do đó, nếu hai máy khách A và B cùng gửi UDP segment đến cùng một IP Máy chủ, cùng Port Máy chủ (vd 53), cả hai segment này sẽ được đẩy vào chung MỘT socket duy nhất tại Máy chủ.

**Phân kênh có kết nối (TCP Demultiplexing):**
Socket TCP được định danh bằng một bộ 4 thông số (four-tuple): `(Source IP, Source Port, Destination IP, Destination Port)`. Do đó, ngay cả khi 10 máy khách cùng gửi dữ liệu đến IP Máy chủ ở Port 80, Máy chủ Web sẽ tạo ra 10 Socket khác biệt để tiếp nhận 10 luồng dữ liệu này. Đây là cốt lõi của kết nối máy chủ Web đồng thời.

---

## 3.2 Giao thức UDP (User Datagram Protocol)

UDP (RFC 768) là giao thức tầng Giao vận ở mức tối giản nhất. Nó thực hiện công việc lấy dữ liệu từ ứng dụng, cộng thêm thông tin ghép kênh/phân kênh, thêm chức năng kiểm tra lỗi đơn giản, rồi đẩy thẳng xuống tầng Mạng.
Đặc điểm:
- **Phi kết nối (Connectionless):** Không có quá trình thiết lập kết nối (bắt tay) giữa bên gửi và nhận trước khi truyền. Không tốn thời gian RTT khởi tạo.
- **Không đáng tin cậy:** Gói tin UDP gửi đi có thể bị mất, lộn xộn thứ tự.
- **Không kiểm soát luồng, không kiểm soát tắc nghẽn:** Gửi dữ liệu ra mạng với bất kỳ tốc độ nào mà ứng dụng có thể đẩy. Gây ra hiện tượng chèn ép các TCP flows nếu UDP xả rác quá mức.
- **Segment header rất nhỏ:** Chỉ 8 bytes (TCP header tốn 20 bytes).

**Cấu trúc UDP Header (8 bytes):**
1. Source Port (2 bytes)
2. Destination Port (2 bytes)
3. Length (2 bytes)
4. Checksum (2 bytes)

**UDP Checksum:** Dùng để phát hiện xem các bit trong segment có bị thay đổi (do nhiễu đường truyền vật lý hoặc lỗi bộ nhớ router) khi di chuyển từ nguồn đến đích hay không. Bên gửi tính tổng các đoạn 16-bit của gói tin, bù 1 và đặt vào trường checksum. Bên nhận cộng tất cả lại, nếu kết quả toàn bit 1 thì không có lỗi, nếu có bit 0 tức là bị lỗi và UDP thường sẽ loại bỏ gói tin đó.

Ứng dụng của UDP: Các ứng dụng cần phản hồi cực nhanh (DNS), đa phương tiện thời gian thực không nhạy cảm việc mất mát (Skype, VoIP, Streaming), SNMP.

---

## 3.3 Nguyên lý Truyền dữ liệu Tin cậy (Principles of Reliable Data Transfer - RDT)

Vì tầng mạng (IP) bên dưới là không tin cậy (Unreliable), giao thức vận chuyển (như TCP) phải xây dựng một ảo giác về một đường ống "Tin cậy tuyệt đối" ở tầng trên. Dữ liệu truyền không bao giờ bị hỏng (corrupted) và không bao giờ bị mất.

Để xây dựng RDT, các nhà thiết kế dùng các cơ chế sau:
1. **Error Detection (Phát hiện lỗi):** Checksum để biết gói tin bị hỏng bit.
2. **ACK/NAK (Phản hồi):** Receiver gửi gói tin báo nhận (Acknowledgement) khi nhận thành công, hoặc Negative Acknowledgement khi gói tin bị lỗi để Sender biết gửi lại.
3. **Timeout (Hẹn giờ):** Nếu Sender gửi gói tin đi, nhưng gói tin bị mất, hoặc gói ACK báo về bị mất, Sender sẽ chờ mãi mãi? Giải pháp là Timer. Sender đặt đồng hồ đếm ngược. Nếu hết thời gian timeout mà chưa nhận được ACK, Sender sẽ tự động Retransmit (gửi lại) gói tin đó.
4. **Sequence Number (Số thứ tự):** Khi gửi lại do timeout, Receiver có thể nhận được các bản sao lặp lại của cùng một gói tin (Duplicate packets). Để Receiver phân biệt gói mới và gói bị lặp, mỗi gói tin phải được đánh số thứ tự (Sequence number).

**RDT theo nguyên lý Pipelining (Đường ống):**
Trong giao thức RDT cơ bản như Stop-and-Wait, Sender gửi 1 gói, chờ ACK, rồi mới gửi gói 2. Điều này làm hiệu suất cực thấp vì đường truyền lớn bị bỏ trống. Giải pháp là Pipelining: Sender được phép gửi nhiều gói tin liên tiếp mà không cần chờ ACK ngay lập tức. Tuy nhiên, nó yêu cầu phải có Buffer để lưu trữ, và cơ chế đánh số thứ tự lớn hơn.
Có 2 cách xử lý lỗi trong Pipelining:
- **Go-Back-N (GBN):** Sender duy trì một "cửa sổ trượt" (sliding window) kích thước N. Nếu gói thứ K bị lỗi/mất, Receiver sẽ bỏ qua mọi gói tin K+1, K+2 gửi đến sau đó. Khi Sender bị Timeout ở gói K, nó sẽ phải gửi lại TOÀN BỘ các gói từ K đến N. GBN gửi ACK lũy kế (Cumulative ACK).
- **Selective Repeat (SR - Phát lại có chọn lọc):** Sender chỉ gửi lại CHÍNH XÁC gói tin bị lỗi hoặc bị mất, chứ không phải gửi lại cả một loạt. Receiver có buffer để chứa các gói nhận sớm hơn thứ tự (out-of-order) và gửi các ACK riêng lẻ (Individual ACK).

---

## 3.4 Giao thức TCP (Transmission Control Protocol)

TCP (RFC 793) cung cấp dịch vụ tin cậy, hướng kết nối, và truyền luồng byte (byte-stream).

### 3.4.1 Đặc điểm cơ bản của TCP
- **Hướng kết nối:** TCP yêu cầu thiết lập kết nối logic trước qua quá trình 3-way handshake.
- **Full-duplex:** Truyền dữ liệu đồng thời hai chiều trên cùng một kết nối.
- **Point-to-point:** Mỗi kết nối TCP chỉ thiết lập giữa đúng 1 Sender và 1 Receiver (không có chuyện multicasting).
- **In-order byte stream:** Dữ liệu truyền đi dưới dạng luồng byte tuần tự.

**Cấu trúc TCP Header (Thường 20 bytes):**
- Source Port / Dest Port (4 bytes)
- **Sequence Number (Số thứ tự - 4 bytes):** Là số hiệu của byte ĐẦU TIÊN trong luồng dữ liệu của segment này. (TCP đánh số theo bytes, không đánh số theo số lượng gói).
- **Acknowledgment Number (Số báo nhận - 4 bytes):** Là số hiệu của byte TIẾP THEO mà máy nhận đang mong chờ (Cumulative ACK).
- Header Length, Flags (ACK, SYN, FIN, RST, PSH, URG), Receive Window, Checksum...

### 3.4.2 Quá trình Thiết lập và Đóng kết nối
**Thiết lập (3-way Handshake):**
1. Client gửi một **SYN segment** cho Server (Cờ SYN=1, Seq=x). Client ở trạng thái SYN_SENT.
2. Server nhận SYN, cấp phát buffer. Phản hồi bằng **SYNACK segment** (Cờ SYN=1, ACK=1, Seq=y, Ack_num=x+1). Server chuyển sang SYN_RCVD.
3. Client nhận SYNACK, phản hồi bằng **ACK segment** (Cờ ACK=1, Seq=x+1, Ack_num=y+1). Có thể mang theo payload dữ liệu. Client và Server chuyển sang ESTABLISHED.

**Đóng kết nối (4-way Handshake):**
1. Client gửi **FIN segment** báo muốn ngắt. Trạng thái FIN_WAIT_1.
2. Server nhận FIN, phản hồi **ACK**. Server ở trạng thái CLOSE_WAIT. Client nhận ACK sang FIN_WAIT_2.
3. Khi Server đã truyền xong mọi dữ liệu còn lại, nó cũng gửi **FIN segment**. Chuyển sang LAST_ACK.
4. Client nhận FIN, phản hồi **ACK**. Client vào trạng thái TIME_WAIT (thường chờ một lúc để đảm bảo mạng xóa hết các gói lạc). Sau đó kết thúc (CLOSED). Server nhận ACK thì CLOSED ngay.

### 3.4.3 TCP Reliable Data Transfer (Truyền tin cậy)
TCP sử dụng Timer. Vậy đặt Timeout bao lâu là vừa? TCP tính toán RTT liên tục qua các mẫu (SampleRTT) để đưa ra EstimatedRTT bằng công thức trung bình có trọng số mũ EWMA (Exponential Weighted Moving Average) để làm mượt dữ liệu. TimeoutInterval = EstimatedRTT + 4 * DevRTT.

**Truyền lại nhanh (Fast Retransmit):**
Chờ Timeout thường rất lâu. Tuy nhiên TCP có mẹo: Nếu Sender nhận được 3 ACK lặp lại (Duplicate ACKs) cùng một số thứ tự, nghĩa là Receiver đang gào thét "Tôi thiếu đoạn này, các đoạn sau tới hết rồi". Sender lập tức gửi lại ngay gói tin đó mà KHÔNG ĐỢI TIMEOUT.

### 3.4.4 Flow Control (Kiểm soát luồng)
TCP cung cấp Flow Control để ngăn Sender gửi dữ liệu QUÁ NHANH làm tràn bộ đệm nhận (receive buffer) của Receiver.
Receiver công bố kích thước còn trống trong bộ đệm của nó cho Sender thông qua trường **Receive Window (rwnd)** trong TCP header. Sender phải giới hạn lượng dữ liệu đang bay (unacknowledged data) luôn luôn nhỏ hơn hoặc bằng rwnd.

### 3.4.5 Congestion Control (Kiểm soát tắc nghẽn)
Khác với Flow Control (bảo vệ máy nhận), **Congestion Control** bảo vệ TOÀN BỘ MẠNG LƯỚI INTERNET khỏi sự nghẽn cổ chai cục bộ tại các router. Nếu mọi người cùng bơm dữ liệu hết công suất, router nghẽn -> mất gói -> gửi lại -> nghẽn nặng hơn -> Internet sụp đổ.

TCP giải quyết tắc nghẽn thông qua 3 pha chính:
1. **Slow Start (Khởi động chậm):** Bắt đầu gửi chậm (Congestion Window `cwnd` = 1 MSS), nhưng tăng TỐC ĐỘ GẤP ĐÔI (tăng theo cấp số nhân) sau mỗi RTT. Giai đoạn này thực ra không chậm, nó thăm dò tốc độ rất gắt.
2. **Congestion Avoidance (Tránh tắc nghẽn):** Khi `cwnd` đạt đến ngưỡng ssthresh (Slow Start Threshold), tốc độ không nhân đôi nữa mà tăng tuyến tính, cộng 1 MSS cho mỗi RTT để tránh gây ra lỗi mạng đột ngột.
3. **Phát hiện tắc nghẽn và phản ứng:**
   - Nếu xảy ra **Timeout**, đó là sự cố nghiêm trọng. TCP phản ứng mạnh bằng cách tụt ssthresh xuống còn một nửa `cwnd` hiện tại, và ép `cwnd` về 1 MSS. Quay lại pha Slow Start.
   - Nếu xảy ra **3 Duplicate ACKs** (TCP Reno), có vẻ mạng vẫn hoạt động được đôi chút vì gói tin gửi sau vẫn đến đích. TCP giảm một nửa ssthresh, và đưa `cwnd` bằng giá trị ssthresh mới cộng thêm 3 (Fast Recovery), tăng tuyến tính trở lại.

Sự hoạt động của TCP Congestion Control khiến cho đồ thị throughput của nó có hình răng cưa (Saw-tooth behavior) - AIMD (Additive Increase, Multiplicative Decrease).

---
## TÓM TẮT (KEY TAKEAWAYS)
- Tầng giao vận kết nối tiến trình-tiến trình (Process-to-process).
- Multiplexing/Demultiplexing qua IP và Port. UDP dùng 2-tuple, TCP dùng 4-tuple.
- UDP phi kết nối, không tin cậy. Dùng cho Streaming/DNS. Checksum 1s complement.
- RDT giải quyết môi trường lỗi qua: Checksum, ACK, Timer (Timeout), Sequence Number. Kỹ thuật pipelining: Go-Back-N (Ack lũy kế) và Selective Repeat (Ack độc lập).
- TCP thiết lập kết nối 3 bước (SYN, SYNACK, ACK), ngắt 4 bước (FIN). Đánh số thứ tự theo byte stream.
- Fast Retransmit khi có 3 Dup ACKs.
- Flow Control dùng biến rwnd (Window size).
- Congestion Control: Tránh nghẽn router, với 3 trạng thái Slow Start, Congestion Avoidance, Fast Recovery. Hành vi đặc trưng AIMD (Răng cưa).

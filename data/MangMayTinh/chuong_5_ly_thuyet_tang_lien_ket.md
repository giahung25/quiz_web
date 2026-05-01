# CHƯƠNG 5: TẦNG LIÊN KẾT (DATA LINK LAYER) VÀ MẠNG LAN

Nếu tầng Mạng (IP) phụ trách việc tìm đường từ thiết bị A tới thiết bị B xuyên qua toàn bộ Internet, thì **Tầng Liên Kết Dữ Liệu (Link Layer)** chỉ chịu trách nhiệm chuyển dữ liệu (Datagram) từ **một nút mạng sang nút mạng ngay kề cận nó** (như từ PC tới Switch, hoặc từ Switch tới Router) qua một đường liên kết vật lý đơn lẻ (single link).
Đơn vị dữ liệu của tầng này là **Frame (Khung)**.

---

## 5.1 Các dịch vụ của Tầng Liên Kết
1. **Đóng khung (Framing):** Đóng gói IP Datagram vào trong thân một Frame. Header của Frame sẽ chứa thông tin về địa chỉ vật lý nguồn và đích.
2. **Kiểm soát truy cập đường truyền (Link Access):** Nếu nhiều thiết bị cùng sử dụng chung một môi trường truyền thông (như sóng Wi-Fi hoặc một cáp đồng trục chung), giao thức Medium Access Control (MAC) sẽ quy định lúc nào ai được phép phát tín hiệu lên cáp.
3. **Chuyển giao tin cậy (Reliable Delivery):** Cung cấp cơ chế ACK và gửi lại tương tự TCP, nhưng chỉ áp dụng trên từng liên kết (ví dụ trên liên kết Wi-Fi rất hay bị nhiễu). Tuy nhiên, trên liên kết cáp quang hay cáp đồng xoắn (rất ít lỗi), tầng Link thường KHÔNG cung cấp tính năng này để giảm gánh nặng xử lý.
4. **Phát hiện lỗi (Error Detection) và Sửa lỗi (Correction):** Sử dụng các bit kiểm tra lỗi (Parity, CRC) ở cuối Frame để phần cứng bên nhận dò xem tín hiệu điện từ có bị sai lệch bit nào không.

Tầng Link được cài đặt 100% bằng PHẦN CỨNG trên một con chip gọi là **Card mạng (Network Interface Card - NIC)**. Mọi thứ diễn ra ở phần cứng để đạt tốc độ cao nhất.

---

## 5.2 Kỹ thuật Phát hiện và Sửa lỗi (Error-Detection and -Correction)

Khi tín hiệu điện đi qua cáp, nó có thể bị nhiễu lật bit (0 thành 1). Máy nhận cần biết gói tin có bị sai không.
1. **Kiểm tra chẵn lẻ (Parity Checks):**
   - *Đơn chiều:* Thêm 1 bit vào cuối chuỗi dữ liệu sao cho tổng số bit 1 là một số chẵn. Máy nhận đếm số bit 1, nếu ra số lẻ tức là có 1 bit bị lỗi. Không phát hiện được nếu 2 bit cùng lỗi.
   - *Hai chiều (2D Parity):* Sắp dữ liệu thành ma trận, kiểm tra chẵn lẻ theo hàng và cột. Phương pháp này không những phát hiện được lỗi mà còn **chỉ ra chính xác bit nào bị lỗi để tự động SỬA LỖI (FEC - Forward Error Correction)** mà không cần yêu cầu gửi lại.
2. **Tổng kiểm tra (Checksum):** Giống tầng Giao vận (UDP/TCP checksum).
3. **Kiểm tra phần dư tuần hoàn (CRC - Cyclic Redundancy Check):** Rất mạnh và phổ biến trong phần cứng Ethernet. Coi chuỗi bit dữ liệu như một đa thức nhị phân. Chia đa thức này cho một chuỗi bit chuẩn (Generator G), phần dư (remainder) của phép chia chính là mã CRC (thường 32 bit). Bên nhận thực hiện phép chia tương tự, nếu số dư bằng 0 là dữ liệu toàn vẹn.

---

## 5.3 Giao thức Truyền thông Đa truy cập (Multiple Access Protocols)

Khi nhiều máy tính kết nối vào CÙNG MỘT môi trường truyền dẫn (Broadcast link) như cáp đồng trục chung hay sóng Wi-Fi, nếu 2 máy cùng phát tín hiệu cùng lúc, tín hiệu sẽ hòa vào nhau và gây ra **Xung đột (Collision)**. Lẽ dĩ nhiên là cả 2 khung dữ liệu đều hỏng.
Các giao thức Đa truy cập giải quyết bài toán: Phân chia tài nguyên môi trường này như thế nào? Có 3 nhóm chính:

### 5.3.1 Nhóm Chia sẻ Kênh (Channel Partitioning)
- **TDM (Time Division) / FDM (Frequency Division):** Chia nhỏ thời gian hoặc băng tần và cấp cố định cho từng máy. Ưu điểm là công bằng, không bao giờ có xung đột. Nhược điểm là lãng phí: Nếu chỉ có 1 máy cần truyền, nó cũng chỉ được dùng 1 phần băng thông của mình.

### 5.3.2 Nhóm Truy cập Ngẫu nhiên (Random Access)
- Không cấp cố định. Ai có dữ liệu thì cứ phát luôn với tốc độ tối đa của liên kết. Nếu xảy ra xung đột, họ sẽ chờ một khoảng thời gian NGẪU NHIÊN rồi phát lại.
- **ALOHA & Slotted ALOHA:** Các giao thức nguyên thủy. Hiệu suất (Efficiency) rất thấp, chỉ khoảng 18% đến 37% băng thông thực tế được dùng hữu ích.
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):** Dùng trong Ethernet có dây.
  - *Carrier Sense (Nghe trước khi nói):* Máy tính lắng nghe đường truyền. Nếu thấy có sóng (có người đang nói), nó sẽ ĐỢI cho đến khi rảnh mới phát.
  - *Collision Detection (Phát hiện xung đột):* Trong lúc đang phát tín hiệu, thiết bị vẫn liên tục đo lường mức điện áp trên cáp. Nếu điện áp tăng vọt bất thường, nó hiểu là có một thiết bị khác cũng vừa phát tín hiệu dẫn đến va chạm. Nó LẬP TỨC NGỪNG PHÁT để tiết kiệm thời gian (thay vì cố phát hết khung) và gửi tín hiệu Jamming để báo cho mọi người biết.
  - *Binary Exponential Backoff:* Sau khi xung đột, máy tính chọn ngẫu nhiên thời gian chờ từ tập {0, 1, 2, ..., 2^n - 1} lần slot time (với n là số lần xung đột liên tiếp). Nghĩa là càng va chạm nhiều, nó càng lùi lại chờ lâu hơn.
- **CSMA/CA (Collision Avoidance):** Dùng trong Wi-Fi không dây.

### 5.3.3 Nhóm Chuyển lượt (Taking-Turns)
- **Polling (Thăm dò):** Có 1 máy chủ (Master) lần lượt hỏi từng máy con "Bạn có gì cần gửi không?". Khắc phục xung đột, nhưng Master chết thì cả mạng sụp.
- **Token Passing (Chuyển thẻ bài):** Một "thẻ bài" (token) được truyền vòng tròn giữa các máy. Máy nào giữ thẻ bài mới được quyền phát dữ liệu. Không cần Master. Mạng Token Ring từng rất thịnh hành của IBM.

---

## 5.4 Địa chỉ MAC và Giao thức ARP

Trong tầng mạng, chúng ta dùng địa chỉ IP (32 bit, logic, có tính cấu trúc phân cấp).
Trong tầng liên kết, chúng ta dùng địa chỉ vật lý, gọi là **MAC Address (Media Access Control Address)**.
- Địa chỉ MAC có chiều dài **48 bit** (6 bytes), thường được viết dưới dạng hệ thập lục phân, ví dụ: `1A-23-F9-CD-06-9B`.
- Địa chỉ MAC là **Phẳng (Flat)** và **Độc nhất vô nhị (Unique)**. Nó được nhà sản xuất ghi cứng (burned) vào bộ nhớ ROM của con chip Card mạng (NIC). Dù bạn mang laptop từ Việt Nam sang Mỹ, MAC không đổi (nhưng IP sẽ đổi theo mạng Mỹ).
- Giống như IP là địa chỉ nhà/mã bưu chính (chỉ ra khu vực bạn sống), còn MAC là Số chứng minh nhân dân (định danh cơ thể bạn bất kể bạn ở đâu).

### Giao thức phân giải địa chỉ ARP (Address Resolution Protocol)
Khi Máy A cần gửi Datagram cho Máy B (A đã biết IP của B thông qua DNS), nhưng để đóng khung (Frame) ở tầng Liên kết, A BẮT BUỘC phải biết địa chỉ MAC của B. Làm sao để tìm ra?
Giao thức ARP là cầu nối giữa IP và MAC:
1. Máy A kiểm tra **Bảng ARP (ARP Table)** nội bộ xem có mapping của IP B sang MAC chưa.
2. Nếu chưa, Máy A tạo một gói tin **ARP Query**. Gói tin này chứa câu hỏi "Ai có IP x.x.x.x, hãy trả lời gửi MAC cho tôi".
3. A đóng gói tin truy vấn vào một Frame với địa chỉ Đích là **Địa chỉ Broadcast (FF-FF-FF-FF-FF-FF)**. Switch sẽ nhận lệnh này và phát tán (broadcast) frame ra TẤT CẢ các cổng mạng LAN.
4. Mọi máy tính đều nhận được, nhưng chỉ có Máy B (có IP khớp với truy vấn) mới phản hồi bằng một **ARP Response** ghi địa chỉ MAC của nó và gửi đích danh (unicast) lại cho A.
5. A lưu lại vào ARP Table và dùng MAC đó để đóng khung dữ liệu.

*Lưu ý: ARP chỉ hoạt động TRONG PHẠM VI MỘT MẠNG CỤC BỘ (Subnet/LAN). Nếu A muốn gửi gói tin cho C ở một mạng khác, A không tìm MAC của C, mà A sẽ dùng ARP để tìm MAC của Cổng Router mặc định (Default Gateway). Gói tin sẽ được Frame chuyển tới Router.*

---

## 5.5 Mạng Ethernet và Bộ chuyển mạch (Switch)

**Ethernet** là công nghệ mạng cục bộ (LAN) có dây phổ biến nhất thế giới. Nó quy định các chuẩn cáp (như Cáp đồng xoắn đôi 100Base-T, 1000Base-T Gigabit) và cấu trúc Frame.

**Cấu trúc Ethernet Frame:**
- **Preamble (8 bytes):** Các chuỗi bit 101010.. dùng để đồng bộ hóa xung nhịp (clock) giữa máy gửi và nhận.
- **Dest MAC & Source MAC (6 bytes mỗi trường)**
- **Type (2 bytes):** Chỉ định giao thức tầng mạng bên trong thân (thường là IPv4, IPv6, ARP).
- **Data (Payload - 46 đến 1500 bytes):** Kích thước tối thiểu là 46 bytes, tối đa MTU là 1500.
- **CRC (4 bytes):** Kiểm tra lỗi.

Ethernet là công nghệ Phi kết nối (Connectionless) và Không tin cậy (Unreliable - không có ACK/NACK).

### Bộ chuyển mạch Tầng Link (Link-Layer Switch)
Switch là một thiết bị thông minh (plug-and-play), hoạt động ở Tầng 2. Nó có vai trò nhận Ethernet frame ở cổng vào và đẩy (forward) ra cổng ra chính xác tới máy đích. Khác với Hub (một thiết bị ngu ngốc nhân bản tín hiệu điện ra mọi cổng gây xung đột mạng), Switch chia tách các miềm xung đột (collision domains).

**Switch hoạt động ra sao? Nó học (Self-Learning) như thế nào?**
Bên trong Switch có một **Bảng Switch (Switch Table)** dùng để ánh xạ (MAC Address -> Cổng số mấy). Ban đầu bảng này trống rỗng.
1. Khởi động, A gửi khung cho B. Khung vào cổng số 1.
2. **Switch học:** Nó nhìn MAC NGUỒN của khung (là A), và ghi vào bảng: "MAC A nằm ở Cổng số 1".
3. **Switch chuyển tiếp (Forwarding):** Nó nhìn MAC ĐÍCH của khung (là B). Vì chưa biết B ở đâu, nó **Phát tán (Flood)** khung đó ra TẤT CẢ các cổng còn lại (trừ cổng 1).
4. Máy B nhận khung và phản hồi lại A. Khung phản hồi vào cổng 3.
5. Switch lại học: Ghi "MAC B nằm ở Cổng 3". Đồng thời nó thấy MAC đích của khung là A. Nó tra bảng thấy A ở cổng 1, lập tức nó **chỉ đẩy khung ra cổng 1 (Selective Forwarding)** chứ không Flood nữa.

### VLAN (Virtual Local Area Network)
Trong các tổ chức lớn, mạng LAN bị chia nhỏ thành các mạng LAN ảo (VLAN) NGAY TRÊN CÙNG MỘT CƠ SỞ HẠ TẦNG SWITCH VẬT LÝ để dễ quản lý, tăng bảo mật và cô lập lượng truy cập Broadcast. Thiết bị thuộc VLAN kế toán không thể liên lạc trực tiếp với VLAN kỹ thuật dù cắm chung một Switch (phải đi vòng qua Router).
Để nối thông nhiều VLAN qua nhiều Switch với chỉ 1 sợi cáp vật lý (Trunk port), IEEE dùng chuẩn 802.1Q: chèn thêm một VLAN tag (4 bytes) vào Ethernet Frame.

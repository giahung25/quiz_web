# CHƯƠNG 6: MẠNG KHÔNG DÂY VÀ DI ĐỘNG (WIRELESS AND MOBILE NETWORKS)

Sự bùng nổ của máy tính xách tay và điện thoại thông minh đã biến mạng không dây và di động trở thành môi trường kết nối phổ biến nhất hành tinh. Hai khái niệm "Không dây" (Wireless) và "Di động" (Mobility) thường đi chung nhưng chúng là hai khía cạnh khác nhau:
- **Không dây:** Chỉ phương thức kết nối vật lý (sóng điện từ radio) thay vì cáp. Máy tính để bàn có thể dùng Wi-Fi nhưng nó không di chuyển.
- **Di động:** Thiết bị di chuyển từ trạm phát sóng này sang trạm phát sóng khác nhưng vẫn yêu cầu giữ được các kết nối (TCP, cuộc gọi thoại) không bị ngắt.

---

## 6.1 Mạng vô tuyến (Wireless Links) và Các đặc điểm

Trong mạng có dây, tín hiệu điện truyền trong ống cáp bị cô lập tốt. Trong mạng không dây, sóng phát vào không gian tự do, chia sẻ chung một "bầu khí quyển", do đó nó gặp phải nhiều thách thức vật lý hơn:

1. **Giảm thiểu cường độ tín hiệu (Path Loss / Suy hao):** Sóng vô tuyến truyền qua vật chất (tường bê tông, cây cối, khoảng cách) cường độ tín hiệu sẽ bị giảm dần. Ngay cả trong không gian tự do, tín hiệu cũng yếu đi theo tỷ lệ nghịch với bình phương khoảng cách.
2. **Nhiễu từ các nguồn khác (Interference):** Vì mạng không dây dùng chung một số băng tần nhất định (như dải tần ISM 2.4 GHz được dùng cho cả Wi-Fi, Bluetooth và... lò vi sóng), chúng rất dễ bị nhiễu do va chạm với các sóng điện từ khác.
3. **Phản xạ đa đường (Multipath propagation):** Sóng radio khi dội vào trần nhà, tường, vật thể sẽ tách thành nhiều phiên bản truyền theo nhiều quỹ đạo dài ngắn khác nhau. Các bản sao tín hiệu này sẽ đến máy nhận ở các thời điểm hơi chênh lệch, gây ra nhiễu và méo dạng tín hiệu gốc.

**Signal-to-Noise Ratio (SNR) và Bit Error Rate (BER):**
- SNR (Tỉ số tín hiệu trên nhiễu) càng LỚN thì chất lượng tín hiệu càng tốt, người nhận càng dễ trích xuất thông tin gốc.
- BER (Tỷ lệ lỗi bit) là tỷ lệ bit bị sai lệch.
- Mối quan hệ: Khi SNR tăng, BER sẽ giảm.
- Để chống lại BER cao trong môi trường vô tuyến yếu, người ta có thể điều chỉnh kỹ thuật điều chế (Modulation). Nếu mạng tốt, dùng điều chế phức tạp (truyền nhanh). Nếu mạng yếu, thiết bị tự lùi về điều chế cơ bản (chậm nhưng chắc chắn).

### Hiện tượng Terminal ẩn (Hidden Terminal Problem)
Giả sử có máy A, B, C. Trạm phát AP (Access Point) nằm ở B. Cả A và C đều nằm trong tầm sóng của B, nhưng A và C nằm cách xa nhau ngoài tầm của nhau.
- A nghe thấy không có sóng, liền phát gói tin cho B.
- C cũng nghe thấy xung quanh không có sóng (do không nghe được A), C liền phát gói tin cho B.
- Kết quả: Xung đột xảy ra tại B.
Đây là một vấn đề đau đầu trong mạng không dây mà công nghệ CSMA/CD của Ethernet có dây không thể áp dụng được (vì các máy không thể nghe thấy nhau truyền).

---

## 6.2 Wi-Fi: Chuẩn mạng cục bộ không dây (IEEE 802.11)

Wi-Fi (Wireless LAN) là công nghệ kết nối các thiết bị với điểm truy cập (Access Point - AP / Router Wi-Fi) trong phạm vi khoảng vài chục mét. Các chuẩn phổ biến: 802.11b, g, n (chạy ở dải tần 2.4 GHz) và 802.11a, ac, ax (chạy ở dải tần 5 GHz).

### 6.2.1 Kiến trúc 802.11
- Khối xây dựng cơ bản là một **BSS (Basic Service Set)**.
- Một BSS điển hình ở chế độ infrastructure (cơ sở hạ tầng) bao gồm một điểm truy cập trung tâm (AP) và các thiết bị không dây (laptop, điện thoại). AP được nối dây cáp vào một router/switch nối ra Internet.
- Mỗi AP được gắn một mã định danh **SSID (Service Set Identifier)** - chính là cái Tên Mạng Wi-Fi mà bạn tìm thấy trên điện thoại, và một dải tần số liên lạc gọi là **Channel (Kênh)**.

### 6.2.2 Quá trình kết nối: Scanning và Association
Để kết nối vào Wi-Fi, máy tính phải tìm AP:
- **Passive Scanning (Quét thụ động):** AP liên tục phát sóng các gói tin đèn biển (Beacon Frames) đi khắp nơi. Máy tính lắng nghe, nhặt các gói Beacon này để biết có các mạng nào xung quanh.
- **Active Scanning (Quét chủ động):** Trái lại, Máy tính sẽ tự phát đi một gói tin Probe Request. Các AP nhận được sẽ phản hồi lại bằng Probe Response.

Sau khi chọn một mạng, thiết bị thực hiện Xác thực (Authentication) và Liên kết (Association) với AP.

### 6.2.3 Giao thức Truy cập Kênh: CSMA/CA
Vì vấn đề Terminal ẩn, Wi-Fi KHÔNG dùng CSMA/CD. Khi đang phát sóng vô tuyến, thiết bị không thể vừa phát vừa nghe dò va chạm. Thay vào đó nó dùng **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance - Tránh va chạm)**.
- *Nghe trước khi nói:* Nếu kênh rảnh, đợi một chút rồi phát nguyên cả khung dữ liệu (không ngắt giữa chừng).
- *Lùi lại (Backoff):* Nếu kênh đang bận, thiết bị phải chờ bằng cách chọn số đếm lùi ngẫu nhiên.
- *ACK ở tầng Link:* Do không thể tự dò va chạm, thiết bị phát sẽ phát xong và chờ đợi. Nếu máy nhận bắt được gói tin an toàn, nó gửi lại một gói ACK ở tầng Link (điều mà Ethernet không làm). Nếu không thấy ACK, máy phát biết là đã rớt gói và sẽ phát lại.

**Cơ chế RTS / CTS để chống Terminal Ẩn:**
Để giải quyết bài toán A và C cùng lúc đè tín hiệu vào B. Chuẩn 802.11 cung cấp một cơ chế đặt chỗ tùy chọn:
1. Máy A gửi trước một gói tin siêu nhỏ: **RTS (Request to Send)** báo xin phát một khung dữ liệu dài X.
2. Trạm AP B trả lời bằng **CTS (Clear to Send)**. Lệnh CTS này phát rộng ra để cả A và C cùng nghe thấy.
3. Máy C nghe thấy CTS của B, biết rằng B đang dành sóng cho ai đó truyền khung dài X, C sẽ im lặng.
4. Máy A nghe thấy CTS, an tâm gửi cục dữ liệu lớn mà không sợ bị C làm nhiễu.

---

## 6.3 Mạng Di động (Cellular Networks) - 4G/5G

Mạng di động do các nhà viễn thông cung cấp, bao phủ diện tích rộng hàng chục nghìn kilomet vuông.
Từ "Cellular" xuất phát từ việc khu vực địa lý được chia nhỏ thành các "Tế bào" (Cells) hình tổ ong. Mỗi ô tế bào được phục vụ bởi một cột ăng-ten trung tâm gọi là **Base Station (Trạm cơ sở - eNodeB trong 4G LTE)**.

### Cấu trúc 4G LTE
Mạng 4G chia làm hai phần: Mạng truy cập vô tuyến (Radio Access Network) và Mạng lõi (Evolved Packet Core - EPC). Toàn bộ 4G (cả thoại và dữ liệu) đều dựa trên kiến trúc IP (Packet-switched) hoàn toàn.

- **UE (User Equipment):** Điện thoại thông minh, đồng hồ thông minh gắn SIM của bạn.
- **eNodeB:** Trạm thu phát sóng cơ sở. Quản lý việc cấp phát tài nguyên vô tuyến (băng tần, thời gian) cho các điện thoại trong ô sóng đó.
- **SGW (Serving Gateway) và PGW (PDN Gateway):** SGW chịu trách nhiệm định tuyến gói tin dữ liệu trong khu vực, PGW là ranh giới gateway kết nối từ mạng di động ra ngoài Internet toàn cầu (làm cả việc NAT địa chỉ IP cho điện thoại).
- **MME (Mobility Management Entity):** Trung tâm não bộ điều khiển. Đóng vai trò là Control Plane. Nó xác thực người dùng (SIM), và theo dõi vị trí của điện thoại để nếu bạn di chuyển, nó biết để điều phối cuộc gọi.
- **HSS (Home Subscriber Server):** Cơ sở dữ liệu chứa thông tin các SIM, hồ sơ thanh toán của khách hàng.

---

## 6.4 Quản lý Di động (Mobility Management)

Khi bạn ngồi trên ô tô tốc độ cao, vừa xem YouTube vừa di chuyển từ thành phố này sang thành phố khác. Mạng làm thế nào để gói tin YouTube vẫn tìm được bạn, dù bạn đã rời khỏi cột sóng cũ?

**Vị trí của thiết bị:**
- **Home Network (Mạng nhà):** Là mạng mà SIM của bạn đăng ký. Ví dụ Viettel Hà Nội.
- **Home Agent (Đại diện nhà):** Một thực thể ở mạng nhà (thường là router/gateway) lưu giữ thông tin định vị của bạn.
- **Visited Network / Foreign Network (Mạng khách):** Nếu bạn đi công tác vào TP.HCM, điện thoại kết nối trạm Viettel HCM, đây là mạng khách. Trạm đang phục vụ bạn gọi là Foreign Agent.
- **Care-of Address (COA):** Khi đến mạng khách, thiết bị của bạn được cấp một địa chỉ IP tạm thời mới gọi là COA.

**Cách định tuyến tới Mobile Node (Định tuyến gián tiếp):**
1. Một Correspondent (Người gửi) ở xa muốn gửi tin nhắn cho bạn. Nó gửi tới địa chỉ IP CỐ ĐỊNH (Permanent IP) của bạn ở mạng nhà (Hà Nội).
2. Gói tin đi tới mạng nhà, **Home Agent** ở mạng nhà tóm lấy gói tin này.
3. Bằng cách nào đó, Home Agent đã biết địa chỉ tạm trú COA hiện tại của bạn ở HCM. Nó nhét gói tin gốc vào một lớp IP thứ 2 (Tunneling) có địa chỉ đích là COA, và ném xuống phương Nam.
4. Gói tin tới mạng khách, Foreign Agent lột lớp vỏ hầm (decapsulation) và giao gói tin gốc cho điện thoại bạn.

**Handover / Handoff (Chuyển giao sóng):**
Khi bạn lái xe, điện thoại ra khỏi vùng phủ sóng của trạm eNodeB số 1 và vào vùng trạm eNodeB số 2.
- Điện thoại của bạn liên tục đo cường độ sóng. Khi nó thấy sóng trạm 2 mạnh hơn trạm 1, nó báo cho trạm 1.
- Trạm 1 chủ động giao tiếp với trạm 2, dọn đường và bàn giao quản lý (Handover) chiếc điện thoại này sang cho trạm 2 mà không làm rớt mạng. Tốc độ chuyển giao chỉ trong vài chục miligiây.

---
## TÓM TẮT (KEY TAKEAWAYS)
- Vô tuyến có suy hao (path loss), nhiễu và dội sóng đa đường. SNR quyết định BER.
- Bài toán Terminal ẩn là vấn đề hai máy khuất tầm nhìn cùng phát làm hỏng sóng trạm giữa. Giải bằng RTS/CTS.
- Wi-Fi (802.11) dùng CSMA/CA, phát beacon quét sóng.
- 4G LTE kiến trúc ALL-IP. Cột sóng gọi là eNodeB, MME điều khiển di động, PGW nối ra Internet.
- Quản lý di động dùng cấu trúc mạng nhà (Home agent) chuyển hầm (tunneling) gói tin đến mạng khách (COA).
- Quá trình đi từ trạm sóng này sang trạm khác là Handover.

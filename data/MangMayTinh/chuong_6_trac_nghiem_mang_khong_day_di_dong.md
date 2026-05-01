# CHƯƠNG 6: TRẮC NGHIỆM MẠNG KHÔNG DÂY VÀ DI ĐỘNG

**Câu 1:** Một trong những khác biệt vật lý lớn nhất làm suy giảm tín hiệu của đường truyền không dây so với cáp quang hoặc cáp đồng là gì?
A. Tín hiệu bị đóng băng do nhiệt độ không gian tự do.
B. Cường độ tín hiệu bị suy giảm rất nhanh theo bình phương khoảng cách (Path loss) và bị hấp thụ/phản xạ bởi các chướng ngại vật trên đường đi.
C. Sóng điện từ không thể mang theo tín hiệu nhị phân.
D. Sóng vô tuyến không thể đi qua vùng có ánh sáng mạnh.
*Đáp án: B*
*Giải thích: Môi trường vô tuyến là không gian mở (unguided media). Sóng lan tỏa mọi hướng làm năng lượng suy hao nhanh, đồng thời tường bê tông, cây cối hấp thụ năng lượng sóng.*

**Câu 2:** Tỉ số SNR (Signal-to-Noise Ratio) trong truyền thông không dây được dùng để đánh giá yếu tố nào?
A. Đo lường kích thước địa chỉ IP.
B. Đo lường tỷ lệ giữa sức mạnh của Tín hiệu thu được so với năng lượng của Nhiễu nền môi trường. SNR càng CAO thì chất lượng tín hiệu càng tốt.
C. Đo tỷ lệ lỗi bit (BER) sinh ra trên cáp.
D. Tính toán tốc độ ánh sáng trong môi trường mạng.
*Đáp án: B*
*Giải thích: Nếu Tín hiệu (Signal) bị Nhiễu (Noise) lấn át (tức SNR thấp), máy nhận sẽ không thể phân biệt nổi số 0 và số 1, dẫn đến Lỗi bit (BER) tăng vọt.*

**Câu 3:** Hiện tượng "Multipath propagation" (Lan truyền đa đường) gây méo tín hiệu vô tuyến xuất phát từ nguyên nhân nào?
A. Do trạm phát phát cùng lúc quá nhiều tần số khác nhau.
B. Do sóng điện từ phản xạ và dội vào các bề mặt (tường, tòa nhà, mặt đất) tạo ra nhiều tia sóng đi theo nhiều quỹ đạo có độ dài khác nhau, và tới ăng-ten nhận ở các thời điểm hơi lệch nhau.
C. Do các thiết bị ở gần nhau phát tín hiệu cùng một lúc.
D. Do nhà mạng đặt các trạm (cell) quá gần nhau.
*Đáp án: B*
*Giải thích: Giống như tiếng vang (echo) trong phòng kín. Tia phản xạ đi xa hơn nên tới muộn hơn tia trực tiếp, chúng dội vào nhau làm nhòe tín hiệu gốc tại bộ thu.*

**Câu 4:** Vấn đề "Hidden Terminal" (Terminal ẩn) trong mạng không dây mô tả nghịch lý nào sau đây?
A. Kẻ tấn công ẩn giấu trong mạng Wi-Fi không hiện tên để nghe lén.
B. Thiết bị di động nằm ở góc chết không tìm thấy điểm phát sóng (AP).
C. Hai máy tính (A và C) không nghe thấy nhau do cách xa nhau hoặc bị cản trở, nhưng chúng cùng nằm trong tầm phủ sóng của một máy chủ AP (B). Cả hai cùng phát sóng tới B vì lầm tưởng kênh đang rảnh, gây ra xung đột tại B.
D. Điểm truy cập tự động ẩn SSID để không ai tìm thấy.
*Đáp án: C*
*Giải thích: A "nghe" kênh rảnh nên A phát cho B. C ở bên kia dãy núi cũng "nghe" kênh rảnh nên C phát cho B. Cả 2 luồng sóng đâm vào nhau tại B khiến B không đọc được khung nào. Ethernet có dây không hề gặp lỗi này.*

**Câu 5:** Vì bài toán Terminal ẩn, chuẩn Wi-Fi (IEEE 802.11) đã thay thế công nghệ CSMA/CD của Ethernet bằng giao thức gì?
A. Token Ring
B. ALOHA
C. TDM
D. CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
*Đáp án: D*
*Giải thích: Phần cứng vô tuyến không thể vừa phát mạnh vừa nghe yếu để phát hiện va chạm (CD). Nó phải đổi sang chiến thuật Tránh Va chạm (CA) bằng cách chờ đợi.*

**Câu 6:** Trong CSMA/CA của Wi-Fi, khi thiết bị muốn phát nhưng thấy sóng (kênh) đang BẬN, quá trình đếm ngược thời gian lùi lại ngẫu nhiên (Backoff) có đặc điểm thông minh nào?
A. Đếm ngược liên tục không ngừng cho đến 0.
B. Quá trình đếm ngược sẽ TẠM DỪNG (Freeze) (đóng băng) lại ngay khi nó nghe thấy kênh bị bận bởi một máy khác. Khi kênh rảnh rỗi, nó mới tiếp tục đếm phần còn lại.
C. Tăng gấp đôi bộ đếm thời gian.
D. Xóa bỏ gói tin để truyền gói khác.
*Đáp án: B*
*Giải thích: Đóng băng bộ đếm giúp các máy đã chờ lâu được ưu tiên phát sóng ngay khi mạng rảnh, đảm bảo công bằng (fairness) giữa các máy trạm.*

**Câu 7:** Cơ chế kiểm soát luồng phụ trợ RTS/CTS trong Wi-Fi được sinh ra để triệt tiêu trực tiếp vấn đề gì?
A. Bẻ khóa mật khẩu WEP.
B. Giải quyết bài toán Terminal Ẩn bằng cách gửi các khung điều khiển siêu nhỏ (đặt chỗ) trước khi truyền cục dữ liệu khổng lồ.
C. Mã hóa tín hiệu mạng 4G.
D. Giới hạn dải tần số 5 GHz.
*Đáp án: B*
*Giải thích: RTS (Xin phát) và CTS (Đồng ý phát) đóng vai trò dọn đường. Khung CTS được AP la lớn cho tất cả mọi máy quanh nó (kể cả máy ẩn) nghe thấy và phải câm lặng để nhường đường cho máy xin phát.*

**Câu 8:** Vì sao giao thức Wi-Fi 802.11 lại thiết kế thêm việc gửi gói tin Báo nhận (ACK) ngay tại Tầng Liên kết (Data Link), điều mà Ethernet có dây không hề làm?
A. Vì Wi-Fi không hoạt động cùng với TCP.
B. Để lấy thông tin tính tiền cước dữ liệu cục bộ.
C. Vì tỷ lệ lỗi (BER) và đụng độ trên kênh không dây rất cao. Bằng cách dùng ACK ngay tại phần cứng Wi-Fi, thiết bị có thể chủ động truyền lại tức thì nếu rớt gói, thay vì để Tầng giao vận (TCP) chờ Timeout rất tốn thời gian.
D. Để mã hóa bảo mật chuẩn WPA3.
*Đáp án: C*
*Giải thích: Gửi qua sóng radio thì "rớt gói" là cơm bữa. Việc Sửa Lỗi Cục Bộ tại mức Link layer giúp TCP ở trên vẫn có ảo giác đường truyền ổn định.*

**Câu 9:** Để máy tính/điện thoại quét tìm các điểm phát Wi-Fi (AP) xung quanh để kết nối, nó dựa vào loại khung dữ liệu nào do AP định kỳ phát ra?
A. Data frames
B. RTS frames
C. Beacon frames (Gói đèn biển)
D. ARP Request
*Đáp án: C*
*Giải thích: Passive Scanning (Quét thụ động). Trạm AP cứ mỗi 100ms lại phát tán một Beacon chứa SSID và thông số MAC của nó để "chào hàng" tới các máy tính trong bán kính.*

**Câu 10:** Kiến trúc của Mạng di động 4G LTE khác với các thế hệ viễn thông 2G/3G tiền nhiệm ở điểm đột phá nào?
A. Vẫn duy trì hệ thống chuyển mạch kênh cồng kềnh cho các cuộc gọi thoại thông thường.
B. Thiết lập một kiến trúc All-IP (Packet-switched 100%), mọi luồng dữ liệu kể cả các cuộc gọi thoại (VoLTE) đều được chuyển thành các gói tin IP truyền qua mạng dữ liệu.
C. Sử dụng sóng Wi-Fi thay cho trạm anten.
D. Loại bỏ thẻ SIM ra khỏi điện thoại.
*Đáp án: B*
*Giải thích: Sự thay đổi này thống nhất cấu trúc lõi mạng với Internet, biến nhà mạng viễn thông trở thành những cỗ máy định tuyến IP khổng lồ.*

**Câu 11:** Trạm thu phát sóng trực tiếp kết nối với điện thoại di động trong ô sóng 4G LTE được gọi bằng thuật ngữ kỹ thuật nào?
A. Access Point (AP)
B. BSS
C. eNodeB (Evolved Node B)
D. HSS
*Đáp án: C*
*Giải thích: eNodeB quản lý vùng không gian vô tuyến. Đảm nhận lịch trình truyền cho hàng ngàn điện thoại di động bằng tài nguyên thời gian và tần số.*

**Câu 12:** Trong Mạng lõi di động (EPC - Evolved Packet Core) của 4G, bộ phận nào nắm vai trò Não bộ Điều khiển (Control Plane), quản lý xác thực điện thoại và theo dõi vị trí di chuyển?
A. PGW (Packet Data Network Gateway)
B. SGW (Serving Gateway)
C. MME (Mobility Management Entity)
D. eNodeB
*Đáp án: C*
*Giải thích: MME là một bộ não thuần túy. Nó không vận chuyển dữ liệu video/web của bạn (đó là việc của Data plane SGW/PGW). Nó chỉ lo định vị bạn đang ở trạm nào để điều phối cuộc gọi.*

**Câu 13:** Cổng Gateway giáp ranh kết nối mạng di động của nhà mạng ra Internet toàn cầu (điểm thực hiện gán IP cho điện thoại) gọi là gì?
A. HSS
B. PGW (PDN Gateway)
C. MME
D. Router BGP
*Đáp án: B*
*Giải thích: PGW là cái phễu cuối cùng. Mọi dữ liệu điện thoại đi vào Internet đều phải lọt qua PGW.*

**Câu 14:** Khi bạn mang điện thoại từ mạng Viettel Hà Nội (Home Network) đi du lịch vào Mạng Viettel TP.HCM hoặc sang Mạng Mỹ (Visited Network), Mạng khách sẽ cấp cho bạn một cái địa chỉ IP tạm thời để giao tiếp. Tên của nó là gì?
A. Permanent IP (IP cố định)
B. MAC Address
C. IPv6
D. Care-of Address (COA - Địa chỉ tạm trú)
*Đáp án: D*
*Giải thích: COA là số nhà tạm bợ để mạng khách biết đường giao gói tin tới cho bạn khi bạn đang lang thang trong địa bàn của họ.*

**Câu 15:** Trong cơ chế quản lý Di động, quá trình Định tuyến Gián tiếp (Indirect Routing) giải quyết việc chuyển một tin nhắn từ Internet tới cái điện thoại đang đi du lịch bằng bước nào sau đây?
A. Lên Google tra địa chỉ của mạng khách và gửi thẳng.
B. Phát Broadcast ra toàn cầu chờ điện thoại nhận lấy.
C. Gửi tin nhắn đến cái IP cố định ở Mạng Nhà. Thiết bị Home Agent tại Mạng Nhà sẽ bắt lấy, nén nguyên khối tin nhắn đó vào một Đường hầm IP (Tunneling) và nhắm thẳng địa chỉ tạm trú (COA) ở Mạng Khách để bắn đi.
D. Trả về lỗi không tìm thấy (Destination unreachable).
*Đáp án: C*
*Giải thích: Mạng nhà đóng vai người giao liên. Người gửi ngoài Internet không hề biết điện thoại đang ở Mỹ, họ cứ gửi thư về Hà Nội, Hà Nội sẽ bọc thư lại gửi hỏa tốc sang Mỹ theo địa chỉ COA.*

**Câu 16:** Sự kiện "Handover" (Handoff / Chuyển giao) trong mạng di động xảy ra khi nào?
A. Khi thuê bao trả trước nạp thêm tiền vào tài khoản.
B. Khi thuê bao ngắt chế độ Máy bay.
C. Khi điện thoại di động di chuyển vượt ra ranh giới sóng của trạm eNodeB cũ và đi vào vùng của một trạm eNodeB mới. Hệ thống sẽ tự động hoán đổi luồng kết nối sang trạm mới cực nhanh mà không làm đứt cuộc gọi/video.
D. Khi kết nối Wi-Fi ở nhà bị rớt.
*Đáp án: C*
*Giải thích: Nhờ tính toán cường độ sóng báo cáo từ điện thoại, eNodeB cũ sẽ đàm phán với eNodeB mới trải thảm đỏ mời điện thoại sang, đồng thời forward nốt gói tin thừa sang trạm mới.*

**Câu 17:** Khung dữ liệu (Frame) của chuẩn Wi-Fi 802.11 phức tạp hơn khung của chuẩn Ethernet 802.3 ở điểm nào rõ rệt nhất?
A. Không sử dụng mã kiểm tra lỗi CRC.
B. Có tới tận 4 trường địa chỉ MAC (Address 1, 2, 3, 4) thay vì chỉ có 2 trường (Source/Dest MAC) như Ethernet, nhằm phục vụ việc chuyển giao khung từ điện thoại -> AP không dây -> Router mạng có dây.
C. Có chứa mã hóa RSA.
D. Độ dài phần tải (payload) bắt buộc phải lớn hơn 1500 bytes.
*Đáp án: B*
*Giải thích: Do AP làm cầu nối giữa môi trường vô tuyến và có dây, khung Wi-Fi phải mang địa chỉ đích cuối, địa chỉ gốc, địa chỉ AP thu và địa chỉ AP phát.*

**Câu 18:** Hiện tượng SNR (Signal-to-Noise Ratio) tụt dốc thê thảm sẽ trực tiếp gây ra điều gì?
A. Làm tăng băng thông của kết nối.
B. Làm cho trạm AP bị hỏng.
C. Khiến cho tỷ lệ Lỗi Bit (BER - Bit Error Rate) tăng vọt, vì máy thu không thể phân biệt nổi tín hiệu gốc lẫn trong đám nhiễu ồn ào.
D. Tăng khoảng cách kết nối.
*Đáp án: C*
*Giải thích: SNR thấp tức là "nhiễu" ồn hơn "tín hiệu", giống như cố gắng nghe bạn bè thì thầm giữa sân vận động đang bật nhạc xập xình. Bạn sẽ nghe nhầm chữ (Lỗi Bit).*

**Câu 19:** Để đối phó với hiện tượng tín hiệu sóng (SNR) thay đổi liên tục khi người dùng đi xa hoặc đi gần lại bộ phát Wi-Fi/4G, thiết bị áp dụng kỹ thuật tự động gì?
A. Kỹ thuật thích ứng Tốc độ / Điều chế (Rate/Modulation Adaptation): Khi sóng khỏe, dùng kỹ thuật điều chế bậc cao (ví dụ QAM-64) để truyền rất nhanh. Khi sóng yếu (đi xa), tự động lùi về điều chế cơ bản (ví dụ BPSK) chậm nhưng chống lỗi tốt.
B. Kỹ thuật thay đổi IP liên tục.
C. Kỹ thuật giảm ánh sáng màn hình điện thoại.
D. Kỹ thuật tắt luồng gửi gói tin ACK.
*Đáp án: A*
*Giải thích: Thấy sóng yếu, điện thoại phải nói "chậm rãi, rõ ràng từng chữ" (tốc độ Mbps bị giảm thê thảm). Sóng mạnh, nó sẽ "nói liến thoắng" (tốc độ vọt lên Gigabit).*

**Câu 20:** Active Scanning (Quét chủ động) trong mạng Wi-Fi đòi hỏi máy khách (Client) phải phát đi loại thông điệp nào để dò tìm mạng?
A. Beacon Frame
B. CTS Frame
C. Probe Request Frame (Khung yêu cầu dò tìm) phát quảng bá. Mọi AP nghe thấy sẽ gửi lại Probe Response Frame trả lời.
D. ARP Request
*Đáp án: C*
*Giải thích: Thay vì ngồi thụ động nhặt Beacon từ AP rớt xuống, Active scanning ép điện thoại phải la lên "Có ai ở quanh đây không?" để các AP đồng loạt xưng tên.*

**Câu 21:** Chuẩn mạng không dây nào của cá nhân (Personal Area Network - PAN) có tầm phủ sóng rất ngắn, chủ yếu dùng để kết nối chuột, tai nghe, thiết bị đeo thông minh?
A. Wi-Fi (802.11ax)
B. Bluetooth (IEEE 802.15.1)
C. 4G LTE
D. Fiber-optics
*Đáp án: B*
*Giải thích: Bluetooth hay Zigbee thuộc nhóm mạng tầm ngắn (vài mét) tiêu thụ năng lượng cực thấp dành cho thiết bị cá nhân và IoT.*

**Câu 22:** Ở phía Mạng nhà (Home Network) của một thuê bao di động, thiết bị HSS (Home Subscriber Server) có vai trò tương đương với gì?
A. Tổng đài điện thoại.
B. Một cơ sở dữ liệu (Database) khổng lồ chứa hồ sơ khách hàng, chìa khóa mật mã xác thực (SIM) và thông tin vị trí của toàn bộ thuê bao thuộc nhà mạng đó.
C. Bộ định tuyến quang học.
D. Thiết bị khuếch đại sóng.
*Đáp án: B*
*Giải thích: HSS là hồ sơ lý lịch. Khi bạn đăng nhập vào 4G, MME sẽ lôi hồ sơ của bạn từ HSS ra xem bạn có nợ cước không, khóa bí mật của SIM là gì.*

**Câu 23:** Trạng thái "Sleep" (Ngủ) của các thiết bị Wi-Fi có tác dụng lớn nhất là gì?
A. Tăng băng thông khi thức dậy.
B. Tiết kiệm năng lượng (Pin) cho thiết bị di động bằng cách tắt phần cứng vô tuyến. Thiết bị hẹn giờ thức dậy đúng lúc AP phát Beacon để nghe xem có dữ liệu gửi cho mình hay không.
C. Chống lại cuộc tấn công DoS.
D. Bảo vệ màn hình máy tính.
*Đáp án: B*
*Giải thích: Pin là sinh mệnh của điện thoại. Phần cứng dò sóng ăn điện rất ác. Power management giúp điện thoại ngủ 90% thời gian.*

**Câu 24:** Mạng vô tuyến sử dụng Dải tần số ISM (Industrial, Scientific, Medical) như 2.4 GHz gặp rủi ro gì lớn nhất?
A. Tần số này không thể truyền thông tin.
B. Vì đây là dải tần miễn phí, nó bị sử dụng bởi hàng đống công nghệ tạp nham từ Wi-Fi, Bluetooth, Zigbee cho đến bức xạ của Lò vi sóng, nên MỨC ĐỘ NHIỄU (Interference) rất kinh khủng.
C. Bị nhà mạng tính phí rất cao.
D. Sóng 2.4 GHz không đi xuyên qua được kính cửa sổ.
*Đáp án: B*
*Giải thích: Băng tần 2.4GHz là một "khu chợ chồm hổm" vô tuyến do không cần giấy phép. Đó là lý do chuẩn 5GHz ra đời để có môi trường sạch sẽ hơn (dù xuyên tường kém hơn).*

**Câu 25:** Nhược điểm của cơ chế Direct Routing (Định tuyến trực tiếp) trong việc quản lý thiết bị di động là gì?
A. Người gửi phải đóng gói bằng Tunneling.
B. Nếu thiết bị di động đi ô tô tốc độ cao và thay đổi Mạng khách (Visited Network) liên tục, luồng dữ liệu truyền thẳng từ Người gửi đến COA sẽ bị gãy giữa chừng vì Người gửi gặp khó khăn trong việc cập nhật địa chỉ COA mới liên tục.
C. Quá chậm so với định tuyến gián tiếp.
D. Tốn phí của nhà mạng.
*Đáp án: B*
*Giải thích: Định tuyến trực tiếp tiết kiệm đường đi (không phải vòng về Mạng Nhà). Nhưng bù lại độ trễ chuyển giao handover lớn vì bắt người gửi (đang ở đầu kia Trái đất) phải cập nhật lại luồng tin.*

**Câu 26:** 5G đem lại những cải tiến kỹ thuật nổi trội nào so với 4G?
A. Chuyển trở lại dùng cáp đồng.
B. Loại bỏ giao thức IP.
C. Tốc độ Gigabit ở sóng mmWave, tăng cường mật độ thiết bị khổng lồ cho IoT, và Mạng lõi được Ảo hóa/Phân chia (Network Slicing) tạo ra các mạng riêng biệt tùy theo nhu cầu dịch vụ.
D. Tăng khoảng cách phát sóng của eNodeB lên hàng ngàn kilomet.
*Đáp án: C*
*Giải thích: 5G không chỉ là "Internet nhanh hơn", mà nó được thiết kế cho xe tự lái (trễ siêu thấp) và IoT (hàng triệu cảm biến). Network slicing cắt hạ tầng ảo ra cho từng nhu cầu.*

**Câu 27:** Trong một khung MAC Wi-Fi (802.11), trường "Duration" (Thời lượng) được gài vào để làm gì?
A. Định giờ hẹn tắt máy.
B. Chứa thời lượng của bộ phim đang xem.
C. Để các máy khác "nghe lỏm" được biết là quá trình truyền khung này (cộng thêm khung ACK) sẽ kéo dài trong bao nhiêu micro-giây, từ đó chúng cài đặt bộ đếm NAV (Network Allocation Vector) và im lặng ngủ chờ cho rảnh kênh.
D. Hiển thị độ bền của thiết bị.
*Đáp án: C*
*Giải thích: Khung Wi-Fi la lên: "Tôi cần 50ms để truyền và nhận cục này". Mọi máy nghe thấy liền tự lấy băng dính dán mồm mình lại trong 50ms (NAV).*

**Câu 28:** Đâu KHÔNG phải là một chuẩn do IEEE quy định cho mạng Không dây (Wireless LAN)?
A. 802.11b
B. 802.11g
C. 802.3 Ethernet
D. 802.11ac (Wi-Fi 5)
*Đáp án: C*
*Giải thích: 802.3 là tiêu chuẩn gia đình dành riêng cho Cáp đồng và Cáp quang có dây (Ethernet).*

**Câu 29:** Nếu một thiết bị gửi dữ liệu qua một liên kết vô tuyến mà phát hiện tỷ lệ lỗi quá cao, tầng liên kết của thiết bị đó sẽ dùng công cụ tự động nào thay vì để tầng TCP lo liệu?
A. Chuyển đổi mã hóa RSA.
B. Gửi cờ SYN lên router.
C. Dùng cơ chế ARQ (Automatic Repeat reQuest) ở tầng Liên kết (Data Link Layer) để yêu cầu máy nhận xác nhận ACK cục bộ và tự truyền lại khung bị lỗi ngay trên không trung.
D. Format lại ổ cứng.
*Đáp án: C*
*Giải thích: ARQ tầng Link giúp khắc phục lỗi ngay tại chiến trường vô tuyến đầy nhiễu loạn trước khi rác rến bị đẩy lên các tầng cao hơn.*

**Câu 30:** Thiết kế "Ô hình Lục giác (Tổ ong)" trong mạng Cellular có lợi ích lý thuyết nào?
A. Làm cột sóng dễ xây hơn.
B. Phủ kín hoàn toàn mặt phẳng địa lý không để lại các góc chết, đồng thời cho phép Tái sử dụng Tần số (Frequency Reuse) ở các ô cách xa nhau để tiết kiệm băng tần đắt đỏ.
C. Cho phép sóng truyền qua bê tông 100%.
D. Xóa bỏ hoàn toàn hiện tượng nhiễu.
*Đáp án: B*
*Giải thích: Ô hình lục giác (tổ ong) là mô hình toán học hoàn hảo nhất để tối ưu diện tích phát sóng. Ô số 1 xài băng tần X thì ô số 3 ở xa cũng có thể tái xài băng tần X mà không bị nhiễu.*

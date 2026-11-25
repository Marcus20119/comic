# Mẫu `prompts.md` — Commit Trái Tim

Dùng tài liệu này để **soạn** một file hoàn chỉnh cho từng chap mới, không gửi nguyên mẫu còn placeholder cho Go. Đọc [storyline](story-outline.md), [outfit](outfit.md) và [chỉ đạo manga](manga-direction.md) trước. File duy nhất để sản xuất chap là `episodes/ep-NNN/prompts.md`; mỗi khối bên trong phải copy được. Không nhờ Go đọc đường dẫn local hay nhớ session trước.

## 00 — Mở session: toàn bộ ngữ cảnh chap

Mở một session mới. Gửi **một khối ngữ cảnh hoàn chỉnh** kèm 6 ảnh theo tên `01`–`06` trong [Go pack](assets/reference/go-pack/). Chép chú giải ảnh vào khối 00; khi chuyển link vào file chap, đường dẫn bắt đầu bằng `../../assets/reference/go-pack/`.

| Ảnh | Đính kèm | Vai trò tại chỗ |
| --- | --- | --- |
| 01 | [Comic art guide](assets/reference/go-pack/01-comic-art-style-guide.png) | Nét manga, màu, ánh sáng, cách tạo khối; không sao chép cảnh hay chữ. |
| 02 | [Lettering guide](assets/reference/go-pack/02-lettering-style-guide.png) | Thoại, Dẫn truyện, Suy nghĩ và SFX; không dùng để nhận diện. |
| 03 | [Mặt bằng văn phòng IT](assets/reference/go-pack/03-it-office-floor-plan.png) | Tương quan phòng, cửa, bàn, pantry; không tái vẽ sơ đồ hay nhãn. |
| 04 | [Lineup chính](assets/reference/go-pack/04-office-lineup-phong-dung-dat.png) | Trái Phong (tóc nâu đỏ, không kính), giữa Dũng (tóc sẫm ngắn, vai rộng, không kính), phải Đạt (tóc sẫm rối, kính chữ nhật). Khóa mặt, tóc và vóc dáng, không khóa đồ ngày mới. |
| 05 | [Thảo–Nhi–Trân](assets/reference/go-pack/05-thao-nhi-tran.png) | Trái Thảo, giữa Nhi, phải Trân. |
| 06 | [Khang–Minh–Nam](assets/reference/go-pack/06-khang-minh-nam.png) | Trái Khang, giữa Minh, phải Nam. |

```text
Bạn đang chuẩn bị [tên hiển thị, số chap và tựa]. Đây là lượt nạp ngữ cảnh, CHƯA tạo ảnh.

Ảnh đính kèm: [tên file và vai trò 01–06; vị trí nhân vật theo góc người xem]. Sheet outfit sẽ đến sau; sheet khóa quần áo, còn ảnh gốc khóa nhận diện. Chỉ vẽ người được gọi ở mỗi cảnh.

Điểm vào: [sự kiện từ chap trước, điều từng người biết và chi tiết chưa lộ].
Nội dung toàn chap: [kể đủ mở đầu, từng cảnh theo thứ tự, ngày/giờ hoặc mốc chuyển, ai có mặt, điều họ muốn, và mỗi cảnh kết thúc ra sao].
Phân trang: [phạm vi pXX theo cảnh, mối nối giữa cảnh; nêu trang chốt và ending hook cụ thể].
Không vượt mạch: [chi tiết bắt buộc và điều Go không tự thêm/đổi, mốc tình cảm chưa đến].
Giữ xuyên chap: [địa điểm, đạo cụ và trạng thái outfit; giọng, xưng hô, độ thân mật và cách trình bày chữ].
Cách xuất: [khổ 4:5, đúng số trang truyện dưới 20, một ảnh mỗi lượt, thoại tiếng Việt theo nguyên văn từng page]. Chờ mục 01 thiết kế outfit.
```

## 01 — Thiết kế outfit cho đúng chap

Prompt đứng riêng, gửi sau mục 00. Tra chương tương ứng trong `outfit.md`; không đưa ID trần rồi yêu cầu Go đoán. Ghi đủ người có mặt, mã, áo/quần hoặc váy, màu/fit, giày, phụ kiện; tách theo ngày/hoạt động khi thật sự thay. Nếu chap tiếp nối cùng ngày thì tái hiện đúng bộ đã khóa, không thiết kế đồ mới. Không buộc cả team lên trang truyện chỉ vì sheet có đủ người.

```text
Tạo [một sheet trang phục ngang, hoặc các sheet theo mốc đã ghi], nền trung tính, từng người nguyên người và không chồng lên nhau. Từng ô: [vị trí, nhân vật, ảnh nhận diện, mã outfit, ngày/cảnh, mô tả đủ]. Giữ đúng mặt, tóc, màu da, kính và tỷ lệ. Chỉ tạo quần áo đúng thiết kế; không thêm logo, nhãn, chữ hay phụ kiện lạ.
```

Chọn sheet đúng, lưu `art/wardrobe.png` (nhiều mốc thì dùng tên mô tả đã ghi trong `prompts.md`) rồi đính lại sau ảnh 06. Soạn luôn câu khóa: “Ảnh 07 là [tên sheet], [vị trí từng người và mã bộ]. Chỉ áp vào [mốc/page], ảnh 04–06 vẫn khóa nhận diện.” Thêm chú thích tương đương nếu có ảnh outfit thứ hai. Khi Go lẫn context, đính lại đúng tên ảnh kèm chú giải, không tự đổi thứ tự.

## 02 — Bìa (`art/cover.png`)

Một ảnh dọc 4:5, không chia panel. Nêu ý bìa, nhân vật thực sự có mặt, outfit đúng mốc, vị trí trước/sau, điểm nhìn, biểu cảm theo tình huống và vùng đặt chữ. Ghi nguyên văn tên series hiển thị, số chap, tựa chap. Không dùng bìa để kể hộ cú lật cuối chap. Nêu rõ chỉ tạo bìa, chưa tạo recap hay trang truyện.

## 03 — Tập trước (`art/recap.png`)

Một ảnh dọc 4:5 đặt sau bìa, trước p01, không tính vào pXX. Ghi trực tiếp một đoạn ngắn về **chap đã xảy ra** dựa trên bản đã làm, không trỏ sang `recap.md` và không tiết lộ chap mới. Khối văn bản căn trái bên trong, đặt giữa trang, nền đủ sáng để đọc; không panel hay bong bóng. Dùng mẫu **Dẫn truyện** ở ảnh 02, tiêu đề “Tập trước” cùng kiểu và chỉ nhỉnh hơn thân bài; ưu tiên chữ thay vì phóng tiêu đề. Hình điểm xuyết nhỏ là tùy chọn, ngoài vùng chữ; nếu có nhân vật phải dùng outfit chap cũ, không lấy sheet chap mới. Nếu cần khớp font tuyệt đối, cho phép gen bản nền và đặt chữ thủ công từ đoạn đã khóa trong prompt.

## 04 — Từng page (`art/p01.png`… tối đa `art/p19.png`)

Một tiêu đề và một khối hoàn chỉnh cho mỗi ID. Bố cục đi theo nội dung: thêm panel để tách lượt đáp hoặc bước việc, giảm panel để giữ ánh nhìn hoặc khung cảnh quan trọng. Ghi rõ khi nào có chữ, khi nào cần sạch. Đừng dán khuôn bên dưới còn ngoặc vuông vào Go.

```text
Tạo đúng MỘT trang manga màu dọc 4:5, chap [số], page [ID], không in ID. Số panel [N]; [numbering, hàng/cột, tỷ lệ, hướng đọc và khoảng tách]. Điểm rơi là [thông tin hoặc cảm xúc cần giữ].
Ảnh cần dùng: [tên/số và vai trò]. Cảnh: [nơi, giờ, ánh sáng, ngày/outfit, người và đạo cụ]; nối từ [trạng thái trang trước].
Panel 1: [cỡ cảnh, ai ở đâu, cử chỉ một nhịp, biểu cảm quan sát được, hướng mắt và vùng đặt chữ].
Chữ in: [người nói/loại chữ theo thứ tự, nguyên văn tiếng Việt; hoặc Không chữ].
[Liệt kê đủ từng panel với quy cách trên, không mở rộng ngoài phạm vi trang.]
Chỉ in câu đích, không in nhãn. Chữ thoại và Dẫn truyện theo ảnh 02; dấu rõ, đúng đuôi bóng, bóng không vượt rãnh hay che mặt. Không thêm người, tư thế, vật, chữ UI hoặc tình tiết ngoài mô tả. Giữ đồ, đạo cụ và nhận diện xuyên cảnh.
```

**Kiểm trước khi bàn giao:** Đủ 00–04 theo thứ tự; mục 00 có toàn bộ mạch và hook; từng page khớp thứ tự đã nạp; số trang truyện dưới 20; bộ outfit trùng mốc; lời đọc thành tiếng tự nhiên, phân vai rõ; kiểm đọc recap và ảnh ghép ở khổ điện thoại khi có bản thật. Không tạo file QA riêng trong chap.

# Chap 01 — Ngày đầu đừng commit bừa

Chap 01 đã hoàn thành: `art/cover.png` và `art/p01.png`–`art/p15.png`. Không có recap trước chap đầu. Tài liệu này gom prompt, kịch bản và ghi chú rà đã có; không gen lại hay sửa ảnh. Một số trang từng được gen lại từ Go; khi lời trong tài liệu cũ khác với ảnh đã chọn, dùng ảnh làm nguồn continuity cho chap sau.

[Kịch bản lưu trữ](#kịch-bản-lưu-trữ) · [Mẫu prompt chung](../../go-image-prompts.md)

## 00 — Mở session mới

Chọn cả **6 PNG trong [Go pack](../../assets/reference/go-pack/)** theo thứ tự tên `01`–`06` và đính kèm trong cùng một lượt, cùng tin nhắn mở session. Giữ session đó để gửi riêng từng khối `cover`, `p01` … `p15`. Tên file chỉ là nhãn lưu, không in lên ảnh. Nếu Go dùng nhầm reference ở lượt sau, đính lại theo đúng thứ tự trước khi gửi prompt trang.

1. [Comic art guide](../../assets/reference/go-pack/01-comic-art-style-guide.png) — nét, màu, bóng và biểu cảm.
2. [Lettering guide](../../assets/reference/go-pack/02-lettering-style-guide.png) — kiểu bong bóng, lời dẫn và SFX tiếng Việt; không lấy mặt hay thoại mẫu.
3. [Sơ đồ văn phòng IT](../../assets/reference/go-pack/03-it-office-floor-plan.png) — không gian; không sao chép sơ đồ.
4. [Lineup Phong–Dũng–Đạt](../../assets/reference/go-pack/04-office-lineup-phong-dung-dat.png) — **trái Phong, giữa Dũng, phải Đạt** theo góc nhìn người xem.
5. [Sheet Thảo–Nhi–Trân](../../assets/reference/go-pack/05-thao-nhi-tran.png) — **trái Thảo, giữa Nhi, phải Trân**.
6. [Sheet Khang–Minh–Nam](../../assets/reference/go-pack/06-khang-minh-nam.png) — **trái Khang, giữa Minh, phải Nam** theo góc nhìn người xem.

```text
Tôi chuẩn bị một bìa và 15 trang cho chap 01 “Ngày đầu đừng commit bừa” của truyện tiếng Việt Commit Trái Tim. Lượt này chỉ ghi nhận bối cảnh và ảnh đính kèm, chưa tạo ảnh. Chờ prompt cover hoặc pXX.

Ảnh 1 (01-comic-art-style-guide.png): chỉ lấy nét manga màu, bóng mảng, texture nhẹ, màu ấm và biểu cảm tiết chế. Không sao chép tư thế, bố cục hoặc chữ.
Ảnh 2 (02-lettering-style-guide.png): chỉ lấy kiểu bong bóng và phân cấp chữ tiếng Việt. In đúng chữ từng prompt; không lấy ngoại hình hay thoại mẫu.
Ảnh 3 (03-it-office-floor-plan.png): chỉ lấy liên hệ cửa kính, dãy bàn, pantry, lối WC, phòng họp; không vẽ bản đồ hay nhãn phòng.
Ảnh 4 (04-office-lineup-phong-dung-dat.png): TRÁI là Phong, tóc nâu đỏ dựng, sơ mi sáng, thẻ nhân viên, không kính. GIỮA là Dũng, tóc sẫm ngắn, vai rộng, sơ mi sẫm, quần cargo nâu ô-liu, đồng hồ, không kính. PHẢI là Đạt, tóc sẫm rối, kính chữ nhật, sơ mi sáng, thẻ nhân viên. Cả ba trưởng thành. Vị trí chỉ để nhận diện ảnh gốc, không ràng buộc bố cục trang. Giữ khuôn mặt, tóc, kính, tỷ lệ, trang phục đúng cho từng người.
Ảnh 5 (05-thao-nhi-tran.png): TRÁI là Thảo, QA, tóc búi và kính; GIỮA là Nhi, người mới, tóc buộc, hoodie sáng, jeans xanh rộng và tai nghe như hàng Trang phục; PHẢI là Trân, BA, tóc nâu dài gợn, áo sáng và chân váy nâu theo hàng mẫu chính. Thảo mặc áo cổ cao tối, quần be sáng và dây thẻ đỏ như mẫu chính, giữ nguyên. Ảnh 6 (06-khang-minh-nam.png): TRÁI là Khang, designer, tóc nâu gợn, sơ mi họa tiết tối và quần be; GIỮA là Minh, kỹ sư, dáng tròn, kính bo tròn, hoodie xám sáng; PHẢI là Nam, kỹ sư, kính chữ nhật, sơ mi caro và quần tối. Không nhầm kính, dáng hoặc trang phục Minh/Nam/Đạt. Ảnh 4–6 quyết định ngoại hình từng người; ảnh 1 chỉ quyết định cách vẽ.

Nội dung: Phong và Nhi tới ngày đầu, Đạt giới thiệu Phong và Nhi với toàn team. Cảnh chào có đúng tám người; Dũng vắng mặt, không vẽ hoặc nhắc tên anh. Thảo nhờ xem một nút lệch trên màn hình đặt lịch thử. Phong gặp Dũng trong WC nam, chào hơi lúng túng; Đạt nói vọng qua cánh cửa buồng đóng. Phong ăn trưa cùng Nhi. Minh và Nam giúp hai người mới vào đúng bản thử; Trân và Khang giải thích người dùng và quy ước nút. Chiều Phong phát hiện hai lượt đặt cùng giờ. Cuối chap cậu mới biết Dũng là CEO. Hài bằng phản ứng, không minh họa hoạt động vệ sinh, không có góc nhìn vào buồng hoặc theo cái liếc. Điểm tình cảm là ánh mắt và cách Dũng nhớ câu nói, không có tam giác tình yêu.

Một ngày, không đổi outfit. Sổ nhỏ xanh sẫm xuất hiện từ p03, để ở bàn khi Phong đi WC rồi mang theo vào phòng họp. Bìa là tranh đơn; các trang dọc 4:5 đọc từ trên xuống. Số panel theo prompt từng trang: trang hội thoại có 4–5 khung, p05 là trang toàn khung không chữ, p06 có một insert mắt hẹp và p07 chỉ có hai khung lớn. Mặc định gen hình cùng chữ có dấu theo từng prompt. Không in tên người nói, nhãn chỉ dẫn hay chữ giả. Không tự thêm người hay panel.
```

## cover — Bìa chap 01

Lưu `art/cover.png`.

```text
Tạo đúng một bìa manga màu dọc 4:5, một tranh không panel. Ảnh 4 khóa ngoại hình Phong và Dũng; ảnh 5 cột giữa cho Nhi; ảnh 1 cho cách vẽ, ảnh 3 cho văn phòng. Bố cục ba lớp: Phong lệch trái ở tiền cảnh cửa kính, Nhi vẫy từ ghế trống ở trung cảnh bên phải, Dũng áo sẫm thấp thoáng phía xa sau kính. Giữ tương phản tập trung ở mặt Phong và tấm thẻ: Phong nhìn ¾ về dãy bàn, ngón cái miết mép thẻ, vai hơi căng nhưng ánh mắt háo hức. Nhi cười tự nhiên, tai nghe ở cổ; Dũng không nhìn thẳng máy, không lộ chức danh. Không thêm người, không hé lộ WC. Ánh sáng sáng sớm ấm, phản chiếu kính nhẹ, không dùng vùng chữ để che nhân vật.

Để phần tư trên ít chi tiết và in đúng ba dòng có dấu theo thứ tự: “Commit Trái Tim” (lớn nhất), “Chap 01” (nhỏ), “Ngày đầu đừng commit bừa” (vừa). Chọn chữ đậm dễ đọc ở thumbnail; không in ngoặc bao ngoài, tagline, logo hay watermark.
```

## Prompt từng trang

Gửi mỗi khối một lượt. Mặc định Go đặt chữ theo prompt. Kiểm dấu và đuôi bong bóng ngay; nếu máy vẽ sai chữ, dùng lệnh bản sạch cuối file rồi đặt chữ từ [kịch bản lưu trữ](#kịch-bản-lưu-trữ).

### p01 — Quẹt thẻ lần đầu

Lưu `art/p01.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p01 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 3 dải ngang từ trên xuống, chiều cao tương đối 42/24/34, rãnh trắng đều, không chia thêm ô. Nhịp trang: Hành lang rộng, cận tay, rồi bước qua cửa. Tiếng tít thay cho lời giải thích.

Panel 1 — Hình: Phong ở cửa kính, đưa thẻ đeo dây đen vào đầu đọc bên phải; Nhi đứng cạnh, tai nghe vòng cổ. Chừa trên trái.
Chữ đúng thứ tự: Caption: Ngày đầu đi làm. • Phong: Ủa, chưa được hả?

Panel 2 — Hình: Cận tay; thẻ đang cách mặt đọc một chút, Nhi chỉ vào tâm đầu đọc, đèn vẫn tắt. Giữ hướng cửa, chừa trên phải.
Chữ đúng thứ tự: Nhi: Áp sát vô thử coi.

Panel 3 — Hình: Góc từ trong cửa, đầu đọc sáng. Phong bước qua, vai hạ nhẹ; Nhi theo sau. SFX sát đầu đọc, bóng thoại trên Nhi.
Chữ đúng thứ tự: SFX: Tít! • Nhi: Rồi, vô thôi ông.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p02 — Đây là Phong với Nhi

Lưu `art/p02.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p02 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 4 dải ngang từ trên xuống, chiều cao tương đối 38/21/19/22, rãnh trắng đều, không chia thêm ô. Nhịp trang: Khung lớn xác lập cả team; chuyển sang từng người mới rồi một nhịp đáp, không chen thêm lời.

Panel 1 — Hình: Toàn cụm bàn chung theo sơ đồ. Đạt đứng cùng Phong và Nhi ở đầu lối đi; Thảo, Trân, Khang, Minh, Nam quay về phía họ từ bàn. Đúng tám người; Dũng không xuất hiện, kể cả trong ảnh hoặc phản chiếu. Chừa hai bóng nhỏ phía Đạt.
Chữ đúng thứ tự: Đạt: Mọi người ơi, cho anh một phút. • Đạt: Đây là Phong với Nhi, hai bạn mới của team mình.

Panel 2 — Hình: Trung cận Phong đặt tay lên quai túi, cười hơi căng nhưng nhìn cả nhóm. Chừa trên Phong.
Chữ đúng thứ tự: Phong: Em chào mọi người. Em mới ra trường, có gì mọi người chỉ em với ạ.

Panel 3 — Hình: Trung cận Nhi đặt tay lên lưng ghế gần nhất, nhìn cùng hướng với Phong. Chừa trên Nhi, không che tai nghe.
Chữ đúng thứ tự: Nhi: Em là Nhi. Em mà gọi nhầm tên thì sửa em liền nha.

Panel 4 — Hình: Minh cười từ ghế, nhấc tay; Nam đặt chuột xuống nhìn sang Minh, Trân mỉm cười. Hai bóng gọn theo đúng người.
Chữ đúng thứ tự: Minh: Cứ gọi anh Minh trước. Tên dễ nhớ nhất phòng. • Nam: Tự chấm luôn ha.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p03 — Chỗ này của hai em

Lưu `art/p03.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p03 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 5 panel trên 4 hàng: hàng 1 là panel 1 toàn chiều ngang; hàng 2 là panel 2; hàng 3 chia đôi (trái panel 3, phải panel 4); hàng 4 là panel 5 toàn chiều ngang. Đọc từ trên xuống, trái sang phải ở hàng 3. Chiều cao bốn hàng khoảng 19/22/35/24, rãnh trắng rõ; để bóng thoại không bắc qua rãnh. Nhịp trang: Năm khung trong bốn hàng: 1 và 2 toàn ngang; 3 trái và 4 phải cùng hàng; 5 toàn ngang. Đọc 3 trước 4. Xếp chỗ, đổi ghế, chỉ đường, mở bản thử rồi nhận việc; không đưa cả nhóm vào mọi khung.

Panel 1 — Hình: Đạt chỉ hai ghế cạnh nhau; Nhi định kéo chiếc có tay vịn xô lệch, Minh thấy và đưa tay ra. Chừa trên Đạt rồi Minh.
Chữ đúng thứ tự: Đạt: Hai em ngồi đây nhé. • Minh: Ấy, ghế đó để anh đổi cho.

Panel 2 — Hình: Nam đẩy ghế lành ra. Minh đỡ chiếc hỏng; Nhi né một bước. Hai bóng ở phía trên.
Chữ đúng thứ tự: Nam: Cái tay vịn lỏng. Lấy ghế này đi. • Minh: Cái ghế đó anh suýt ngã bữa trước.

Panel 3 — Hình: Trân đặt hai tờ hướng dẫn cạnh bàn phím; Khang chỉ hình cốc nhỏ trên một tờ. Không in chữ giả. Chừa hai bóng không che giấy.
Chữ đúng thứ tự: Trân: Chị Trân. Cần tài liệu thì nhắn chị nha. • Khang: Anh Khang. Muốn tìm cà phê thì mở trang hình cái cốc.

Panel 4 — Hình: Thảo đứng cạnh Phong, chỉ màn hình; Nhi ngồi ghế lành ở lớp sau. Chừa bóng cho Thảo và Phong.
Chữ đúng thứ tự: Thảo: Chị Thảo, QA. Em vào được bản thử chưa? • Phong: Dạ, máy em vào được rồi.

Panel 5 — Hình: Cận bảng lịch và nút nhỏ hơi lệch. Phong đặt sổ xanh cạnh phím. Không in ký tự UI; bóng ngoài màn hình.
Chữ đúng thứ tự: Thảo: Cái nút Đặt lại hơi lệch. Em xem giúp chị. • Phong: Dạ, để em thử trước.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p04 — Ra ngoài một lát

Lưu `art/p04.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p04 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 3 dải ngang từ trên xuống, chiều cao tương đối 33/37/30, rãnh trắng đều, không chia thêm ô. Nhịp trang: Bớt lời sau cảnh đông; ghế sang cửa là điểm cắt đổi nhịp.

Panel 1 — Hình: Nhi nghiêng đầu từ ghế bên, tai nghe lệch một bên; Phong vừa buông chuột. Chừa trên cả hai.
Chữ đúng thứ tự: Nhi: Trưa ăn gì ông? • Phong: Bà kiếm được quán rồi hả?

Panel 2 — Hình: Nhi giơ hai ngón tay cạnh điện thoại; Phong đứng, sổ xanh vẫn ở bàn. Chừa phía trên.
Chữ đúng thứ tự: Nhi: Có hai quán. Quán nào dưới năm chục thì vô. • Phong: Chờ tui chút. Tui đi rửa mặt.

Panel 3 — Hình: Máy ngoài hành lang: Phong đẩy cửa WC nam. Chỉ biểu tượng đơn giản, không thấy bên trong hay Dũng.
Chữ đúng thứ tự: Không chữ.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p05 — Mở cảnh WC

Lưu `art/p05.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p05 (không in). Dùng ảnh 1 cho nét, ảnh 3 cho không gian và ảnh 4 cho nhận diện Phong–Dũng. Một khung toàn trang có viền, không chia ô.

Panel 1 — Hình: Toàn khung dọc, góc máy từ sau lưng: Dũng áo sẫm đứng bên trái, Phong áo sáng tóc nâu đỏ đứng bên phải, ở hai vị trí cạnh nhau sau vách ngăn. Dũng hơi ngoảnh đầu; Phong cứng vai một nhịp. Dùng sắc gạch và ánh đèn ấm để nối với trang sau. Hai người mặc nguyên trang phục công sở; không mô tả cơ thể riêng tư hoặc hoạt động vệ sinh.
Chữ đúng thứ tự: Không chữ.

Không thêm lời thoại, caption, số trang, logo hoặc chữ giả.
```

### p06 — Chào anh

Lưu `art/p06.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p06 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 4 dải ngang từ trên xuống, chiều cao tương đối 31/24/13/32, rãnh trắng đều, không chia thêm ô. Nhịp trang: Chào, đáp, insert liếc, cắt ngay sang quay mặt. Ba khung nhân vật lớn/vừa, insert mắt rất hẹp.

Panel 1 — Hình: Phong bước qua vách, Dũng áo sẫm bên phải Phong, cửa buồng đóng mờ xa. Chỉ khung đầu–vai ngang mắt. Chừa một bóng nhỏ.
Chữ đúng thứ tự: Phong: Em chào anh.

Panel 2 — Hình: Cận đầu–vai Dũng quay sang vừa đủ, bình thản, đúng người giữa lineup; không ghé sát. Chừa trên phải.
Chữ đúng thứ tự: Dũng: Ừ. Em mới vào à?

Panel 3 — Hình: Insert chỉ mắt và mày Phong. Cậu vô thức liếc xuống phía vùng riêng tư của Dũng, hoàn toàn ngoài khung. Chỉ đồng tử hạ chéo và mí khựng; không đích nhìn, thân thể, gương hay góc POV.
Chữ đúng thứ tự: Không chữ.

Panel 4 — Hình: Cắt ngay sang đầu–vai Phong cùng trục. Cậu quay mặt sang hướng ngược Dũng vì ngượng, nhìn vào tường, tai ửng nhẹ. Không nhìn lại, không hạ máy. Chừa một bóng nhỏ.
Chữ đúng thứ tự: Phong: Dạ. Em mới… mới vào sáng nay.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p07 — Họp ngoài đó

Lưu `art/p07.png`.

```text
Vẽ một trang manga màu dọc 4:5, chap 01, nhãn p07 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Đúng 2 dải ngang từ trên xuống, chiều cao tương đối 43/57, rãnh trắng đều, không chia thêm ô. Nhịp trang: Hai khung lớn. Cửa đóng làm nền cho lời vọng; khung dưới cho phản ứng tự kể.

Panel 1 — Hình: Khung tĩnh cửa buồng đóng kín, nhìn từ bên ngoài; không Đạt, không khe nhìn. Một bóng thoại vọng hướng về cửa.
Chữ đúng thứ tự: Đạt (vọng từ buồng): Hai người họp ngoài đó xong chưa?

Panel 2 — Hình: Hai đầu–vai cùng trục p06. Phong giật mắt về cửa, tai còn đỏ. Dũng quay sang cửa để đỡ lời, khóe miệng hơi nhấc; không nhìn chằm chằm Phong. Phong liếc lên ngang tầm mắt một thoáng khi nghe anh đáp; vai thả lỏng. Không hạ máy. Dành khoảng im quanh hai gương mặt.
Chữ đúng thứ tự: Dũng: Chưa. Mới chào nhau thôi.

In đúng nội dung sau nhãn, không in tên người nói, nhãn kỹ thuật hay dấu phân cách •. Giữ đúng dấu tiếng Việt. Bóng thoại oval hướng đuôi đúng người; lời vọng hướng ngoài khung; ý nghĩ không đuôi; caption khung chữ nhật; SFX sát nguồn. UI chỉ in từng giá trị được giao, không in / hoặc dấu chấm cuối danh sách. Không chữ = panel im. Không thêm người, panel, logo hay chữ giả.
```

### p08 — Bốn mươi chín nghìn

Lưu `art/p08.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p08 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 3 panel. Bố cục: Ba panel: hàng trên toàn ngang chiếm 52% chiều cao, hàng dưới chia trái–phải 45/55. Đọc 1 → 2 trái → 3 phải. Nhịp trang: Caption nhảy từ WC sang bữa trưa đã hẹn ở p04; từ né ánh mắt sang thoải mái với bạn. Chốt bằng Nhi nhắc việc cần làm khi về bàn.

Panel 1 — Hình: Khung rộng pantry: Phong và Nhi đặt hai hộp cơm vừa lấy xuống bàn. Nắng trưa ấm; tai nghe Nhi nằm cạnh hộp, Phong đã bớt căng nhưng còn ngẩn ra. Chừa ô caption ở góc trên trái, lời Nhi trên phía cô.
Chữ đúng thứ tự: Caption: Đến giờ trưa. • Nhi: Bốn chín. Còn dư một ngàn nha.

Panel 2 — Hình: Cận ngang tay: Phong gắp miếng trứng sang hộp Nhi như trả công. Giữ mặt Phong ở rìa trên nếu đủ chỗ, đừng để bóng che hai hộp.
Chữ đúng thứ tự: Phong: Nè, công tìm quán.

Panel 3 — Hình: Nhi nhận miếng trứng, cười rồi rướn tay lấy điện thoại cạnh tai nghe. Màn hình úp hoặc không chữ. Chừa trên Nhi cho bóng ngắn.
Chữ đúng thứ tự: Nhi: Lát về nhắc tui hỏi anh Minh cái dây mạng nha.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p09 — Về bàn

Lưu `art/p09.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p09 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 4 panel. Bố cục: Bốn panel: hàng trên toàn ngang 30%; hàng giữa 37% chia trái rộng 58%, phải 42%; hàng dưới toàn ngang 33%. Đọc 1, 2 trái, 3 phải, 4 dưới. Nhịp trang: Đáp lại lời Nhi từ p08. Nối bằng động tác đặt tay xuống bàn, rồi tiếng nói bên cạnh dẫn sang chuyện bản thử.

Panel 1 — Hình: Sau bữa trưa, góc nhìn từ lối pantry về đúng cụm ghế cũ. Nhi về bàn, một tay vừa đặt tai nghe xuống; Phong ngồi cạnh, sổ xanh đúng cạnh phím. Minh bước dọc lối đi tới Nhi, cầm cuộn dây. Không cần caption, tư thế ngồi và đạo cụ xác lập chỗ cũ.
Chữ đúng thứ tự: Không chữ.

Panel 2 — Hình: Minh đặt cuộn dây: bố cục tay và dây ở giữa, mặt Minh dáng tròn kính bo ở trên. Nhi đón dây. Chừa hai bóng ngắn không che cuộn.
Chữ đúng thứ tự: Minh: Nè, dây của em. • Nhi: Ủa, em chưa kịp hỏi luôn.

Panel 3 — Hình: Trong ô hẹp, Nam ở phía bàn Phong, chỉ dải màu bằng đầu bút, không chạm màn hình. Chừa một bóng nhỏ đủ rộng. Dải màu là dấu hiệu môi trường, không phải thông báo lỗi.
Chữ đúng thứ tự: Nam: Phong, đúng bản thử chưa em?

Panel 4 — Hình: Khung rộng giữ Phong đối diện màn hình, Nam rời theo lối đi. Phong gật rồi nhích con trỏ đến nút đang lệch trong lưới lịch, chưa bấm. Để màn hình và tay chuột đọc được. Bóng Phong trên đầu; không in chữ UI.
Chữ đúng thứ tự: Phong: Dạ, đúng rồi.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p10 — Để nguyên chỗ đó

Lưu `art/p10.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p10 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 4 panel. Bố cục: Bốn panel: hàng 1 toàn ngang 25%; hàng 2 toàn ngang 32%; hàng cuối 43% chia trái rộng 63% (panel 3), phải 37% (panel 4). Nhịp trang: Nút cuối p09 mở câu hỏi đầu p10. Chuyển từ việc căn nút sang lý do Phong muốn thử thao tác thực tế.

Panel 1 — Hình: Giữ đúng hướng màn hình cuối p09, Phong đưa tay chỉ nút. Trân dừng cạnh bàn với tờ lịch và nhìn theo đầu ngón tay. Bóng Phong ở ngoài màn hình.
Chữ đúng thứ tự: Phong: Chị Trân, em dời nút qua đây cho thẳng được không?

Panel 2 — Hình: Khung ngang hai người, Trân nghiêng tờ lịch để minh họa; chỉ vào một ô và nhìn Phong, không che lưới. Bóng trên khoảng trống phía Trân.
Chữ đúng thứ tự: Trân: Giữ chỗ cũ nha em. Khách đứng ngay quầy, lễ tân quen tay bấm ở đó rồi.

Panel 3 — Hình: Qua vai Phong: Khang đặt bản phác cạnh tờ lịch, dùng hai đầu ngón tay lần theo hai mép cần căn. Không chữ giả trên giấy; một bóng ngắn.
Chữ đúng thứ tự: Khang: Căn hai mép thôi. Nút cứ để đấy.

Panel 4 — Hình: Cận mặt Phong nhìn từ tay Khang xuống chuột. Tay Phong đặt lên chuột nhưng chưa bấm; giữ đúng bàn tay và hướng chuột cho đầu p11. Một bóng ngắn phía trên.
Chữ đúng thứ tự: Phong: Dạ, để em thử trước.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p11 — Một nhịp chờ

Lưu `art/p11.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p11 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 3 panel. Bố cục: Ba panel theo nhịp co–giãn: hàng trên cao 42% chia trái hẹp 32% (panel 1), phải 68% (panel 2); panel 3 toàn ngang 58%. Nhịp trang: Không nhảy giờ giữa câu ở p10 và cú bấm. Dành ô lớn nhất cho chờ, không cho kết quả hiện sớm.

Panel 1 — Hình: Cận đúng bàn tay trên chuột từ p10, ngón trỏ bấm lần một. SFX nhỏ sát chuột.
Chữ đúng thứ tự: SFX: Cạch.

Panel 2 — Hình: Cận lưới lịch và chấm xử lý rất nhỏ, chưa có thẻ kép. Giữ mép màn hình và ánh sáng đã lập; không in chữ hoặc số.
Chữ đúng thứ tự: Không chữ.

Panel 3 — Hình: Khung rộng hơn theo trục cũ: Phong chờ, ngón trỏ vẫn hờ trên chuột, mặt hơi nghiêng về màn hình. Có thể thấy sổ xanh cạnh phím. Để khoảng tĩnh phía phải và một ô nghĩ nhỏ; không đưa người khác vào.
Chữ đúng thứ tự: Phong (nghĩ): Ủa, bấm rồi mà?

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p12 — Khoan, để nguyên

Lưu `art/p12.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p12 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 4 panel. Bố cục: Bốn panel: hàng trên 39% toàn ngang; hàng giữa 35% chia trái 57% và phải 43%; hàng dưới 26% toàn ngang. Đọc trên xuống, trái sang phải ở hàng giữa. Nhịp trang: Nối cử chỉ đang lơ lửng ở p11 với lần bấm hai, rồi chặn Phong trước khi mất dấu lỗi.

Panel 1 — Hình: Khung qua vai cùng trục p11: ngón tay bấm lần hai, thấy hai thẻ khác màu trong cùng một ô. Hai thẻ chỉ gối nhẹ; chưa in giờ hoặc mã. Đặt SFX gần tay, không lấp ô.
Chữ đúng thứ tự: SFX: Cạch.

Panel 2 — Hình: Cận Phong nhìn ngạc nhiên, chỉ ô lịch rồi định đưa tay về chuột. Một bóng ngoài màn hình.
Chữ đúng thứ tự: Phong: Chị Thảo, em tải lại nha? Nó ra hai cái nè.

Panel 3 — Hình: Cận Thảo tới từ lối đi, giơ bàn tay ra hiệu dừng, không chạm Phong. Chừa một bóng rõ phía trên.
Chữ đúng thứ tự: Thảo: Khoan. Để nguyên cho chị xem.

Panel 4 — Hình: Khung ngang đầu–vai ở đúng bàn: Thảo cúi vừa đủ để cùng nhìn; Phong rời tay khỏi chuột, kéo sổ xanh tới. Bóng Thảo đúng hướng; kết bằng câu hỏi để p13 trả lời.
Chữ đúng thứ tự: Thảo: Em vừa bấm mấy lần?

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p13 — Hai mã, một khung giờ

Lưu `art/p13.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p13 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 4 panel. Bố cục: Bốn panel: 1 toàn ngang cao 44%; hàng hai cao 32% chia trái 63% và phải 37%; 4 toàn ngang cao 24%. Nhịp trang: Cho người đọc thấy bằng chứng lớn trước khi rời bàn; việc chuyển cảnh có lý do và lỗi được lưu lại.

Panel 1 — Hình: Cận thẳng màn hình: một ô 14:30, hai thẻ khác màu có đủ chỗ cho A17 và B24, không đè chữ lên nhau. Bóng Phong ngoài UI, không in lời Thảo từ trang trước.
Chữ đúng thứ tự: UI: 14:30 / A17 / B24. • Phong: Hai lần ạ. Lần đầu không thấy gì.

Panel 2 — Hình: Thảo giữ mắt trên màn hình, chỉ vào biểu tượng chụp ảnh dạng hình học. Phong nghe, hai tay tách khỏi chuột. Chừa bóng trên Thảo.
Chữ đúng thứ tự: Thảo: Chụp lại ô này rồi gửi chị nha. Chưa cần sửa gì hết.

Panel 3 — Hình: Cận ngón tay Phong nhấn tổ hợp phím; thấy mép sổ xanh kê cạnh phím. Không biến thành lần bấm chuột thứ ba. Không chữ UI.
Chữ đúng thứ tự: Không chữ.

Panel 4 — Hình: Rộng theo trục bàn: ảnh đã lưu, Phong gập sổ; Đạt dừng ở lối đi gọi Phong và Nhi. Bóng Đạt phía lối đi. Giữ ánh chiều; không nhắc tên hoặc dáng Dũng.
Chữ đúng thứ tự: Đạt: Hai em xong thì qua phòng họp gặp anh một lát nhé.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p14 — Cửa mở

Lưu `art/p14.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p14 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 3 panel. Bố cục: Ba panel bất đối xứng: hàng trên cao 72%, trái 64% là panel 1 từ ngưỡng cửa, phải 36% là panel 2 cận; hàng đáy cao 28% là panel 3 ngang. Đọc trái → phải → dưới. Nhịp trang: Mở lại cảnh bằng cue địa điểm và sổ xanh, không kể lại lỗi. Giữ cú lộ mặt cho p15.

Panel 1 — Hình: Nhìn từ ngưỡng cửa thấy phòng họp đúng mặt bằng, bàn kéo sâu vào khung. Phong và Nhi đang tới hai ghế cạnh nhau; Phong đặt sổ xanh xuống, Đạt ở đầu bàn. Caption nhỏ trên trái ngoài vùng mặt. Không có Dũng trong khung.
Chữ đúng thứ tự: Caption: Một lát sau, tại phòng họp. • Đạt: Hai em ngồi đi.

Panel 2 — Hình: Cận tay Phong miết cạnh sổ, Nhi ghé sát vừa đủ, không cười trêu. Bóng thì thầm ngắn nằm gọn trong ô hẹp, bóng Phong thấp hơn.
Chữ đúng thứ tự: Nhi (thì thầm): Ông run nữa hả? • Phong: Đâu có.

Panel 3 — Hình: Dải cuối chỉ thấy tay đẩy cánh cửa, tay áo sẫm và đồng hồ, lấy ánh đèn hành lang làm tương phản. Không vẽ mặt, bóng người hay phản chiếu nhận diện. Bóng Đạt từ ngoài khung.
Chữ đúng thứ tự: Đạt (ngoài khung): Mời anh.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

### p15 — À. Sếp.

Lưu `art/p15.png`.

```text
Vẽ đúng một trang manga màu dọc 4:5, chap 01, nhãn p15 (không in). Ảnh 1 cho nét, 2 cho chữ, 3 cho không gian, 4–6 khóa ngoại hình. Giữ đúng 3 panel. Bố cục: Ba panel: hàng trên cao 32%, trái 62% là panel 1 ở cửa, phải 38% là panel 2 phản ứng; panel 3 toàn ngang 68%. Nhịp trang: Nối hành động mở cửa rồi dành phần lớn trang cho ánh mắt; không dùng hồi tưởng để giải thích câu đùa.

Panel 1 — Hình: Dũng bước hết nửa bước qua cánh cửa p14, đúng áo sẫm và đồng hồ; Đạt nghiêng về hai người mới. Chừa bóng Đạt, không in chức danh như bảng tên.
Chữ đúng thứ tự: Đạt: Hai em, đây là anh Dũng, CEO bên mình.

Panel 2 — Hình: Cận Phong nhận ra người lúc sáng, tay ngừng miết cạnh sổ; tai ửng nhẹ, mắt mở thêm một chút. Một bóng nhỏ phía trên, không che mắt.
Chữ đúng thứ tự: Phong: Dạ… em chào anh.

Panel 3 — Hình: Khung lớn ngang: Phong nhìn lên, Dũng bắt gặp ánh mắt, cười vừa đủ. Đạt mở tập giấy, Nhi vẫn về phía Đạt. Để khoảng trống giữa hai ánh mắt rồi đặt bóng của Dũng phía trên, ý nghĩ Phong nhẹ ở dưới. Không flashback hay thêm đối thoại.
Chữ đúng thứ tự: Dũng: Lần này mới tính là họp nhé. • Phong (nghĩ): À. Sếp.

Chỉ in chữ sau từng nhãn, giữ dấu tiếng Việt; không in tên người nói, nhãn kỹ thuật, dấu phân cách • hoặc /. Với UI, in đúng từng giá trị đã ghi ở đúng vị trí. Bóng thoại hướng đuôi đúng người, lời vọng từ ngoài khung, ý nghĩ không đuôi, caption trong ô chữ nhật riêng, SFX sát nguồn. Không chữ = panel im. Rãnh trắng rõ, không để bóng vượt rãnh; không tự thêm panel, nhân vật, logo hoặc chữ giả.
```

## Nếu cần gen bản sạch

Nếu chữ sai dấu, nhầm đuôi hoặc khó đọc, gửi lại khối của đúng ảnh kèm lệnh dưới. Dùng chữ từ phần Kịch bản lưu trữ rồi giữ ảnh đã chọn bằng tên trang chuẩn.

```text
Chế độ bản sạch: giữ đúng bố cục, hình, nhận diện và vùng chừa chữ; không vẽ chữ, số, caption, SFX, chữ UI, bong bóng, logo hay watermark. Không đổi nội dung hình.
```

---

## Kịch bản lưu trữ

**15 trang + 1 bìa riêng · đã có ảnh Go.**

[Prompt gửi Go](#00--mở-session-mới) · [Ghi chú rà cũ](#ghi-chú-rà-cũ) · [Sườn mùa](../../story-outline.md) · [Series Bible](../../README.md)

### Mạch chap

Sáng, Đạt gom cả team chào Phong và Nhi. Dũng vắng mặt và không được nhắc tên. Nhóm phá băng bằng một chiếc ghế hỏng. Thảo giao việc xem nút Đặt lại trên bản thử. Sau cảnh gặp người áo sẫm ở WC và bữa cơm với Nhi, Phong quay lại làm việc, được đồng nghiệp giúp rồi phát hiện hai mã cùng một giờ. Cuối chap Phong mới biết người áo sẫm là Dũng, CEO.

- **Continuity:** Một ngày, không đổi outfit. p02 có đúng tám người: Đạt, Phong, Nhi, Thảo, Trân, Khang, Minh và Nam. Dũng không xuất hiện trong cảnh chào. Sổ xanh có từ p03, vẫn ở bàn lúc Phong đi WC, mang vào họp.
- **Nhịp:** p02–p03 có thêm panel để đổi người nói. p05 là trang toàn khung mở cảnh WC. p06 tách một insert mắt hẹp khỏi động tác quay đi; p07 giữ hai khung lớn, chỉ cửa đóng và phản ứng. Không vẽ đích nhìn hoặc chi tiết riêng tư. Câu đùa “họp” có lời đáp ở p15.
- **Chữ chuẩn:** Mục **Đặt chữ** là nguyên văn. `Không chữ` là panel im. UI chỉ hiện đủ giờ và mã ở p13; team chưa kết luận nguyên nhân.

### Bìa (`cover`)

Giữ bìa Phong cầm thẻ trước cửa kính, Nhi vẫy ở dãy bàn, Dũng thấp thoáng lớp sau. Không kể hộ gag WC hay chức danh. Chữ: **Commit Trái Tim** · **Chap 01** · **Ngày đầu đừng commit bừa**.

### Kịch bản trang và chữ

#### p01 — Quẹt thẻ lần đầu

Hành lang rộng, cận tay, rồi bước qua cửa. Tiếng tít thay cho lời giải thích.

- **p01-01:** Phong ở cửa kính, đưa thẻ đeo dây đen vào đầu đọc bên phải; Nhi đứng cạnh, tai nghe vòng cổ. Chừa trên trái. **Đặt chữ:** Caption: Ngày đầu đi làm. • Phong: Ủa, chưa được hả?
- **p01-02:** Cận tay; thẻ đang cách mặt đọc một chút, Nhi chỉ vào tâm đầu đọc, đèn vẫn tắt. Giữ hướng cửa, chừa trên phải. **Đặt chữ:** Nhi: Áp sát vô thử coi.
- **p01-03:** Góc từ trong cửa, đầu đọc sáng. Phong bước qua, vai hạ nhẹ; Nhi theo sau. SFX sát đầu đọc, bóng thoại trên Nhi. **Đặt chữ:** SFX: Tít! • Nhi: Rồi, vô thôi ông.

#### p02 — Đây là Phong với Nhi

Khung lớn xác lập cả team; chuyển sang từng người mới rồi một nhịp đáp, không chen thêm lời.

- **p02-01:** Toàn cụm bàn chung theo sơ đồ. Đạt đứng cùng Phong và Nhi ở đầu lối đi; Thảo, Trân, Khang, Minh, Nam quay về phía họ từ bàn. Đúng tám người; Dũng không xuất hiện, kể cả trong ảnh hoặc phản chiếu. Chừa hai bóng nhỏ phía Đạt. **Đặt chữ:** Đạt: Mọi người ơi, cho anh một phút. • Đạt: Đây là Phong với Nhi, hai bạn mới của team mình.
- **p02-02:** Trung cận Phong đặt tay lên quai túi, cười hơi căng nhưng nhìn cả nhóm. Chừa trên Phong. **Đặt chữ:** Phong: Em chào mọi người. Em mới ra trường, có gì mọi người chỉ em với ạ.
- **p02-03:** Trung cận Nhi đặt tay lên lưng ghế gần nhất, nhìn cùng hướng với Phong. Chừa trên Nhi, không che tai nghe. **Đặt chữ:** Nhi: Em là Nhi. Em mà gọi nhầm tên thì sửa em liền nha.
- **p02-04:** Minh cười từ ghế, nhấc tay; Nam đặt chuột xuống nhìn sang Minh, Trân mỉm cười. Hai bóng gọn theo đúng người. **Đặt chữ:** Minh: Cứ gọi anh Minh trước. Tên dễ nhớ nhất phòng. • Nam: Tự chấm luôn ha.

#### p03 — Chỗ này của hai em

Năm khung trong bốn hàng: 1 và 2 toàn ngang; 3 trái và 4 phải cùng hàng; 5 toàn ngang. Đọc 3 trước 4. Xếp chỗ, đổi ghế, chỉ đường, mở bản thử rồi nhận việc; không đưa cả nhóm vào mọi khung.

- **p03-01:** Đạt chỉ hai ghế cạnh nhau; Nhi định kéo chiếc có tay vịn xô lệch, Minh thấy và đưa tay ra. Chừa trên Đạt rồi Minh. **Đặt chữ:** Đạt: Hai em ngồi đây nhé. • Minh: Ấy, ghế đó để anh đổi cho.
- **p03-02:** Nam đẩy ghế lành ra. Minh đỡ chiếc hỏng; Nhi né một bước. Hai bóng ở phía trên. **Đặt chữ:** Nam: Cái tay vịn lỏng. Lấy ghế này đi. • Minh: Cái ghế đó anh suýt ngã bữa trước.
- **p03-03:** Trân đặt hai tờ hướng dẫn cạnh bàn phím; Khang chỉ hình cốc nhỏ trên một tờ. Không in chữ giả. Chừa hai bóng không che giấy. **Đặt chữ:** Trân: Chị Trân. Cần tài liệu thì nhắn chị nha. • Khang: Anh Khang. Muốn tìm cà phê thì mở trang hình cái cốc.
- **p03-04:** Thảo đứng cạnh Phong, chỉ màn hình; Nhi ngồi ghế lành ở lớp sau. Chừa bóng cho Thảo và Phong. **Đặt chữ:** Thảo: Chị Thảo, QA. Em vào được bản thử chưa? • Phong: Dạ, máy em vào được rồi.
- **p03-05:** Cận bảng lịch và nút nhỏ hơi lệch. Phong đặt sổ xanh cạnh phím. Không in ký tự UI; bóng ngoài màn hình. **Đặt chữ:** Thảo: Cái nút Đặt lại hơi lệch. Em xem giúp chị. • Phong: Dạ, để em thử trước.

#### p04 — Ra ngoài một lát

Bớt lời sau cảnh đông; ghế sang cửa là điểm cắt đổi nhịp.

- **p04-01:** Nhi nghiêng đầu từ ghế bên, tai nghe lệch một bên; Phong vừa buông chuột. Chừa trên cả hai. **Đặt chữ:** Nhi: Trưa ăn gì ông? • Phong: Bà kiếm được quán rồi hả?
- **p04-02:** Nhi giơ hai ngón tay cạnh điện thoại; Phong đứng, sổ xanh vẫn ở bàn. Chừa phía trên. **Đặt chữ:** Nhi: Có hai quán. Quán nào dưới năm chục thì vô. • Phong: Chờ tui chút. Tui đi rửa mặt.
- **p04-03:** Máy ngoài hành lang: Phong đẩy cửa WC nam. Chỉ biểu tượng đơn giản, không thấy bên trong hay Dũng. **Đặt chữ:** Không chữ.

#### p05 — Mở cảnh WC

Trang chuyển cảnh không thoại, một khung toàn trang để xác lập vị trí trước lời chào ở p06.

- **p05-01:** Toàn khung dọc, góc máy từ sau lưng: Dũng áo sẫm đứng bên trái, Phong áo sáng tóc nâu đỏ đứng bên phải, ở hai vị trí cạnh nhau sau vách ngăn. Dũng hơi ngoảnh đầu; Phong cứng vai một nhịp. Dùng sắc gạch và ánh đèn ấm để nối với trang sau. Hai người mặc nguyên trang phục công sở; không mô tả cơ thể riêng tư hoặc hoạt động vệ sinh. **Đặt chữ:** Không chữ.

#### p06 — Chào anh

Chào, đáp, insert liếc, cắt ngay sang quay mặt. Ba khung nhân vật lớn/vừa, insert mắt rất hẹp.

- **p06-01:** Phong bước qua vách, Dũng áo sẫm bên phải Phong, cửa buồng đóng mờ xa. Chỉ khung đầu–vai ngang mắt. Chừa một bóng nhỏ. **Đặt chữ:** Phong: Em chào anh.
- **p06-02:** Cận đầu–vai Dũng quay sang vừa đủ, bình thản, đúng người giữa lineup; không ghé sát. Chừa trên phải. **Đặt chữ:** Dũng: Ừ. Em mới vào à?
- **p06-03:** Insert chỉ mắt và mày Phong. Cậu vô thức liếc xuống phía vùng riêng tư của Dũng, hoàn toàn ngoài khung. Chỉ đồng tử hạ chéo và mí khựng; không đích nhìn, thân thể, gương hay góc POV. **Đặt chữ:** Không chữ.
- **p06-04:** Cắt ngay sang đầu–vai Phong cùng trục. Cậu quay mặt sang hướng ngược Dũng vì ngượng, nhìn vào tường, tai ửng nhẹ. Không nhìn lại, không hạ máy. Chừa một bóng nhỏ. **Đặt chữ:** Phong: Dạ. Em mới… mới vào sáng nay.

#### p07 — Họp ngoài đó

Hai khung lớn. Cửa đóng làm nền cho lời vọng; khung dưới cho phản ứng tự kể.

- **p07-01:** Khung tĩnh cửa buồng đóng kín, nhìn từ bên ngoài; không Đạt, không khe nhìn. Một bóng thoại vọng hướng về cửa. **Đặt chữ:** Đạt (vọng từ buồng): Hai người họp ngoài đó xong chưa?
- **p07-02:** Hai đầu–vai cùng trục p06. Phong giật mắt về cửa, tai còn đỏ. Dũng quay sang cửa để đỡ lời, khóe miệng hơi nhấc; không nhìn chằm chằm Phong. Phong liếc lên ngang tầm mắt một thoáng khi nghe anh đáp; vai thả lỏng. Không hạ máy. Dành khoảng im quanh hai gương mặt. **Đặt chữ:** Dũng: Chưa. Mới chào nhau thôi.

#### p08 — Bốn mươi chín nghìn

Ba panel: hàng trên toàn ngang chiếm 52% chiều cao, hàng dưới chia trái–phải 45/55. Đọc 1 → 2 trái → 3 phải. Caption nhảy từ WC sang bữa trưa đã hẹn ở p04; từ né ánh mắt sang thoải mái với bạn. Chốt bằng Nhi nhắc việc cần làm khi về bàn.

- **p08-01:** Khung rộng pantry: Phong và Nhi đặt hai hộp cơm vừa lấy xuống bàn. Nắng trưa ấm; tai nghe Nhi nằm cạnh hộp, Phong đã bớt căng nhưng còn ngẩn ra. Chừa ô caption ở góc trên trái, lời Nhi trên phía cô. **Đặt chữ:** Caption: Đến giờ trưa. • Nhi: Bốn chín. Còn dư một ngàn nha.
- **p08-02:** Cận ngang tay: Phong gắp miếng trứng sang hộp Nhi như trả công. Giữ mặt Phong ở rìa trên nếu đủ chỗ, đừng để bóng che hai hộp. **Đặt chữ:** Phong: Nè, công tìm quán.
- **p08-03:** Nhi nhận miếng trứng, cười rồi rướn tay lấy điện thoại cạnh tai nghe. Màn hình úp hoặc không chữ. Chừa trên Nhi cho bóng ngắn. **Đặt chữ:** Nhi: Lát về nhắc tui hỏi anh Minh cái dây mạng nha.

#### p09 — Về bàn

Bốn panel: hàng trên toàn ngang 30%; hàng giữa 37% chia trái rộng 58%, phải 42%; hàng dưới toàn ngang 33%. Đọc 1, 2 trái, 3 phải, 4 dưới. Đáp lại lời Nhi từ p08. Nối bằng động tác đặt tay xuống bàn, rồi tiếng nói bên cạnh dẫn sang chuyện bản thử.

- **p09-01:** Sau bữa trưa, góc nhìn từ lối pantry về đúng cụm ghế cũ. Nhi về bàn, một tay vừa đặt tai nghe xuống; Phong ngồi cạnh, sổ xanh đúng cạnh phím. Minh bước dọc lối đi tới Nhi, cầm cuộn dây. Không cần caption, tư thế ngồi và đạo cụ xác lập chỗ cũ. **Đặt chữ:** Không chữ.
- **p09-02:** Minh đặt cuộn dây: bố cục tay và dây ở giữa, mặt Minh dáng tròn kính bo ở trên. Nhi đón dây. Chừa hai bóng ngắn không che cuộn. **Đặt chữ:** Minh: Nè, dây của em. • Nhi: Ủa, em chưa kịp hỏi luôn.
- **p09-03:** Trong ô hẹp, Nam ở phía bàn Phong, chỉ dải màu bằng đầu bút, không chạm màn hình. Chừa một bóng nhỏ đủ rộng. Dải màu là dấu hiệu môi trường, không phải thông báo lỗi. **Đặt chữ:** Nam: Phong, đúng bản thử chưa em?
- **p09-04:** Khung rộng giữ Phong đối diện màn hình, Nam rời theo lối đi. Phong gật rồi nhích con trỏ đến nút đang lệch trong lưới lịch, chưa bấm. Để màn hình và tay chuột đọc được. Bóng Phong trên đầu; không in chữ UI. **Đặt chữ:** Phong: Dạ, đúng rồi.

#### p10 — Để nguyên chỗ đó

Bốn panel: hàng 1 toàn ngang 25%; hàng 2 toàn ngang 32%; hàng cuối 43% chia trái rộng 63% (panel 3), phải 37% (panel 4). Nút cuối p09 mở câu hỏi đầu p10. Chuyển từ việc căn nút sang lý do Phong muốn thử thao tác thực tế.

- **p10-01:** Giữ đúng hướng màn hình cuối p09, Phong đưa tay chỉ nút. Trân dừng cạnh bàn với tờ lịch và nhìn theo đầu ngón tay. Bóng Phong ở ngoài màn hình. **Đặt chữ:** Phong: Chị Trân, em dời nút qua đây cho thẳng được không?
- **p10-02:** Khung ngang hai người, Trân nghiêng tờ lịch để minh họa; chỉ vào một ô và nhìn Phong, không che lưới. Bóng trên khoảng trống phía Trân. **Đặt chữ:** Trân: Giữ chỗ cũ nha em. Khách đứng ngay quầy, lễ tân quen tay bấm ở đó rồi.
- **p10-03:** Qua vai Phong: Khang đặt bản phác cạnh tờ lịch, dùng hai đầu ngón tay lần theo hai mép cần căn. Không chữ giả trên giấy; một bóng ngắn. **Đặt chữ:** Khang: Căn hai mép thôi. Nút cứ để đấy.
- **p10-04:** Cận mặt Phong nhìn từ tay Khang xuống chuột. Tay Phong đặt lên chuột nhưng chưa bấm; giữ đúng bàn tay và hướng chuột cho đầu p11. Một bóng ngắn phía trên. **Đặt chữ:** Phong: Dạ, để em thử trước.

#### p11 — Một nhịp chờ

Ba panel theo nhịp co–giãn: hàng trên cao 42% chia trái hẹp 32% (panel 1), phải 68% (panel 2); panel 3 toàn ngang 58%. Không nhảy giờ giữa câu ở p10 và cú bấm. Dành ô lớn nhất cho chờ, không cho kết quả hiện sớm.

- **p11-01:** Cận đúng bàn tay trên chuột từ p10, ngón trỏ bấm lần một. SFX nhỏ sát chuột. **Đặt chữ:** SFX: Cạch.
- **p11-02:** Cận lưới lịch và chấm xử lý rất nhỏ, chưa có thẻ kép. Giữ mép màn hình và ánh sáng đã lập; không in chữ hoặc số. **Đặt chữ:** Không chữ.
- **p11-03:** Khung rộng hơn theo trục cũ: Phong chờ, ngón trỏ vẫn hờ trên chuột, mặt hơi nghiêng về màn hình. Có thể thấy sổ xanh cạnh phím. Để khoảng tĩnh phía phải và một ô nghĩ nhỏ; không đưa người khác vào. **Đặt chữ:** Phong (nghĩ): Ủa, bấm rồi mà?

#### p12 — Khoan, để nguyên

Bốn panel: hàng trên 39% toàn ngang; hàng giữa 35% chia trái 57% và phải 43%; hàng dưới 26% toàn ngang. Đọc trên xuống, trái sang phải ở hàng giữa. Nối cử chỉ đang lơ lửng ở p11 với lần bấm hai, rồi chặn Phong trước khi mất dấu lỗi.

- **p12-01:** Khung qua vai cùng trục p11: ngón tay bấm lần hai, thấy hai thẻ khác màu trong cùng một ô. Hai thẻ chỉ gối nhẹ; chưa in giờ hoặc mã. Đặt SFX gần tay, không lấp ô. **Đặt chữ:** SFX: Cạch.
- **p12-02:** Cận Phong nhìn ngạc nhiên, chỉ ô lịch rồi định đưa tay về chuột. Một bóng ngoài màn hình. **Đặt chữ:** Phong: Chị Thảo, em tải lại nha? Nó ra hai cái nè.
- **p12-03:** Cận Thảo tới từ lối đi, giơ bàn tay ra hiệu dừng, không chạm Phong. Chừa một bóng rõ phía trên. **Đặt chữ:** Thảo: Khoan. Để nguyên cho chị xem.
- **p12-04:** Khung ngang đầu–vai ở đúng bàn: Thảo cúi vừa đủ để cùng nhìn; Phong rời tay khỏi chuột, kéo sổ xanh tới. Bóng Thảo đúng hướng; kết bằng câu hỏi để p13 trả lời. **Đặt chữ:** Thảo: Em vừa bấm mấy lần?

#### p13 — Hai mã, một khung giờ

Bốn panel: 1 toàn ngang cao 44%; hàng hai cao 32% chia trái 63% và phải 37%; 4 toàn ngang cao 24%. Cho người đọc thấy bằng chứng lớn trước khi rời bàn; việc chuyển cảnh có lý do và lỗi được lưu lại.

- **p13-01:** Cận thẳng màn hình: một ô 14:30, hai thẻ khác màu có đủ chỗ cho A17 và B24, không đè chữ lên nhau. Bóng Phong ngoài UI, không in lời Thảo từ trang trước. **Đặt chữ:** UI: 14:30 / A17 / B24. • Phong: Hai lần ạ. Lần đầu không thấy gì.
- **p13-02:** Thảo giữ mắt trên màn hình, chỉ vào biểu tượng chụp ảnh dạng hình học. Phong nghe, hai tay tách khỏi chuột. Chừa bóng trên Thảo. **Đặt chữ:** Thảo: Chụp lại ô này rồi gửi chị nha. Chưa cần sửa gì hết.
- **p13-03:** Cận ngón tay Phong nhấn tổ hợp phím; thấy mép sổ xanh kê cạnh phím. Không biến thành lần bấm chuột thứ ba. Không chữ UI. **Đặt chữ:** Không chữ.
- **p13-04:** Rộng theo trục bàn: ảnh đã lưu, Phong gập sổ; Đạt dừng ở lối đi gọi Phong và Nhi. Bóng Đạt phía lối đi. Giữ ánh chiều; không nhắc tên hoặc dáng Dũng. **Đặt chữ:** Đạt: Hai em xong thì qua phòng họp gặp anh một lát nhé.

#### p14 — Cửa mở

Ba panel bất đối xứng: hàng trên cao 72%, trái 64% là panel 1 từ ngưỡng cửa, phải 36% là panel 2 cận; hàng đáy cao 28% là panel 3 ngang. Đọc trái → phải → dưới. Mở lại cảnh bằng cue địa điểm và sổ xanh, không kể lại lỗi. Giữ cú lộ mặt cho p15.

- **p14-01:** Nhìn từ ngưỡng cửa thấy phòng họp đúng mặt bằng, bàn kéo sâu vào khung. Phong và Nhi đang tới hai ghế cạnh nhau; Phong đặt sổ xanh xuống, Đạt ở đầu bàn. Caption nhỏ trên trái ngoài vùng mặt. Không có Dũng trong khung. **Đặt chữ:** Caption: Một lát sau, tại phòng họp. • Đạt: Hai em ngồi đi.
- **p14-02:** Cận tay Phong miết cạnh sổ, Nhi ghé sát vừa đủ, không cười trêu. Bóng thì thầm ngắn nằm gọn trong ô hẹp, bóng Phong thấp hơn. **Đặt chữ:** Nhi (thì thầm): Ông run nữa hả? • Phong: Đâu có.
- **p14-03:** Dải cuối chỉ thấy tay đẩy cánh cửa, tay áo sẫm và đồng hồ, lấy ánh đèn hành lang làm tương phản. Không vẽ mặt, bóng người hay phản chiếu nhận diện. Bóng Đạt từ ngoài khung. **Đặt chữ:** Đạt (ngoài khung): Mời anh.

#### p15 — À. Sếp.

Ba panel: hàng trên cao 32%, trái 62% là panel 1 ở cửa, phải 38% là panel 2 phản ứng; panel 3 toàn ngang 68%. Nối hành động mở cửa rồi dành phần lớn trang cho ánh mắt; không dùng hồi tưởng để giải thích câu đùa.

- **p15-01:** Dũng bước hết nửa bước qua cánh cửa p14, đúng áo sẫm và đồng hồ; Đạt nghiêng về hai người mới. Chừa bóng Đạt, không in chức danh như bảng tên. **Đặt chữ:** Đạt: Hai em, đây là anh Dũng, CEO bên mình.
- **p15-02:** Cận Phong nhận ra người lúc sáng, tay ngừng miết cạnh sổ; tai ửng nhẹ, mắt mở thêm một chút. Một bóng nhỏ phía trên, không che mắt. **Đặt chữ:** Phong: Dạ… em chào anh.
- **p15-03:** Khung lớn ngang: Phong nhìn lên, Dũng bắt gặp ánh mắt, cười vừa đủ. Đạt mở tập giấy, Nhi vẫn về phía Đạt. Để khoảng trống giữa hai ánh mắt rồi đặt bóng của Dũng phía trên, ý nghĩ Phong nhẹ ở dưới. Không flashback hay thêm đối thoại. **Đặt chữ:** Dũng: Lần này mới tính là họp nhé. • Phong (nghĩ): À. Sếp.

### Kiểm trước khi xuất

- [ ] Đủ 15 trang, bìa riêng và đúng số panel từng trang.
- [ ] Cảnh chào đủ tám người, không có Dũng. Danh tính CEO chỉ lộ ở p15.
- [ ] p06 chỉ liếc ngoài khung rồi quay mặt ngay; p07 hai khung lớn, không lộ bên trong buồng.
- [ ] Nhịp bấm lần một → chờ → bấm lại → hai mã đọc được qua p11–p13. Không đoán nguyên nhân.
- [ ] Chữ có dấu, đúng người, đủ chỗ đọc; không ghi đè ảnh cũ.

---

## Ghi chú rà cũ

**Phạm vi:** QA ban đầu đọc 14 trang và brief bìa. Sau khi chèn p05, các tham chiếu được đổi sang số trang hiện tại; trang chèn chưa qua QA phát hành. Báo cáo không đánh giá ảnh Go đã gen hoặc phản ứng độc giả. Các phát hiện dưới đây đã được sửa và rà lại ở bản hiện tại.

| Trang | Phát hiện | Sửa và kiểm lại |
| --- | --- | --- |
| p01 | Thẻ không đọc được vì “lật sai mặt” thiếu nguyên nhân nhìn thấy được. | Để thẻ cách mặt đọc rồi áp sát; tiếng tít và vai hạ thay lời giải thích. |
| p02–p03 | Cảnh chào có đủ tên nhưng p03 dồn năm dải mỏng; câu về Nam nghe như punchline viết sẵn. | Giữ toàn cảnh đủ tám người, không Dũng. Chia p03 thành bốn hàng, hai ô nhỏ đọc trái → phải ở hàng ba. Minh nói từ trải nghiệm suýt ngã, Nam giúp bằng việc đẩy ghế. Kiểm lại chỗ đặt bóng thoại ở hai ô nhỏ. |
| p06–p07, p15 | Cái liếc đủ rõ nhưng nếu Dũng cười thẳng vào Phong, cảnh dễ đọc thành trêu quê. Câu nhắc “biên bản” dễ thành lời nhắc hộ độc giả. | Giữ insert im và cú quay ngay ở p06. p07 chỉ hai khung; Dũng đáp về phía cửa để Phong có một nhịp lấy lại bình tĩnh rồi nhìn lên. p15 trả câu đùa bằng “Lần này mới tính là họp nhé”, không kể lại việc hôm sáng. Chức danh chỉ được nói ở p15. |
| p08–p10 | Câu tính tiền giao không hợp vì hai người cùng đi bộ; lý do giữ nút hơi chung chung. | Đổi sang tính công đi bộ và trả công bằng miếng trứng. Trân nói rõ có khách đang đợi ở quầy, để người đọc hiểu chuyện IT có hệ quả ngoài màn hình. |
| p11–p15 | Hai móc dễ giẫm lên nhau nếu lỗi đã được giải thích hoặc Dũng được nhận diện ở p14. | Giữ chuỗi chờ → bấm lại → hai mã; Thảo chỉ yêu cầu giữ bằng chứng. Trang 14 chỉ có tay áo và đồng hồ. Trang 15 mới trả câu hỏi “người đó là ai?”. |

**Còn phải kiểm trên ảnh:** p02 đủ tám người và không nhầm nhận diện; p03 đọc đúng hai ô kề; p06–p07 không lộ đích nhìn hoặc bên trong buồng; p13 in đúng `14:30`, `A17`, `B24`; thoại và biểu cảm p15 đủ kín đáo. Chưa có phản hồi độc giả để xác nhận sức hút của cảnh.

### Rà nhịp phần sau cảnh WC (p08–p15)

- **p07 → p08:** “Đến giờ trưa” nối về kế hoạch ăn đã gieo ở p04; không cần thêm một trang dẫn ra khỏi WC.
- **p08 → p10:** dây mạng được nhắc trước khi Minh đem tới; cửa pantry nối về bàn, rồi góc nhìn nút cuối p09 dẫn thẳng vào câu hỏi đầu p10.
- **p10 → p13:** tay trên chuột → bấm lần một → chờ → bấm lại → hai thẻ → hỏi số lần → giữ bằng chứng. Không chèn caption giữa các thao tác cùng cảnh.
- **p13 → p15:** Đạt gọi, Phong mang sổ, “Một lát sau, tại phòng họp” định vị lại. Tay đẩy cửa ở cuối p14 được nối ngay với Dũng bước vào; không lộ trước cú chốt.
- Layout phân biệt ô ngang chủ đạo, cặp ô ngang lệch và cặp ô bán dọc. Đã đối chiếu trật tự trong prompt; cần kiểm bố cục, dấu và khoảng thoại trên ảnh Go thật. Không sửa prompt hoặc nội dung p01–p07.

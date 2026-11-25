# Chap 02 — The Boss

**16 trang truyện + bìa + recap.** Hai sheet outfit chỉ để tham chiếu, không đăng cùng truyện. [Storyline](../../story-outline.md) · [Phục trang](../../outfit.md) · [Chỉ đạo truyện](../../manga-direction.md).

Mở một session Go mới. Gửi mục 00 với sáu ảnh, rồi gen lần lượt hai sheet ở mục 01 và đính lại: 07 công sở, 08 Dũng sau tập. Gửi tin nhắn khóa hai sheet trước khi làm bìa. Sau đó gửi **02 Bìa → 03 Recap → 04 p01–p16**. Một khối `text` mỗi lượt; tên file chỉ để lưu, không in. Nếu Go mất ảnh tham chiếu, đính lại đúng file và nêu đúng số, không đánh lại thứ tự. Không trông chờ Go mở đường dẫn local.

## 00 — Mở session: toàn bộ ngữ cảnh

| Ảnh | Tệp                                                                                | Dùng cho                                            |
| --- | ---------------------------------------------------------------------------------- | --------------------------------------------------- |
| 01  | [Comic art](../../assets/reference/go-pack/01-comic-art-style-guide.png)           | Nét manga màu, bóng mảng, chất liệu và biểu cảm.    |
| 02  | [Lettering](../../assets/reference/go-pack/02-lettering-style-guide.png)           | Mẫu thoại, Dẫn truyện, suy nghĩ và SFX tiếng Việt.  |
| 03  | [Mặt bằng](../../assets/reference/go-pack/03-it-office-floor-plan.png)             | Dãy bàn, phòng họp, pantry, cửa và vách kính.       |
| 04  | [Lineup chính](../../assets/reference/go-pack/04-office-lineup-phong-dung-dat.png) | Trái Phong, giữa Dũng, phải Đạt theo góc người xem. |
| 05  | [Thảo–Nhi–Trân](../../assets/reference/go-pack/05-thao-nhi-tran.png)               | Trái Thảo, giữa Nhi, phải Trân.                     |
| 06  | [Khang–Minh–Nam](../../assets/reference/go-pack/06-khang-minh-nam.png)             | Trái Khang, giữa Minh, phải Nam.                    |

```text
Đây là Commit Trái Tim, Chap 02 — The Boss. Lượt này chỉ nạp ngữ cảnh, chưa vẽ. Chờ prompt outfit.

Ảnh 01 comic art khóa nét manga màu, bóng mảng và độ ấm; ảnh 02 lettering dùng cho tiếng Việt, không chép chữ mẫu; ảnh 03 sơ đồ dùng để giữ vị trí bàn, phòng họp, pantry và cửa. Ảnh 04: trái Phong (24 tuổi, tóc nâu đỏ, không kính), giữa Dũng (35, tóc tối, vai rộng, không kính), phải Đạt (33, tóc sẫm hơi rối, kính chữ nhật). Ảnh 05: trái Thảo, giữa Nhi, phải Trân. Ảnh 06: trái Khang, giữa Minh, phải Nam. Hướng trái/phải là từ phía người xem ảnh. 04–06 khóa nhận diện và vóc dáng; sheet 07 sẽ khóa quần áo công sở; sheet 08 chỉ cho Dũng sau tập. Không đưa tất cả người trong sheet vào mọi tranh.

Từ Chap 01: Phong và Nhi vào làm. Phong gặp Dũng trong WC, nói vấp rồi tới cuối ngày mới biết anh là CEO. Trên màn đặt lịch thử, Phong bấm một lần mà chưa thấy gì, bấm lại và thấy hai thẻ chung ô 14:30. Cậu đã chụp lại; chưa ai biết hệ thống có lưu hai lượt hay chỉ hiển thị lặp. Chap này không dựng lại cảnh WC, không tỏ tình hay cho hai người đụng chạm.

- p01–p02, sáng hôm sau, cửa kính và dãy bàn: Phong đã quẹt thẻ qua nhưng quên buông, Nhi chọc. Cậu chỉ kể một chuyện chào hỏi kỳ cục, Minh nghe nửa câu rồi trêu. Đạt gọi vào họp.
- p03–p06, phòng họp: Đạt hướng dẫn cách báo việc; Nhi hỏi một câu rất thật, Đạt trả lời nghiêm túc. Dũng tới nghe cập nhật. Phong né mắt nhưng lúc được hỏi vẫn nói đúng hai lần bấm và điều mình thấy. Dũng phân biệt hiện hai thẻ với đặt trùng thật; Đạt giao Phong dựng lại các bước với Thảo và Nam xem riêng phần căn nút.
- p07–p10, dãy bàn: Thảo muốn thử trước vì sợ hai khách tới cùng giờ. Nam không muốn gắn mức khẩn khi chưa biết có hai lượt lưu; hai người thống nhất lấy kết quả đối chiếu làm căn cứ. Trân giải thích áp lực ở quầy; Khang chỉ hình dấu chờ và dấu đã lưu. Nhi hỏi lễ tân phải trả lời khách thế nào khi màn hình im, sau đó lo mình hỏi nhiều. Đạt dùng đúng câu Nhi hỏi khi chốt thêm bước cần quan sát. Phong tự ghi lại, không chẩn đoán nguyên nhân hay tạo dữ liệu log mới.
- p11, sau giờ nghỉ trưa: Nhi kể lại nỗi lo; thấy câu mình hỏi được giữ trong phần thử thì nhẹ người. Minh trêu CEO nhớ tên Phong, không biết chuyện WC. Phong cầm sổ đi lấy nước.
- p12–p14, pantry ngay sau giờ nghỉ: Dũng vừa tập xong, đã đổi khỏi bộ đi họp sang D-02-GYM, áo gym đen đục vừa người, short charcoal, giày training đen; tóc hơi ẩm, khăn trên vai trái, chai nước trên kệ thấp. Đây là nhịp attraction/tension 1–2: thấy sự khác biệt qua vai áo và giọt nước ở thái dương trong một khung vừa, không tách cơ thể thành nhiều cận cảnh. Phong nhìn lâu hơn dự tính, bắt gặp mắt anh rồi quay sang chồng cốc, lỡ rút hai cốc. Dũng thấy nhưng không bình phẩm; hỏi chuyện buổi họp, tự dịch sang để Phong có chỗ đứng và đợi cậu đáp. Phong tự đùa nhẹ, Dũng cười, hai người biết nói chuyện ngoài vai trò sếp/nhân viên. Đạt đi ngang vừa lúc Dũng gọi Phong quay lấy sổ, chỉ nghe giọng khác lúc họp, không nghe đoạn riêng.
- p15–p16: Đạt hỏi Phong có vướng nghiệp vụ không rồi đi. Cuối buổi, Dũng đã thay lại bộ công sở; Đạt đưa sổ việc tuần, định rời. Khi chỉ còn hai người, Dũng hỏi “Cậu nhân viên mới tên Phong, làm việc thế nào?” Đạt mới thật sự dừng bước. Cắt trước câu đáp, không vẽ ghen hoặc người nghe lén.

Continuity: sổ Phong xanh đậm, sổ Đạt xám; Phong mang sổ xanh sang pantry, đặt xuống rồi quên, quay lại lấy ngay. Phong chỉ dùng một cốc giấy sau khi trả cốc dư; cốc đã có nước ở p14–p15. Khăn và chai là của Dũng, không sang dãy bàn. Outfit 07 dùng cho toàn team; đổi riêng Dũng sang 08 ở p12–p14, p16 trở lại 07 sau bước nhảy cuối chiều. Recap nói về ngày đầu, không dùng 07–08. Không cho Go thêm nụ hôn, chạm người, lời tỏ tình hay cảnh tập/thay đồ. Dùng thoại Việt theo từng page, một lượt một ảnh. Trang dọc 4:5, đọc trên xuống, trái trước phải trong cùng hàng. Không in các nhãn sản xuất.
```

## 01 — Thiết kế và khóa outfit

### 01A — Công sở, ảnh 07

Dùng ảnh 01, 04, 05, 06. Lưu sheet đã chọn `art/wardrobe.png`. Đây là `Day 1 — Office day` của chương trong `outfit.md`, tức ngày đi làm kế tiếp trong truyện.

```text
Tạo MỘT sheet trang phục khổ ngang 3:2, lưới 3 hàng × 3 cột, mỗi người toàn thân, tỷ lệ máy như nhau, chân cùng đường sàn trong mỗi hàng; nền kem trơn, rãnh tách thoáng, dáng đứng tự nhiên. Mỗi hàng đọc trái qua phải. Giữ mặt, tóc, kính, da, râu và vóc dáng như ảnh gốc; không đổi tỷ lệ cơ thể theo áo. ID chỉ để định vị, không in ID/tên/chữ/logo.
Hàng 1 — trái Phong P-02 (04 trái): thun trắng ngà, overshirt navy mở cúc, chinos beige, sneaker trắng; dây thẻ công ty đen trơn khi làm việc là đạo cụ nối từ Chap 01. Giữa Dũng D-02 (04 giữa): polo đen vừa dáng, quần tây charcoal, đồng hồ kim loại, giày da casual tối, không kính. Phải Đạt DAT-02 (04 phải): polo navy, quần tây xám đậm, sneaker da tối giản, đồng hồ, kính chữ nhật.
Hàng 2 — trái Thảo TH-02 (05 trái): sơ mi xanh sage, quần tây đen, loafer, giữ kính. Giữa Nhi NHI-02 (05 giữa): thun mint, cardigan trắng mỏng, jeans xanh nhạt, sneaker trắng. Phải Trân TR-02 (05 phải): blouse xanh nhạt, chân váy midi beige, giày bệt.
Hàng 3 — trái Khang K-02 (06 trái): sơ mi sọc dọc đen–trắng dáng relaxed, quần đen ống thẳng, sneaker đen–trắng, vòng tay nhỏ. Giữa Minh M-02 (06 giữa): hoodie xám nhạt, jeans xanh đậm, sneaker trắng, giữ vóc dáng và kính. Phải Nam NAM-02 (06 phải): sơ mi navy trơn, xắn tay nhẹ, quần đen, sneaker xám, giữ kính và dáng riêng.
Đừng nhầm polo của Đạt với Dũng hay sơ mi của Nam; không thêm cardigan nam, suit, cà vạt hoặc đồ gym. Không tạo bìa hay trang truyện.
```

### 01B — Dũng sau tập, ảnh 08

Lưu `art/wardrobe-gym.png`. D-02-GYM dùng thiết kế gym D-06B theo phụ lục cho cảnh **cùng ngày**. Không đưa chi tiết phòng tập của Chap 06 vào truyện Chap 02.

```text
Tạo một sheet toàn thân duy nhất cho Dũng trưởng thành (35 tuổi), nền kem trơn. Dùng đúng người giữa ảnh 04 làm nhận diện: cùng mặt, tóc tối, râu lún phún, vai rộng, vóc dáng thực tế; không kính. D-02-GYM: áo thun gym đen đục, vừa vai và ngực tự nhiên, quần short training charcoal, sneaker training đen. Tóc hơi ẩm ở thái dương; khăn tập xám sáng vắt trên vai trái, chai nước trơn màu sẫm cầm tay phải để kiểm đạo cụ; không đồng hồ công sở. Đứng thoải mái, không gồng cơ, không vén áo. Chất vải không xuyên thấu. Không phông gym, chữ, logo hoặc người khác. Đây chỉ là sheet khóa đồ và đạo cụ cho p12–p14.
```

Đính hai sheet đã chọn rồi gửi:

```text
Ảnh 07 là wardrobe.png: hàng trên Phong P-02 / Dũng D-02 / Đạt DAT-02; hàng giữa Thảo TH-02 / Nhi NHI-02 / Trân TR-02; hàng dưới Khang K-02 / Minh M-02 / Nam NAM-02. Ảnh 08 là wardrobe-gym.png, chỉ có Dũng ở D-02-GYM; chỉ dùng cho Dũng p12–p14 sau giờ nghỉ. Bìa, họp và p16 dùng Dũng 07. Phong và các nhân vật khác luôn giữ 07 trong ngày này. 04–06 vẫn khóa nhận diện, recap không dùng outfit mới. Chỉ xác nhận và đợi prompt bìa.
```

## 02 — Bìa (`art/cover.png`)

```text
Vẽ MỘT bìa manga màu dọc 4:5, không panel. Dùng 01 cho nét, 02 cho lettering, 03 cho phòng họp, 04 cho mặt/dáng, 07 cho P-02, D-02, DAT-02. Máy từ ngang bàn phòng họp: tiền cảnh lệch trái là Phong sơ mi khoác mở navy, tay đặt mép sổ xanh mở, quay mắt về người đang hỏi nhưng chưa kịp ngước hẳn. Lớp giữa bên phải là Dũng polo đen, vai rộng, đang lắng nghe chứ không tạo dáng quyền lực; mắt nhìn Phong, chưa cười. Đạt ở lớp sau, polo navy và kính, đang xoay một tờ ghi việc trên bàn; anh có việc riêng, không đứng giữa hai người như ngăn họ. Nhấn mặt Phong và hướng nhìn chéo; để bàn và vách kính làm chiều sâu. Ánh sáng văn phòng ban sáng, phản sáng ấm nhẹ, không ám màu đổi áo. Chừa phần tư trên ít chi tiết, chữ rõ ở thumbnail. Chỉ in ba dòng: Commit Trái Tim / Chap 02 / The Boss. Mỗi mục một dòng, không in dấu gạch chéo, không slogan, logo, chữ ngẫu nhiên, cảnh WC hay hé lộ câu hỏi cuối chap.
```

## 03 — Tập trước (`art/recap.png`)

Có thể đính thêm [p01 Chap 01](../ep-001/art/p01.png) trong lượt này, chỉ để so kiểu/cỡ của ô lời dẫn; không đổi số 01–08 hoặc lấy cảnh, người và pose từ ảnh đó.

```text
Vẽ MỘT trang recap dọc 4:5. Một đoạn chữ đặt giữa trang, căn trái trong khối rộng khoảng 76–78%, nền kem nhạt, chữ nâu đen dễ đọc trên điện thoại. Không panel, rãnh, bong bóng hoặc chữ thư pháp. Dùng mẫu Dẫn truyện ở ảnh 02; nếu có p01 Chap 01 đính thêm thì so với ô lời dẫn góc trên trái cùng chiều rộng. Giãn dòng khoảng 1,35; tiêu đề cùng kiểu chữ và chỉ lớn hơn thân bài 15–20%. Không phóng to để lấp vùng trống. Tùy chọn một nét phác thẻ nhân viên hoặc lịch ở góc dưới, nhạt, ngoài vùng chữ; không vẽ người hay cảnh WC. Không dùng outfit 07 hoặc 08. Chỉ in tiêu đề và đoạn văn sau, giữ nguyên dấu và dấu câu:

Tập trước

Ngày đầu đi làm, Phong nói vấp khi chào một người áo đen trong nhà vệ sinh. Đến buổi họp cuối ngày, Phong mới biết người mình gặp ban sáng là Dũng, sếp tổng.

Không logo, số trang, chữ UI hay lời thoại. Nếu được yêu cầu bản nền, bỏ toàn bộ chữ nhưng giữ đúng khoảng trống để đặt chữ thủ công.
```

## 04 — Từng page

### p01 — Sáng hôm sau

Lưu `art/p01.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p01 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 42%, giữa chia trái 45% phải 55% cao 27%, dưới ngang 31%.
Cảnh / continuity: Cửa kính buổi sáng, Phong và Nhi theo 07. Nhắc cảm xúc hôm qua bằng sự phân tâm, không flashback.

Panel 1 — Hình: Góc rộng từ sảnh: cửa đã hé, đèn đầu đọc xanh. Phong bước qua mà vẫn kẹp mép thẻ giữa hai ngón; Nhi theo sát phía sau một bước. Giữ khoảng trên trái cho caption, không in nhãn cửa.
Chữ theo thứ tự: Caption: Sáng hôm sau. • SFX: Tít!

Panel 2 — Hình: Cận hai ngón tay Phong chưa chịu buông thẻ. Nhi ló qua mép khung, nhìn tay chứ không chỉ vào mặt cậu.
Chữ theo thứ tự: Nhi: Thả nó ra đi ông. Qua cửa rồi.

Panel 3 — Hình: Cận đầu–vai Phong nhìn xuống thẻ rồi buông tay, bật cười vì vừa bị bắt quả tang. Overshirt navy mở, áo trong trắng ngà.
Chữ theo thứ tự: Phong: Tui tưởng chưa quẹt.

Panel 4 — Hình: Hai người đi vào theo cùng trục. Nhi liếc ngang khi Phong đi chậm lại, giọng tò mò chứ không dò xét.
Chữ theo thứ tự: Nhi: Hôm qua về ông còn tỉnh mà. Có chuyện gì hả? • Phong: Lát tới bàn kể.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p02 — Chào tới hai lần

Lưu `art/p02.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p02 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 32%, giữa chia 56/44 cao 35%, dưới ngang 33%.
Cảnh / continuity: Dãy bàn; Phong, Nhi, Minh, Đạt theo 07. Minh chỉ nghe câu cuối, chưa biết người kia là Dũng hay nơi gặp.

Panel 1 — Hình: Phong đặt sổ xanh cạnh bàn phím và kéo ghế ngồi. Nhi tựa bên bàn mình, chờ Phong nói hết, không ghé tai.
Chữ theo thứ tự: Phong: Hôm qua tui gặp một anh. Chào có một tiếng mà nói vấp mấy lần.

Panel 2 — Hình: Phong lật sổ che nửa nụ cười; Nhi hơi nhướng mày. Rãnh trống giữa hai mặt cho hai bóng ngắn.
Chữ theo thứ tự: Nhi: Rồi? • Phong: Cuối ngày gặp lại. Tui phải chào thêm lần nữa.

Panel 3 — Hình: Minh ngang qua với cốc trên tay, nghe đúng đoạn cuối. Anh cười và đi chậm nửa bước, không đứng chen vào giữa hai người.
Chữ theo thứ tự: Minh: Mới đi làm ngày đầu mà đã có màn chào tập hai hả em?

Panel 4 — Hình: Đạt gọi từ đầu lối đi, polo navy và sổ xám; Phong chộp sổ xanh như được cứu. Nhi ngoái sang Phong, môi mím vì nhịn cười.
Chữ theo thứ tự: Đạt: Mình họp nha mọi người. Phong, Nhi, mang sổ theo luôn.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p03 — Nói tới chỗ mình biết

Lưu `art/p03.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p03 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 3 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 47%, dưới chia 54/46. Hàng cuối đọc trái rồi phải.
Cảnh / continuity: Phòng họp, đúng tám người: Đạt, Phong, Nhi, Thảo, Nam, Trân, Khang, Minh. Dũng chưa vào. Cửa kính phía sau chỗ Đạt, giữ trục đến khi tan họp.

Panel 1 — Hình: Toàn từ cửa thấy Đạt ở đầu bàn; Phong và Nhi kề nhau một bên, các ghế còn lại theo mặt bằng, không nhân viên nền. Đạt mở sổ xám, giới thiệu việc tuần này; bóng phía trên, không che mặt.
Chữ theo thứ tự: Đạt: Tuần này ưu tiên màn đặt lịch. Mình nói ngắn thôi: đang làm gì, có vướng gì không.

Panel 2 — Hình: Nhi nhấc tay khỏi mặt bàn, chần chừ mới hỏi. Đạt quay về phía cô, trả lời như câu hỏi bình thường; Phong mở sổ xanh, im.
Chữ theo thứ tự: Nhi: Em mới thử được một nửa thì báo sao anh? • Đạt: Thử tới đâu nói tới đó. Chỗ nào chưa rõ thì hỏi luôn.

Panel 3 — Hình: Cận bút Phong vừa chạm giấy thì cửa ngoài khung bật nhẹ. Tay dừng, không in chữ trên sổ.
Chữ theo thứ tự: SFX: Cạch.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p04 — Anh ghé nghe thôi

Lưu `art/p04.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p04 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 3 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Ô trên ngang 43%, hai ô dưới 45/55. Cùng hướng cửa và chỗ ngồi p03.
Cảnh / continuity: Dũng D-02 bước vào phần cập nhật; Phong đã biết chức vụ từ hôm qua. Không ai nhắc WC.

Panel 1 — Hình: Dũng bước qua cửa, polo đen, đồng hồ kim loại, cầm tập giấy. Đạt nhích ghế cạnh mình. Dũng đặt giấy xuống, vai thẳng nhưng không tạo dáng; câu nói hướng cả bàn.
Chữ theo thứ tự: Dũng: Mọi người cứ ngồi. Anh ghé nghe phần đặt lịch thôi.

Panel 2 — Hình: Cận Phong nhận ra anh, mắt vừa chạm đã dời về sổ. Hơi mím môi, bút chạm nguyên một điểm; chưa cần đỏ mặt.
Chữ theo thứ tự: Không chữ.

Panel 3 — Hình: Dũng ngồi cạnh Đạt, nhìn về phía Phong, không cười trêu, không nghiêng vào khoảng riêng. Chừa ô chữ trên vách kính ngoài các mặt.
Chữ theo thứ tự: Dũng: Phong, hôm qua em gặp lỗi ở màn đặt lịch đúng không?

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p05 — Em thấy hai thẻ

Lưu `art/p05.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p05 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 30%, giữa chia 48/52 cao 28%, dưới ngang 42%.
Cảnh / continuity: Câu hỏi p04 có đáp ngay. Phong bắt đầu hơi căng, rồi nói rõ mình thấy gì thay vì đứng hình.

Panel 1 — Hình: Phong ngẩng lên chậm một nhịp, giữ mép sổ bằng hai ngón. Nhi nhìn cậu rồi quay về sổ mình; Đạt không chen.
Chữ theo thứ tự: Phong: Dạ. Lần đầu em bấm thì màn hình không báo gì.

Panel 2 — Hình: Cận tay Phong chỉ hai dấu trong sổ. Chỉ nét gạch, không mã hoặc giờ trên giấy.
Chữ theo thứ tự: Phong: Em bấm lại thì nó hiện hai thẻ trong cùng một ô giờ.

Panel 3 — Hình: Dũng chuyển mắt từ Phong sang sổ, đặt bút xuống. Tông hỏi bằng chứng, không truy lỗi cá nhân.
Chữ theo thứ tự: Dũng: Mình biết là đặt trùng thật, hay mới thấy hai thẻ thôi?

Panel 4 — Hình: Hai người ở hai đầu đường nhìn, khoảng giữa còn mặt bàn. Phong thả vai, nhìn lên khi trả lời. Không chiếu ảnh lỗi lên tường.
Chữ theo thứ tự: Phong: Em mới thấy hai thẻ thôi ạ. Em có gửi ảnh cho chị Thảo.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p06 — Tới đâu nói tới đó

Lưu `art/p06.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p06 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 29%, giữa chia 57/43 cao 35%, dưới ngang 36%.
Cảnh / continuity: Khép phần CEO, mở việc sau họp. Giữ đúng số thẻ đang thấy, không khẳng định bản sửa.

Panel 1 — Hình: Thảo từ chỗ ngồi gật nhẹ, giữ sổ tay mình; Dũng quay sang nghe. Chừa bóng Thảo, không che mặt Nam ở mép khung.
Chữ theo thứ tự: Thảo: Em có ảnh rồi. Để em hỏi Phong từng bước, rồi thử lại.

Panel 2 — Hình: Dũng gập tập giấy và nhìn cả bàn. Bóng ngắn về Dũng, ánh mắt không khóa vào Phong.
Chữ theo thứ tự: Dũng: Vậy kiểm tra giúp anh xem có đặt trùng thật không. Có kết quả báo anh nhé.

Panel 3 — Hình: Dũng ra qua cửa cũ với tập giấy. Phong nhìn theo nửa nhịp rồi quay lại khi Đạt mở sổ xám.
Chữ theo thứ tự: Không chữ.

Panel 4 — Hình: Đạt nhìn sang Phong rồi Nam, tay đánh dấu hai mục riêng trên sổ, không in chữ. Nhi tự ghi phần mình vừa hỏi.
Chữ theo thứ tự: Đạt: Họp xong Phong qua bàn Thảo nhé. Nam coi giúp phần căn nút. Hai việc tách riêng.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p07 — Khẩn hay chưa?

Lưu `art/p07.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p07 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 27%, giữa hai ô 52/48 cao 33%, dưới ngang 40%.
Cảnh / continuity: Sau họp, bàn Thảo. Thảo muốn ưu tiên do hậu quả với khách; Nam đòi phân loại bằng chứng, không gạt đi. Hai người thống nhất có việc làm ngay.

Panel 1 — Hình: Thảo mở ảnh chụp trên laptop, Phong mang sổ tới, Nam ở phía lối. Ảnh chỉ cần hai thẻ trong cùng ô, không in thêm mã. Một caption ngắn ghi thời điểm.
Chữ theo thứ tự: Caption: Sau buổi họp. • Thảo: Nam, cái này em muốn thử trước. Nếu lưu trùng, hai khách tới cùng giờ thì sao?

Panel 2 — Hình: Cận Nam hơi kéo ghế ra để nhìn ảnh, ngón tay giữ ở mép bàn. Anh không lắc đầu hay cười nhạt.
Chữ theo thứ tự: Nam: Thử trước thì được. Nhưng khoan ghi khẩn khi chưa biết có lưu hai lần thật không.

Panel 3 — Hình: Thảo nhìn Nam, gật riêng một cái rồi xoay laptop cho cả hai cùng xem. Giữ nhịp nhanh, không tạo vẻ thắng thua.
Chữ theo thứ tự: Thảo: Ừ. Lát em thử, anh coi bên lưu lịch giúp em nhé.

Panel 4 — Hình: Phong ghi cách mô tả; Nam hạ tay rồi dừng lại nghe Phong. Hai bóng theo đúng lượt, chữ ngắn.
Chữ theo thứ tự: Phong: Vậy em ghi “hiện hai thẻ cùng giờ”, chưa ghi “đặt trùng” nha chị? • Thảo: Đúng rồi.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p08 — Khách còn đứng đó

Lưu `art/p08.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p08 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 35%, giữa chia 50/50 cao 26%, dưới ngang 39%.
Cảnh / continuity: Nối việc cần thử bằng góc nhìn người dùng. Trân, Khang, Phong, Nhi theo 07. Hình tròn và dấu kiểm là bản phác, không phải tính năng đã có.

Panel 1 — Hình: Trân kéo một ghế cạnh bàn, đặt giấy phác ở giữa. Cô chỉ vào ô cũ rồi ô mới bằng hai ngón, nói như đang nghĩ hộ người ở quầy.
Chữ theo thứ tự: Trân: Lễ tân đổi giờ ngay trước mặt khách. Họ phải biết đã lưu chưa để còn hẹn người ta.

Panel 2 — Hình: Qua vai Khang: hai hình phác trên tờ nhỏ, vòng chờ và dấu kiểm. Sọc áo và vòng tay đúng sheet; không in UI.
Chữ theo thứ tự: Khang: Một cái là đang chờ, một cái là xong. Màn im thì ai biết được.

Panel 3 — Hình: Cận Nhi nhìn dấu chờ, định hỏi rồi nhìn lên Trân. Đừng biến ngập ngừng thành mếu; hai tay cô vẫn ở mép bàn.
Chữ theo thứ tự: Không chữ.

Panel 4 — Hình: Hai người mới nhìn cùng tờ phác. Nhi hỏi nghiêm túc; Phong đang ghi thì dừng bút như nhận ra mình cũng chưa nghĩ tới.
Chữ theo thứ tự: Nhi: Nếu khách đứng chờ mà màn hình cứ im, lễ tân nói sao với khách hả chị?

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p09 — Câu đó giữ lại

Lưu `art/p09.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p09 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Hai ô trên 55/45 cao 40%, giữa ngang 23%, dưới ngang 37%.
Cảnh / continuity: Trân không nghĩ ra đáp án giả. Câu hỏi của Nhi đổi việc team cần quan sát; p10 trả giá trị thực tế của nó.

Panel 1 — Hình: Trân nhìn thẳng Nhi, bàn tay mở trên tờ giấy. Không vẽ tranh quầy lễ tân mới; chỉ bàn làm việc.
Chữ theo thứ tự: Trân: Chị cũng chưa dám bảo họ bấm lại. Phải biết lần đầu có lưu không đã.

Panel 2 — Hình: Thảo bước đến vừa đủ nghe, giữ ảnh chụp cạnh tờ phác. Bóng hướng về Thảo, không lẫn với Trân.
Chữ theo thứ tự: Thảo: Nhi, giữ câu đó nha em. Lúc thử chị muốn coi kỹ đoạn màn hình im.

Panel 3 — Hình: Nhóm tản bớt. Nhi kéo ghế về bàn, vòng tay qua lưng ghế rồi mới khẽ quay sang Phong. Không chữ.
Chữ theo thứ tự: Không chữ.

Panel 4 — Hình: Cận hai người mới ở bàn cạnh nhau. Nhi hạ giọng; Phong đặt bút xuống, đáp thẳng rồi nhoẻn cười một chút.
Chữ theo thứ tự: Nhi: Tui hỏi hoài, mọi người có thấy phiền không ta? • Phong: Câu hồi nãy tui cũng muốn hỏi mà chưa dám.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p10 — Từ lúc mở lịch

Lưu `art/p10.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p10 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 5 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 25%, giữa chia 58/42 cao 29%, hai dải dưới 22% và 24%.
Cảnh / continuity: Đạt củng cố vai mentor bằng việc để Phong tự dẫn người đọc đi lại các bước. Nam góp ý cách trình bày; Nhi thấy câu mình hỏi có ích.

Panel 1 — Hình: Đạt ở phía lối đi, kính chữ nhật và sổ xám. Phong tự xoay sổ xanh về anh, Đạt không với lấy bút.
Chữ theo thứ tự: Đạt: Đưa sổ này cho người chưa thấy lỗi, họ bắt đầu ở đâu em?

Panel 2 — Hình: Qua vai Phong thấy lịch thử trên laptop và hai dấu trong sổ, không UI đọc được. Tay cậu lần về đầu trang.
Chữ theo thứ tự: Phong: Từ lúc mở lịch. Để em ghi lại cả chỗ em chọn giờ trước khi bấm.

Panel 3 — Hình: Đạt nhìn sang Nhi ở bàn kế, chạm đầu ngón vào dòng trống chứ không viết hộ. Nhi dừng gõ phím, nghe rõ.
Chữ theo thứ tự: Đạt: Ghi luôn lúc chưa có thông báo. Cái Nhi hỏi hồi nãy đó.

Panel 4 — Hình: Nam đặt bản ghi phần căn nút cạnh bàn phím Phong, hai tờ có nét gạch không thành chữ. Anh nói gọn rồi rút tay.
Chữ theo thứ tự: Nam: Còn phần căn nút em ghi riêng. Kẻo đọc một hồi tưởng sửa nút là hết lỗi.

Panel 5 — Hình: Cận Phong tự chia trang sổ làm hai phần, thả vai. Nhi ở mép khung nhìn sang, khóe miệng nhấc nhẹ. Không giải bug.
Chữ theo thứ tự: Phong: Rồi. Căn nút một bên, lỗi đặt lịch một bên.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p11 — Được nhớ tên

Lưu `art/p11.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p11 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 31%, giữa chia 52/48 cao 31%, dưới ngang 38%.
Cảnh / continuity: Sau giờ nghỉ trưa. Trả nỗi lo của Nhi rồi để Minh pha một câu. Hướng đi và sổ nối sang pantry. Chưa vẽ Dũng.

Panel 1 — Hình: Ánh sáng sau trưa trên cụm bàn. Nhi thấy Phong gạch riêng một dòng dưới hai dấu trong sổ. Cả hai vẫn 07, không ai cầm cốc giấy của Phong.
Chữ theo thứ tự: Caption: Sau giờ nghỉ trưa. • Nhi: Vậy câu của tui có vô phần thử thiệt hả? • Phong: Vô rồi. Chiều Thảo coi đúng khúc đó.

Panel 2 — Hình: Minh ngang qua, nâng cốc mình như cụng gió. Chọc vì nghe cuộc họp, không nhìn Nhi như đồng phạm.
Chữ theo thứ tự: Minh: Mới ngày thứ hai mà sếp nhớ tên. Hồi anh mới vô, ảnh gọi “em bên IT” cả tuần.

Panel 3 — Hình: Nhi cười thật lần đầu từ đoạn ngại hỏi. Minh liếc cốc rồi cười theo; đừng phóng đại thành chibi.
Chữ theo thứ tự: Nhi: Tại hồi nào kiếm anh cũng thấy cái cốc trước.

Panel 4 — Hình: Phong bật cười, gập sổ xanh và cầm đi về phía pantry. Nhi quay về bàn. Đặt bóng phía sau vai Phong; không thêm chuyện riêng.
Chữ theo thứ tự: Phong: Tui đi lấy nước. Bà giữ ghế giùm tui nha.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p12 — Khác lúc ở đầu bàn

Lưu `art/p12.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p12 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 3 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Ba ô: trên ngang 54%, giữa dải cận ngắn 17%, dưới ngang 29%. Khung lớn là người trong không gian, không phải ảnh khoe cơ thể.
Cảnh / continuity: Pantry sau giờ nghỉ. Dũng vừa tập về, dùng ảnh 08; Phong vẫn P-02 ảnh 07. Đây là lần đầu thấy Dũng mặc đồ tập. Máy ngang tầm mắt, ánh sáng từ cửa sổ; giữ Dũng ở trái cạnh kệ thấp, cửa và chồng cốc ở phải.

Panel 1 — Hình: Toàn vừa từ phía sau vai Phong ở ngưỡng cửa: Dũng đang cúi nhẹ lấy chai nước trơn từ kệ thấp, tay kia giữ mép khăn xám trên vai trái cho khỏi rơi. Áo thun gym đen đục hiện dáng vai khi anh với tay, short training charcoal chỉ xuất hiện tự nhiên trong khung. Tóc hơi ẩm, một giọt nước nhỏ ở thái dương. Trung tâm là động tác lấy chai và mặt Dũng khi bắt đầu ngẩng; không pose, không cắt cận thân thể. Phong cầm sổ xanh, dừng ở ngưỡng. Để im.
Chữ theo thứ tự: Không chữ.

Panel 2 — Hình: Cận đầu–vai Phong: mắt Phong dừng một nhịp rồi chạm đúng mắt Dũng đang ngẩng lên; ngón cái siết mép sổ, môi vừa hé thì khép lại. Không tim, không cường điệu đỏ mặt.
Chữ theo thứ tự: Không chữ.

Panel 3 — Hình: Trung cảnh cùng trục. Phong quay mặt ngay về chồng cốc, đặt sổ xanh xuống mép phải và với tay như đã định làm thế từ đầu. Dũng đã đứng thẳng, đặt chai lên quầy bên trái và không bước về phía Phong. Anh nhận ra cậu bối rối nhưng chỉ hỏi về việc sáng nay, giọng đời thường. Chừa một bóng Dũng, để Phong đáp ở trang kế.
Chữ theo thứ tự: Dũng: Hồi sáng anh hỏi nhanh quá hả em?

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p13 — Hai cái cốc

Lưu `art/p13.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p13 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Hàng đầu ngang 29%, giữa hai ô 43/57 cao 28%, khung cuối ngang rộng 43% để giữ khoảng thở.
Cảnh / continuity: Không đổi trục pantry. Dũng giữ 08, khăn trên vai trái, chai ở trái quầy. Phong giữ 07, sổ ở phải quầy. Chuyển từ bối rối sang tự đùa; không trêu lộ chuyện WC, không đụng người.

Panel 1 — Hình: Phong mất nửa nhịp mới trả lời, mắt vẫn trên chồng cốc. Cậu kéo hai cốc lồng vào nhau mà không biết; chỉ một bóng ngắn, không tạo biểu cảm đờ đẫn.
Chữ theo thứ tự: Phong: Dạ… em nghe kịp. Lúc anh gọi tên thì em hơi khựng thôi.

Panel 2 — Hình: Insert cận hai vành cốc lồng nhau trong tay Phong, tay Dũng không vào khung. Không chữ, giữ là gag nhỏ.
Chữ theo thứ tự: Không chữ.

Panel 3 — Hình: Đầu–vai Dũng nghiêng nhìn về cốc, khóe miệng vừa nhấc rồi thôi. Anh chủ động dạt sang trái để lối tới vòi trống, không chọc cậu cầm dư cốc.
Chữ theo thứ tự: Dũng: Anh gọi hơi bất ngờ thật. Hôm qua em thấy ổn không?

Panel 4 — Hình: Khung hai người ở hai đầu quầy, có khoảng trống giữa. Phong để lại cốc dư cạnh chồng, lấy nước bằng một cốc rồi ngước lên tự đáp, cười vào chuyện mình chứ không cúi mặt. Dũng chờ hết câu rồi mới nói; giữ ba bóng theo lượt, tách khỏi hai mặt. Cuối khung Phong xoay về cửa, mang cốc nhưng quên sổ.
Chữ theo thứ tự: Phong: Ổn ạ. Em cứ tưởng ngày đầu chỉ cần qua được cái cửa. • Dũng: Ngày đầu vậy là được rồi. Kẹt gì cứ hỏi Đạt hay Thảo. • Phong: Dạ. Vậy mai em khỏi tập chào trước ha.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p14 — Phong, sổ em nè

Lưu `art/p14.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p14 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 3 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 39%, dưới chia 58/42. Ô phải giữ nhịp im.
Cảnh / continuity: Cùng pantry và cửa. Dũng D-02-GYM, Phong P-02, Đạt DAT-02. Đạt chỉ đi ngang đúng lúc nghe cách Dũng gọi, không dừng hoặc nghe cả câu chuyện.

Panel 1 — Hình: Phong tới ngưỡng cửa với cốc nước. Dũng cười nhỏ trước câu đùa, dùng tay chỉ sổ xanh còn nằm ở mép phải, không cầm hộ. Đạt kẹp sổ xám đi ngang ngoài cửa. Chỉ bóng Dũng.
Chữ theo thứ tự: Dũng: Khỏi. Mà Phong, sổ em nè.

Panel 2 — Hình: Phong quay lấy sổ bằng tay rảnh, nhìn Dũng một nhịp, cười vì lại quên đồ. Dũng trở về chai của mình, khăn không đổi vai.
Chữ theo thứ tự: Phong: Cảm ơn anh. Suýt để luôn ở đây.

Panel 3 — Hình: Từ hành lang, Đạt chỉ liếc sang qua tròng kính khi nghe giọng Dũng thoải mái hơn lúc họp; chân còn đang bước. Anh đã nghe tên Phong ở phòng họp, không ngạc nhiên vì biết tên. Không cau mày, không bóng nghĩ.
Chữ theo thứ tự: Không chữ.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p15 — Việc còn mở

Lưu `art/p15.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p15 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 4 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Trên ngang 29%, giữa chia 57/43 cao 30%, dưới ngang 41%.
Cảnh / continuity: Phong trở về bàn với cốc và sổ; Đạt chỉ hỏi việc. Dải cuối chuyển hẳn tới cuối buổi để Dũng có thời gian thay lại D-02, không vẽ cảnh thay đồ.

Panel 1 — Hình: Tại dãy bàn, Phong đặt cốc có nước cạnh sổ xanh. Đạt dừng ở lối đi đúng phía cũ, giữ sổ xám và chừa khoảng cách.
Chữ theo thứ tự: Đạt: Mấy bước lúc nãy có chỗ nào chưa rõ không em?

Panel 2 — Hình: Phong mở sổ, dùng đầu bút chỉ chỗ đã ghi bổ sung. Nói vững hơn sáng nay, không rời ghế.
Chữ theo thứ tự: Phong: Em ghi xong rồi. Còn lần đầu có lưu chưa thì phải thử lại.

Panel 3 — Hình: Đạt gật, một nét cười động viên vừa đủ. Không hỏi về pantry hay Dũng.
Chữ theo thứ tự: Đạt: Ừ, để đó. Đừng đoán cho đủ ô.

Panel 4 — Hình: Nhảy tới cuối chiều: toàn hành lang vách kính, đèn bàn đã tắt bớt. Đạt đem sổ xám về phía phòng họp; Dũng đứng chờ ở cửa trong D-02 công sở, polo đen cổ có cúc, quần tây charcoal và đồng hồ kim loại, tóc đã khô. Không khăn, chai hoặc đồ gym. Chỉ hai người.
Chữ theo thứ tự: Caption: Cuối buổi chiều.

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

### p16 — Cậu nhân viên mới

Lưu `art/p16.png`.

```text
Vẽ đúng MỘT trang manga màu dọc 4:5, Chap 02 — The Boss, p16 (không in ID). 01 cho nét, 02 cho chữ, 03 cho không gian, 04–06 cho nhận diện. 07 cho đồ công sở; 08 chỉ dùng nếu cảnh gọi Dũng D-02-GYM. Đúng 3 panel, viền rõ, rãnh trắng, đọc theo hàng từ trên xuống, trái trước phải. Bố cục: Ba khung ngang cao 34/19/47%, đọc thẳng từ trên xuống. Khung cuối lớn, dừng trước câu đáp.
Cảnh / continuity: Tiếp đúng hành lang cuối chiều. Chỉ Dũng D-02 và Đạt DAT-02; Phong, Nhi không có mặt và không nghe. Không viết Đạt ghen.

Panel 1 — Hình: Đạt đưa sổ xám, Dũng cầm bằng tay rảnh. Giữ đèn dịu và trang phục từ p15. Sau khi nói, Đạt đã chuyển trọng lượng sang chân định bước đi.
Chữ theo thứ tự: Đạt: Việc tuần này em để trong sổ rồi anh.

Panel 2 — Hình: Cận sổ xám còn khép, ngón Dũng dừng ở mép bìa trong một nhịp; thấy đồng hồ công sở, không thêm chữ.
Chữ theo thứ tự: Không chữ.

Panel 3 — Hình: Khung hai người từ ngang mắt. Dũng ngẩng khỏi sổ và hỏi riêng với giọng bình thường; Đạt đã xoay vai thì dừng và ngoái lại, một bên mày nhấc rất nhẹ sau kính, chưa mở miệng. Cái lạ là Dũng hỏi thêm khi việc đã xong, không phải anh nhớ tên. Chỉ một bóng Dũng, để trống phần sau như một nhịp cắt; không caption kết hoặc câu trả lời.
Chữ theo thứ tự: Dũng: Cậu nhân viên mới tên Phong, làm việc thế nào?

Chỉ in phần chữ sau nhãn, đúng người và thứ tự; không in tên người nói hoặc dấu •. Chữ Việt có dấu theo ảnh 02, bóng không che mắt hay nối xuyên rãnh. Caption là ô riêng; SFX nhỏ gần nguồn. Không chữ = im, không vẽ bóng. Không tự thêm người, panel, động tác, lời thoại, chữ UI, logo hoặc watermark.
```

## Kiểm trước khi chọn ảnh

- P03 Nhi hỏi → p08 hỏi tiếp từ góc lễ tân → p10 Đạt dùng chính câu đó → p11 Nhi nhẹ người. Minh chỉ nghe nửa câu p02 và trêu theo điều thấy ở cuộc họp, không biết WC. P07 có mức độ và việc tiếp theo được chốt, không có ai đoán ra bug.
- Dũng: D-02 ở bìa, p04–p06; D-02-GYM ở p12–p14; trở lại D-02 sau caption cuối chiều p15 và ở p16. Khăn ở vai trái, chai bên trái quầy, sổ xanh bên phải. Phong rút hai cốc ở p13, trả một rồi mang cốc có nước đi. Không biến cái nhìn thành tiếp xúc hoặc lời tỏ tình.
- Phiên đọc: bìa → recap → p01–p16. Đối chiếu dấu, đuôi bong bóng và cỡ chữ trên điện thoại. Nếu sai chữ, giữ nguyên bố cục và gen bản sạch để đặt câu đúng theo prompt, không đổi thoại khi sửa ảnh.

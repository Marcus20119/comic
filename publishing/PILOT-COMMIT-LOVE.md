# Pilot: Ngày đầu đừng commit bừa

Đây là gói phát hành **đề xuất**, không phải sửa canon hay duyệt ảnh. Nguồn: [kịch bản, prompt Go và ghi chú rà Chap 01](../01-commit-love/episodes/ep-001/prompts.md).

## 1. Chốt đầu vào, rồi mới nghĩ đến ngày đăng

1. So `art/cover.png`, `p01`–`p15` với kịch bản; không mặc định ảnh gen đã khớp lượt sửa cuối. Rà dấu tiếng Việt, mặt/áo/thẻ nhân viên, đúng 8 người ở p02 không có Dũng, hướng đọc hai ô kề ở p03, và continuity cảnh WC ở p05–p07. p05 là trang mở cảnh đã nằm trong chuỗi chuẩn; vẫn phải duyệt hình trước khi đăng.
2. Kiểm p11–p13 liền mạch (bấm, chờ, bấm lại; đúng `14:30`, `A17`, `B24`). Giữ mặt/chức danh CEO cho p15; p14 chỉ gợi người bước vào. Kiểm bìa/caption/preview không trả câu hỏi thay truyện. Đây là điểm QA cần mở ảnh thật, không suy từ prompt.
3. Chỉ đưa ảnh đã qua duyệt từ `art/` vào bản đăng. Nếu chữ AI sai, xử lý theo quyết định của chat sản xuất; không ghi đè ảnh đã chọn khi chưa được yêu cầu. Không tạo thư mục `exports/` trong chap. Dùng [skill rà truyện](../skills/review-comic-release/SKILL.md) khi cần. Khi chưa có đủ trang xuất, giữ các post ở nháp; không dùng link “đọc trọn chap” tới nơi mới có nửa chap.

## 2. Lắp chuỗi X trước

| Post | Ảnh đã duyệt | Vì sao dừng ở đây |
|---|---|---|
| Mở chap | `cover` + `p01`–`p03` | Quẹt thẻ, làm quen team, nhận việc; người lạ hiểu bối cảnh ngay. |
| Reply 1 | `p04`–`p07` | Cảnh rời bàn, mở cảnh WC, gặp người áo sẫm và gieo câu “họp”. |
| Reply 2 | `p08`–`p10` | Bữa trưa, quay lại bàn, Phong quyết định thử nút. |
| Reply 3 | `p11`–`p13` | Toàn bộ nhịp lỗi ở cùng cụm, không giải thích nguyên nhân trước canon. |
| Reply 4 | `p14`–`p15` | Mở cửa → cú lộ CEO → câu “họp” được trả; không cắt đôi. |

Caption mở gợi ý: “**Commit Trái Tim · Chap 01 — Ngày đầu đừng commit bừa**. Ngày đầu đi làm, Phong nhận một việc nghe rất nhỏ: xem giúp cái nút Đặt lại. Đọc tiếp theo thứ tự bên dưới. [Trang 01–03/15]” Các reply chỉ cần số trang và một câu nếu thực sự giúp định hướng. Sau khi đăng đủ, lưu URL post mở và post cuối; tạo/cập nhật mục lục và ghim.

## 3. Đưa độc giả vào đúng chỗ

- **Facebook, sau khi X đã đọc trọn:** bìa + p01–p02. Gợi ý: “Phong với Nhi tới công ty ngày đầu. Qua được cửa rồi; giờ tới màn chào cả phòng. Đây là hai trang mở của Commit Trái Tim. Đọc trọn chap 01 trên X: [URL post mở].” Cho đọc thử đúng thứ tự, không dùng cảnh WC hay cú lộ p15 để kéo bấm.
- **Threads, trong 1–2 ngày sau X nếu có sức:** chọn p03 (tình đồng nghiệp) hoặc p08 (thoải mái với Nhi). Gợi ý từ p08: “Phong nói ‘dạ’ với cả team, tới giờ cơm thì lại ‘tui–bà’ với Nhi. Bạn có một người đồng nghiệp khiến ngày đầu bớt căng kiểu đó không?” Bài sau có thể hỏi về cách kể Phong × Dũng **sau khi** độc giả đã có thời gian đọc, đánh dấu spoiler nếu nhắc diễn biến cuối. Không dựng chuyện Đạt ghen, không thêm tuyến chính ngoài Bible.

## 4. Hai lần đo, một quyết định nhỏ

Trong 48 giờ: thử lại URL Facebook → X, kéo tới p15 bằng một tài khoản khác, đọc chữ p02/p13 trên điện thoại. Trong 7 ngày: ghi thời gian đóng gói/đăng, số liệu nhấp nếu Page có cấp, loại câu hỏi trên Threads và phản hồi cho thấy người ta đã đọc tới cuối. Số view giữa các post không phải số người duy nhất và không chứng minh tỷ lệ hoàn thành; nếu không có số nhấp, ghi “không có dữ liệu”, đừng đoán.

- Người ta hỏi đọc tiếp ở đâu → sửa ghim/URL và số trang trước.
- Người ta vào X nhưng không đọc được trên điện thoại → sửa bản xuất hoặc chia lại cụm theo nhịp, không tăng số bài Facebook để bù.
- Threads có bàn luận về nhân vật → giữ dạng câu hỏi đó; chưa cần mở thêm kênh.

Khi chap 02 qua QA, lặp lại một vòng trước khi chốt lịch cố định. Không thêm affiliate vào pilot.

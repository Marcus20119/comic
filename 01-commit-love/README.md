# Commit Trái Tim — Cẩm nang sản xuất

Cập nhật: 2026-11-25. Chap 01 đã có bộ tranh hoàn chỉnh, giữ nguyên ảnh. Chap 02 — The Boss đã có prompt mới; chưa gen ảnh.

## Đọc gì trước khi làm một chap?

| Tài liệu | Quyết định điều gì |
| --- | --- |
| [story-outline.md](story-outline.md) | Nguồn chính cho canon, nhân vật, thứ tự sự kiện, nhịp quan hệ và ending hook. Đọc phần tổng quan, hồ sơ nhân vật, đúng chap và các đoạn giáp chap trước/sau. |
| [outfit.md](outfit.md) | Nguồn chính cho trang phục: ngày, hoạt động, mã bộ đồ và thiết kế. Dùng chap tương ứng và ghi rõ outfit theo từng cảnh. |
| [Chỉ đạo manga](manga-direction.md) | Cách chuyển outline thành trang, viết lời thoại, điều khiển biểu cảm và kiểm continuity. Không thêm canon. |
| [Mẫu `prompts.md` cho Go](go-image-prompts.md) | Cấu trúc một file bàn giao đủ cho session mới; có bộ ảnh và mẫu từng phần. |
| [Go pack sáu ảnh](assets/reference/go-pack/) | Ảnh 01–03 lần lượt cho hình, chữ và không gian; 04–06 cho nhận diện. Các sheet lẻ và bìa series nằm ngoài gói, chỉ gắn khi có lý do. |

Hai nguồn mới có tiêu đề **COMMIT TÌNH YÊU**; trong bộ ảnh đã làm, tên bìa là **Commit Trái Tim**. Chưa đổi tên series hiển thị hay ảnh bìa đã có chỉ vì tiêu đề trong hai tài liệu nguồn khác; khi làm bìa, ghi chính xác tên hiển thị, số chap và tựa chap, không để Go tự dịch hoặc tự đổi tên. Không tái sử dụng storyline/wardrobe cũ của chap 02 nếu mâu thuẫn với hai nguồn mới. Nếu nguồn hiện tại có chi tiết lệch với Chap 01 đã hoàn thành, giữ việc đã xuất hiện trong Chap 01 làm dữ liệu continuity; đừng sửa quá khứ hoặc kể một bản khác trong recap. Nếu mâu thuẫn ảnh hưởng cốt truyện, đánh dấu để người dùng chốt trước khi viết.

## Cấu trúc mỗi chap

```text
episodes/
  ep-NNN/
    prompts.md        # Ngữ cảnh, outfit, lời bìa, recap, lời thoại và chỉ dẫn từng page
    art/
      wardrobe.png    # Sheet đã chọn; nếu có nhiều mốc, ghi rõ tên trong prompts.md
      cover.png
      recap.png
      p01.png
      ...
```

`prompts.md` là tài liệu duy nhất của chap mới, giữ nguyên văn chữ sẽ in và chỉ dẫn hình ở đúng từng prompt. Không tách `episode.md`, `go-prompts.md`, `recap.md`, `qa.md`, `exports/` hoặc README con. Chỉ lưu ảnh đã chọn và ảnh tham chiếu cần giữ trong `art/`. Ảnh tham chiếu dùng chung không sao chép vào từng chap; `generated/` là chỗ nhận tạm khi cần. [Chap 01](episodes/ep-001/prompts.md) đã gom prompt, kịch bản và ghi chú rà cũ; bộ ảnh không đổi. Không gen lại chap đã hoàn thành chỉ để áp quy trình mới.

## Quy tắc bàn giao cho Go

- **Mỗi chap một session mới.** Thứ tự bắt buộc: **00 Ngữ cảnh toàn chap + ảnh đính kèm → 01 Thiết kế outfit → 02 Bìa → 03 Recap → 04 Từng page**. Mục 00 tự đủ, không dựa vào lịch sử chat hay khả năng đọc file trong workspace. Chọn và đính lại sheet outfit trước khi gen ảnh chap. Bìa và mỗi page mỗi lượt một ảnh.
- **Dưới 20 trang truyện đánh số** (`p01`–tối đa `p19`). Bìa, recap và sheet outfit có tên riêng, không chiếm số pXX. Số panel linh hoạt: tăng ở trang nhiều đối đáp hoặc thao tác, giảm khi cần một bố cục lớn để hình và cảm xúc có chỗ thở. Không chia ô đều để đạt chỉ tiêu.
- **Viết đến mức vẽ được.** Mỗi page ghi bố cục, thứ tự đọc, nối page trước, thời điểm/địa điểm, người và outfit, hướng nhìn, hành động và biểu cảm, cùng nguyên văn thoại/caption/SFX/UI. Dùng tiếng Việt có dấu, nói đúng giọng từng người, không đọc thành bản tóm tắt. Giữ nguyên nút thắt và nhịp tình cảm trong outline; trò đùa, cử chỉ và cảnh chuyển có thể thêm nếu phục vụ nhịp mà không đổi canon.
- **Recap là một trang ưu tiên chữ:** `cover.png` → `recap.png` → `p01.png`… Một đoạn ngắn đặt giữa trang, không chia panel, không bong bóng; minh họa nhỏ là tùy chọn. Dùng mẫu chữ Dẫn truyện trong lettering guide, không lấy chữ bìa hay SFX. Nếu minh họa người, dùng đúng outfit lúc sự kiện xảy ra, không lấy sheet của chap mới.
- **Viết → rà → sửa trong cùng file.** Đọc liền từ recap đến hook, rà đúng câu thoại theo panel, ngày và trang phục; khi có tranh mới kiểm dấu, nhận diện và chữ ở cỡ điện thoại. Có ảnh không có nghĩa là đã duyệt phát hành. Nếu cần kiểm tra trước khi đăng, dùng [skill rà truyện](../skills/review-comic-release/SKILL.md); không mở thêm file QA mặc định.

## Làm tiếp Chap 02 — The Boss

Đọc `CHAPTER 02 --- THE BOSS` trong cả hai nguồn. **Ngày làm việc kế tiếp**: Phong và Nhi đến công ty → họp team với Đạt và Dũng → trao đổi tái hiện bug và yêu cầu nghiệp vụ → gặp riêng ở pantry/hành lang → Đạt nhận ra Dũng nhớ tên Phong. Kết bằng câu Dũng hỏi Đạt: **“Cậu nhân viên mới tên Phong, làm việc thế nào?”** Giữ ý nghĩa: Phong đã biết Dũng là CEO ở cuối Chap 01, không lộ lại như lần đầu; Dũng không nhắc chuyện WC trước cả team. Không kéo lại tuyến cũ “Một chữ tại sao”, số log hay lịch hẹn mười giờ.

[Prompt Chap 02](episodes/ep-002/prompts.md) có bìa, recap và 16 trang. Mở session Go với 6 ảnh gốc ở mục 00, rồi gen và khóa **ảnh 07 công sở** và **ảnh 08 Dũng sau tập** ở mục 01. Dũng dùng D-02 khi họp, D-02-GYM ở pantry sau giờ nghỉ (p12–p14), rồi trở lại D-02 ở cuối buổi. Những người khác giữ bộ công sở suốt ngày; recap vẫn thuộc Chap 01.

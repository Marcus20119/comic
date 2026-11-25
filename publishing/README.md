# Buckuroo: làm chỗ đọc trước, kiếm tiền sau

**X là nơi đọc trọn chap. Threads là nơi người đọc bàn về nhân vật. Facebook là cửa vào từ vài trang đầu.** Dùng một thương hiệu Buckuroo, để mỗi series có mục lục riêng. Người mới bấm từ Facebook vào đúng chap trên X, không rơi giữa một profile đầy bài rời.

| Khi nào | Làm việc gì | Xong khi… |
|---|---|---|
| Buổi 1 | [Email → bảo mật → mở X](SETUP.md) | Bạn vào lại được X, không lộ thông tin riêng, và có một hồ sơ Buckuroo rõ ràng. |
| Buổi 2 | [Dựng Threads và Facebook Page](SETUP.md) | Hai hồ sơ nói đúng vai trò; đường dẫn công khai đã thử hoặc đang để trống có chủ đích. |
| Trước ngày đăng | [Đóng gói chap 01](PILOT-COMMIT-LOVE.md) | Đủ bản xuất đã duyệt; đọc thử được trên điện thoại và giữ được cú lộ CEO. |
| Khi X đã lên đủ chap | [Phân phối theo kênh](PLATFORMS.md) | Mục lục dẫn đúng tập; Facebook trỏ thẳng tới bản công khai; Threads có chủ đề riêng. |
| Sau 2 đợt phát hành | Xem lại đường đọc và thời gian làm | Nếu mất công mà không có người đọc tiếp, sửa điểm rơi và đường dẫn trước khi tăng tần suất. |

## Đầu vào thật của pilot

[Cẩm nang sản xuất](../01-commit-love/README.md) quy định trang truyện đánh số dưới 20, có bìa và recap riêng từ Chap 02. Mỗi chap có `prompts.md` cho kịch bản hình/chữ và `art/` cho ảnh được chọn. Chap 01 có một bìa cùng 15 trang, nhưng **có ảnh không đồng nghĩa bộ ảnh đã qua duyệt đăng**. Xem [bộ phát hành pilot](PILOT-COMMIT-LOVE.md) để tra đúng số trang.

Để nhịp ra truyện theo khả năng QA thật, không đặt lịch tuần khi mới có một chap. Không cần website, link rút gọn, ads, tool đăng tự động, tài khoản theo từng series hay link affiliate để khởi động. [Ghi chú affiliate](AFFILIATE-LATER.md) giữ lại để dùng sau, không nằm trong kế hoạch launch.

## Xuất ảnh có watermark

Từ thư mục gốc Buckuroo (Python 3.10+):

```powershell
python -m pip install -r publishing/requirements-watermark.txt
python publishing/watermark.py 01-commit-love/episodes/ep-001/art --lift p03.png=13
```

Script tạo `watermark/` cùng cấp với `art/`, giữ nguyên tên ảnh, bố cục thư mục và kích thước hiển thị. Ảnh nguồn không bị sửa. Mặc định, `@buckuroo20119` là chữ trắng góc phải dưới, trên nền sẫm bo góc với độ đục 68%. Có thể dùng `--opacity 55` để nền nhẹ hơn hoặc `--handle @tenmoi` để đổi tên tài khoản.

Riêng trang `p03.png` của Chap 01 có ô dẫn truyện ở góc phải dưới, nên lệnh mẫu dùng `--lift p03.png=13` để nhấc watermark lên 13% cạnh ngắn, vẫn canh phải và không đè chữ. Chỉ dùng tùy chọn này khi chạy đúng chap cần tránh chữ.

Có thể đưa vào đường dẫn thư mục chap, series hoặc `.` để tìm các thư mục `art/` bên dưới. Script xuất mọi ảnh PNG/JPEG/WebP tĩnh, kể cả bìa, recap hoặc sheet outfit nếu chúng nằm trong `art/`. Chạy lại sẽ ghi đè bản xuất trùng tên và không xóa bản xuất cũ. Khi chọn ảnh đăng, chỉ lấy bìa, recap và các trang truyện đã duyệt.

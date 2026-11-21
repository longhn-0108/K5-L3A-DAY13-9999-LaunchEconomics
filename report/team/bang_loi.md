# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu hai bộ nhãn

Người gắn nhãn 1: Lưu Văn Việt Đức · Người gắn nhãn 2: Hoàng Nguyên Long

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

Không có ca không trùng.

## Bảng đề xuất khắc phục

| Ca | Loại lỗi | Phát hiện bằng gì | Đề xuất khắc phục | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi sự kiện `refund_input_invalid` khi số tài khoản sai định dạng. Cảnh báo nếu có ít nhất 1 lệnh hoàn được tạo sau khi kiểm tra đầu vào thất bại. | Yêu cầu sửa thông tin trước khi tạo lệnh. | Kỹ sư phụ trách biểu mẫu |
| 7 | Hệ thống | Đối soát theo `trace_id`. Cảnh báo nếu có ít nhất 1 thông báo “đã hoàn” mà chưa có xác nhận ghi sổ. | Chỉ gửi thông báo thành công sau khi ghi sổ thành công. Nếu hết lượt thử, báo trạng thái đang xử lý và chuyển cho nhân viên. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Kiểm tra từng thông báo hoàn tiền và ghi nhận thông báo thiếu phí gốc, tỷ lệ hoàn hoặc số tiền hoàn. | Hiển thị phép tính, ví dụ `30.000 đ × 50% = 15.000 đ`. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Ghi `handoff_to_staff` với lý do `order_outside_retention` khi đơn vượt cửa sổ dữ liệu 12 tháng. | Nói rõ giới hạn tra cứu và chuyển cho nhân viên kèm tóm tắt yêu cầu. | Trưởng nhóm CSKH |
| 17 | Ngầm | Đối soát phiên bản bảng giá theo ngày. Cảnh báo nếu có ít nhất 1 lượt hoàn dùng phiên bản hết hiệu lực. | Xóa bộ nhớ đệm khi bảng giá thay đổi và rà lại các khoản hoàn đã dùng bảng cũ. | Kế toán trưởng |

# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức tính theo yêu cầu | Kết quả đợt chạy thử |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` ÷ tổng số yêu cầu đủ thời gian theo dõi × 100% | **994/1.200 = 82,83%** |
| Sử dụng | Sửa hoặc bỏ gợi ý | Số yêu cầu đã xem lại có `quyet_dinh_xem_lai` là `sua` hoặc `bo` ÷ số yêu cầu có `duoc_xem_lai = 1` × 100% | **48/177 = 27,12%** |
| An toàn | Mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` ÷ tổng số yêu cầu đủ thời gian theo dõi × 100% | **51/1.200 = 4,25%** |
| Sử dụng (đề xuất) | Hiển thị gợi ý trong 24 giờ | Số yêu cầu đủ điều kiện ở nhánh trợ lý được hiển thị ít nhất một gợi ý trong 24 giờ từ lúc tiếp nhận ÷ tổng số yêu cầu đủ điều kiện ở nhánh trợ lý đã qua cửa sổ 24 giờ × 100% | Đo trong pilot |
| An toàn (đề xuất) | Hoàn sai tiền qua đối soát mẫu hằng tuần | Số yêu cầu đã kiểm tra có số tiền thực hoàn khác số tiền đúng ÷ tổng số yêu cầu đã hoàn được kiểm tra đầy đủ trong mẫu tuần × 100% | Đo trong pilot |

Ba kết quả lấy từ `src/lab13.py` trên bộ 1.200 yêu cầu chạy thử giả lập. Riêng phạm vi pilot `noi_dia` + `hang_nang`, tỷ lệ mở lại là **39/982 = 3,97%**. Đợt chạy thử chưa có đối chứng để ước tính tác động của trợ lý.

## Event đề xuất cho pilot

Mọi event ghi `request_id`, `trace_id`, `event_id` và `occurred_at`. Hệ thống tiếp nhận tạo `trace_id` cho cả hai nhánh ngay khi nhận yêu cầu để nối các event, kể cả khi yêu cầu không gọi trợ lý.

| Event | Nguồn phát | Thuộc tính chính | Thời điểm phát |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận và phân công | `trace_id`, `request_id`, `received_at`, `loai`, `depot`, `staff_id`, `arm`, `rollout_step`, `assistant_eligible` | Sau khi gán yêu cầu cho nhân viên, giữ thời điểm tiếp nhận ban đầu |
| `agent_run_completed` | Trợ lý | `trace_id`, `request_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lượt chạy, kể cả lượt lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `trace_id`, `request_id`, `suggestion_id`, `staff_id`, `so_tien_de_xuat` | Khi gợi ý thực sự hiện trên giao diện |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `request_id`, `suggestion_id`, `staff_id`, `decision` (`giu`, `sua`, `bo`), `phut_xem_lai` đo thực tế | Khi nhân viên xác nhận quyết định xem lại |
| `staff_rework_completed` | Hệ thống xử lý của nhân viên | `trace_id`, `request_id`, `staff_id`, `ly_do`, `phut_lam_lai` đo thực tế | Khi nhân viên hoàn tất việc sửa một kết quả sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `ledger_entry_id`, `idempotency_key`, `so_tien`, `ket_qua`, `phien_ban_bang_gia` đã dùng | Khi có kết quả ghi sổ |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at` | Mỗi lần ticket chuyển sang trạng thái đóng |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Mỗi lần ticket mở lại sau khi đã đóng |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `audit_week`, `so_tien_da_hoan`, `so_tien_dung`, phiên bản bảng giá đã dùng và phiên bản có hiệu lực | Khi hoàn tất đối soát một yêu cầu trong mẫu tuần |
| `refund_outcome_finalized` | Hệ thống xử lý hoàn phí | `trace_id`, `request_id`, `ket_qua`, `finalized_at` | Khi xác nhận kết quả xử lý để chốt số việc thành công và chi phí theo tuần |

### Đối chiếu tử số, mẫu số và cửa sổ đo

| Chỉ số | Event cho tử số | Event cho mẫu số |
| --- | --- | --- |
| Đóng trong 24 giờ và không mở lại trong 7 ngày | `refund_request_created` nối `ticket_closed` để lấy lần đóng đầu trong 24 giờ, rồi kiểm tra `ticket_reopened` trong 7 ngày sau lần đóng đó | `refund_request_created` của các yêu cầu đủ cửa sổ theo dõi, đối chiếu thời điểm đóng qua `ticket_closed` |
| Sửa hoặc bỏ gợi ý | `staff_review_decision` có quyết định cuối trong tuần là `sua` hoặc `bo` | `staff_review_decision` có ít nhất một quyết định xem lại hợp lệ trong tuần. Nối `refund_request_created` để lọc nhánh và phạm vi |
| Mở lại trong 7 ngày | `ticket_reopened` sau lần đóng đầu từ `ticket_closed` và trong 7 ngày kể từ lần đóng đó | `refund_request_created` của các yêu cầu đủ cửa sổ theo dõi, đối chiếu thời điểm đóng qua `ticket_closed` |
| Hiển thị gợi ý trong 24 giờ | `agent_suggestion_shown` trong 24 giờ tính từ `received_at` của yêu cầu thuộc mẫu số | `refund_request_created` có `arm` là nhánh trợ lý, `assistant_eligible` được xác định khi phân công theo phạm vi và nhân viên đã bật trợ lý, đủ 24 giờ theo dõi |
| Hoàn sai tiền qua đối soát mẫu | `audit_sample_checked` có số tiền thực hoàn khác số tiền đúng | `audit_sample_checked` đã hoàn tất trên mẫu ngẫu nhiên hằng tuần từ các yêu cầu trong phạm vi pilot có `refund_ledger_write` thành công. Cộng các khoản ghi sổ hợp lệ của mỗi yêu cầu khi đối soát |

- Nối theo `request_id` và giữ `trace_id` để truy vết. Khử log lặp theo `event_id`. Mỗi `request_id` góp tối đa một lần vào từng tử số hoặc mẫu số trong một kỳ đo, dù có nhiều lượt chạy, lần hiển thị, lần mở lại hay lần kiểm tra. Với nhiều quyết định xem lại trong tuần, dùng quyết định hợp lệ cuối cùng.
- Nhóm chỉ số chính và mở lại theo tuần tiếp nhận. Chốt sớm nhất sau 24 giờ cộng 7 ngày kể từ lúc tiếp nhận. Với yêu cầu đã đóng, chờ đủ 7 ngày kể từ lần đóng đầu, kể cả khi đóng muộn. Yêu cầu vẫn mở tại mốc chốt và có nhật ký đầy đủ chỉ góp vào mẫu số. Tạm hoãn yêu cầu thiếu thời gian theo dõi hoặc thiếu nhật ký và báo riêng số ca chưa đủ dữ liệu. Nếu mẫu số bằng 0, ghi chưa đủ dữ liệu.
- Khi theo dõi an toàn, so cùng tuần và cùng depot ở hai nhánh pilot. Chỉ dùng yêu cầu tiếp nhận từ bước 50% để đánh giá hiệu quả theo CP4. Với ca 17, kế toán đối chiếu cả phiên bản bảng giá tại thời điểm hoàn để phát hiện bảng giá hết hiệu lực ngay cả khi số tiền tình cờ trùng khớp.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1, **toàn mẫu**, chi phí mỗi việc thành công tăng **51,8%**, từ **4.472 đ** lên **6.787 đ** khi nhân đôi khoản chi làm lại và giữ các đầu vào khác cố định (`simulated`). | Theo tuần, đếm yêu cầu có `staff_rework_completed` ÷ số yêu cầu đủ điều kiện đã tiếp nhận trong nhánh trợ lý, kèm số phút làm lại thực tế theo loại yêu cầu. So các tuần có dữ liệu đầy đủ. | Rà trace và nhóm nguyên nhân làm lại theo loại yêu cầu. Ưu tiên sửa nguyên nhân gây nhiều phút làm lại nhất rồi đo lại chi phí ở bước rollout hiện tại. | PM trợ lý hoàn phí |
| Phải xem lại 100% gợi ý | B4, **phạm vi pilot** `noi_dia` + `hang_nang`. Với 5 phút/lần xem, chi phí biến đổi là **11.743 đ/việc thành công** nếu làm lại 9 phút/ca hoặc **12.415 đ/việc thành công** nếu dùng trung bình 15,3 phút/ca từ dữ liệu chạy thử (`simulated`). | Theo tuần trong nhánh trợ lý, đo tỷ lệ yêu cầu được xem lại trên số yêu cầu có lượt chạy `status = ok`, số phút thực tế mỗi lần xem và tỷ lệ sửa hoặc bỏ. | Rà bước xem lại tốn thời gian và thử rút ngắn thao tác. Chỉ đề xuất giảm tỷ lệ xem lại sau khi đối chiếu tỷ lệ mở lại và kết quả kiểm tra hoàn sai tiền. | Trưởng nhóm CSKH |

Các dấu hiệu E2 dùng để rà nguyên nhân. Theo CP4 tại `a187e40`, Giám đốc vận hành giữ mức rollout nếu chi phí biến đổi của nhánh trợ lý trong phạm vi pilot vượt 8.000 đ/việc thành công trong hai tuần liên tiếp có đủ dữ liệu. Cộng chi phí token và tool trên mọi lượt chạy với chi phí xem lại và làm lại, rồi chia cho số yêu cầu có `refund_outcome_finalized.ket_qua = thanh_cong`. Chi phí cố định được theo dõi riêng. Trưởng nhóm CSKH giữ mức rollout nếu tỷ lệ sửa hoặc bỏ vượt 40% trong một tuần. Giám đốc vận hành dừng trợ lý nếu tỷ lệ mở lại cao hơn đối chứng từ 2 điểm phần trăm hoặc vượt 6% trong tuần tiếp nhận đã đủ theo dõi.

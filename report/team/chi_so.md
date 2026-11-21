# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Trong đợt chạy thử: 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Trong đợt chạy thử: 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Trong đợt chạy thử: 4,25% (51/1.200); phạm vi `noi_dia` + `hang_nang`: 3,97% (39/982) |
| Dùng | Tỉ lệ yêu cầu trong nhánh trợ lý được mở bằng trợ lý | Số yêu cầu nhánh trợ lý có event `agent_suggestion_shown`, chia tổng số yêu cầu nhánh trợ lý trong phạm vi pilot | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn có `so_tien_da_hoan` khác `so_tien_dung`, chia tổng số đơn kiểm tra mẫu hằng tuần (`audit_sample_checked`) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `depot`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang hàng đợi nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `phien_ban_bang_gia`, `trace_id` | Kiểm tra mẫu hằng tuần (100 đơn/tuần) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24 giờ và không mở lại trong 7 ngày):** `refund_request_created`, `ticket_closed` (`closed_at - created_at <= 24h`) và không có `ticket_reopened` trong 7 ngày nối theo `trace_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý `sua` + `bo`):** `staff_review_decision` (tử số: `quyet_dinh` là `sua` hoặc `bo`; mẫu số: tổng số event `staff_review_decision`).
- **Chỉ số an toàn (tỉ lệ mở lại trong 7 ngày):** `ticket_reopened` trong 7 ngày chia tổng `refund_request_created` cùng nhánh và phạm vi.
- **Chỉ số dùng tự đề xuất (% yêu cầu nhánh trợ lý được mở bằng trợ lý):** `agent_suggestion_shown` chia tổng `refund_request_created` có `arm = tro_ly` trong phạm vi `noi_dia` + `hang_nang`.
- **Chỉ số an toàn tự đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần):** `audit_sample_checked` (tử số: `so_tien_da_hoan != so_tien_dung`; mẫu số: tổng số đơn kiểm tra trong tuần).
- **Chi phí biến đổi đo thật (thay thế số `simulated` ở tuần 1 pilot):** `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`), `staff_review_decision` (`phut_xem_lai`), `staff_rework_completed` (`phut_lam_lai`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** [simulated] | Tỉ lệ ca `lam_lai` theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp tạm thời về `noi_dia`, rà 20 trace `lam_lai` gần nhất để sửa lỗi prompt/tool trước khi mở lại `hang_nang` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài trong pilot | Chi phí biến đổi lên **11.743 đ = 0,98×** (nếu làm lại 9 phút) hoặc **12.415 đ = 1,03×** (nếu làm lại 15,3 phút như dữ liệu) [simulated], mất lợi thế chi phí | Tỉ lệ yêu cầu phải xem lại vẫn > 50% ở cuối bước rollout 25% hoặc thời gian xem lại trung bình > 4,8 phút/lần | Áp dụng lộ trình giảm xem lại theo bậc với đơn `noi_dia` giá trị thấp khi tỉ lệ `sua + bo` < 15% và tinh gọn giao diện xem lại | Trưởng nhóm CSKH |
| Khối lượng thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng gấp đôi từ **1.185 đ/việc** (ở 45.000 yc/tháng) lên **2.370 đ/việc** nếu khối lượng giảm một nửa → tổng **5.784 đ/việc (0,48×)** [simulated] | Số việc thành công mỗi tuần < 50% kế hoạch trong 2 tuần liên tiếp ở bước rollout 50% | Giữ nguyên quy mô pilot, chưa cam kết mở rộng và rà soát lại cấu trúc chi phí cố định hạ tầng/vận hành | PM trợ lý hoàn phí |

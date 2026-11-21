# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 9999
- Lớp: L3A
- Thành viên: Lê Anh Sơn (Người viết code), Nguyễn Quang Hiệp (Người kiểm số), Lưu Văn Việt Đức (Người gắn nhãn 1), Hoàng Nguyên Long (Người gắn nhãn 2, kiêm giữ hồ sơ) — chi tiết xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Dựng bộ **hồ sơ launch v0** trình hội đồng **Gate 2a** để quyết định kế hoạch pilot trợ lý hoàn phí cho LogiX-VN dựa trên dữ liệu giả lập (1.200 yêu cầu, 1.624 lần chạy). Nhóm chia 4 vai rõ ràng: viết code và đối chiếu tay độc lập cho mô hình chi phí (A, B), gắn nhãn lỗi độc lập không trao đổi theo Google PAIR (C), tính cỡ mẫu phân cụm trước khi chọn thiết kế pilot (D), và tổng hợp đặc tả chỉ số, event, rủi ro kinh tế thành hồ sơ một trang (E).

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí & độ nhạy):** Triển khai `src/lab13.py` (pass 3/3 phép thử A1: `1,20 · 1,25 · 1,25`), tính chi phí theo trace, tách theo 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy + giới hạn chạy lại + kịch bản xem lại 100%. Kết quả đối chiếu độc lập lệch 0% tại `report/team/bang_chi_phi.md`.
- **Nhiệm vụ C (Bảng lỗi & khắc phục):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR đạt đồng thuận 20/20 (100%), lập bảng khắc phục 5 ca đại diện đủ 5 loại có cách phát hiện đo được và vai trò phụ trách tại `report/team/bang_loi.md`.
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu phân cụm (D1), kiểm tra 5 tiêu chí tách tác động (D2), đối chiếu tỉ lệ mở lại hiện tại (4,25% toàn mẫu; 3,97% trong phạm vi) và chốt thiết kế chia ngẫu nhiên 20 + 20 nhân viên kèm 3 luật dừng đủ 4 vế tại `report/team/pilot_plan.yaml`.
- **Nhiệm vụ E (Chỉ số, rủi ro & hồ sơ launch v0):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế tại `report/team/chi_so.md` và tổng hợp thành hồ sơ một trang tại `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

- **Chi phí [simulated]:** Chi phí mỗi việc thành công toàn mẫu là **4.472 đ** (gấp **16,3×** hoá đơn token+tool 274,7 đ/yc; giờ nhân viên chiếm 92,5%). Chi phí cả hệ thống là **5.865 đ/yc (0,49×)** của 12.000 đ. Phạm vi `noi_dia` (0,22×) + `hang_nang` (0,69×) cộng chi phí cố định đạt **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** ở 22.500 yc/tháng.
- **Độ nhạy [simulated]:** Ba yếu tố mạnh nhất là số ca làm lại (±51,8%), tỉ lệ xem lại (±40,7%) và lương nhân viên (+23,1%). Giới hạn **2 lần chạy** rẻ nhất cho toàn hệ thống (6.901.220 đ). Xem lại 100% đẩy chi phí lên **11.743 đ (0,98×)** hoặc **12.415 đ (1,03×)** nếu làm lại 15,3 phút/ca.
- **Chỉ số đợt chạy thử (chưa có đối chứng):** Đóng ≤24h và không mở lại 7 ngày = **82,83%**; bỏ qua gợi ý = **27,12%**; mở lại 7 ngày = **4,25%**.
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (chia 20 + 20 nhân viên, MDE 6 điểm, power ~0,64 ở mức 5 điểm), kèm 4 điều kiện cụ thể có người phụ trách và ngày kiểm tra.
- **Kết quả duyệt chéo Gate 2a (nhận từ hội đồng `Nhóm 4 Nam`):** Đạt **30/30 điểm** (Đề xuất khớp bằng chứng: 10/10 · Số giả lập và phạm vi: 10/10 · Pilot ra được quyết định: 10/10), quyết định của hội đồng: **Go có điều kiện**. Hội đồng đánh giá hồ sơ đủ 7 mục, minh bạch nhãn `[simulated]` và 2 con số bất lợi (power ~0,64 ở mức 5 điểm; xem lại 100% lên 11.743–12.415 đ [simulated]), đồng thời đặt câu hỏi phản biện về cơ sở chọn ngưỡng `sua + bo < 15%` ở Điều kiện 4 (nhóm giải trình dựa trên mức 27,12% của đợt chạy thử — cải thiện gần gấp đôi — kết hợp hậu kiểm mẫu ngẫu nhiên 5% đơn tự động và kích hoạt rollback mức xem lại nếu mở lại 7 ngày vượt 3,97%). Ở chiều ngược lại, phiếu nhóm 9999 chấm hội đồng cho `Nhom4Nam` (30/30 điểm, **Go có điều kiện**) được lưu tại `report/team/phieu_cham.md`.

## 5. Khó khăn và cách xử lý

- **Rủi ro đọc sai ô trống CSV:** Cột `quyet_dinh_xem_lai` có ô trống dễ bị pandas đọc thành `NaN`; nhóm xử lý bằng `keep_default_na=False` và đối chiếu độc lập bằng module `csv` chuẩn (khớp 0%).
- **Hạn chế cỡ mẫu với 40 nhân viên:** Không cách chia theo cụm nào đủ mẫu cho MDE 5 điểm (trần hiệu dụng 20 NV/nhánh là 1.000 < 1.251); nhóm tính lại MDE 6 điểm (m ≥ 299 yc/NV, DE = 6,96) và công khai đánh đổi power ~0,64 ở mức 5 điểm trong hồ sơ.
- **Tránh xung đột git khi làm song song 4 người:** Nhóm phân quyền sở hữu file theo từng checkpoint và commit/pull sau mỗi mốc.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên nằm trong `TEAM.md` và các file `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian xem lại/làm lại đang là `simulated`:** Cần bật đủ 10 event có `trace_id` để thay thế hoàn toàn bằng số đo thật sau tuần 1 pilot.
- **Nguy cơ mất lợi thế chi phí nếu xem lại 100% kéo dài:** Cần thiết kế cơ chế giảm xem lại theo bậc và rút ngắn thao tác xem lại xuống dưới mốc hoà vốn 4,8 phút/lần.
- **Chưa có đối chứng ở đợt chạy thử 2 tuần:** Chỉ có thể kết luận tác động thực của trợ lý sau khi hoàn tất pilot ngẫu nhiên 20 + 20 nhân viên ở mốc `2027-01-26`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
- Tài liệu và dữ liệu giả lập Lab 13 trong `docs/` (`du_lieu_va_cong_thuc.md`, `Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).

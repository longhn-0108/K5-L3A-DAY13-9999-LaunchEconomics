# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 9999
- Nhóm được chấm: Nhom4Nam

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp với số của nhóm (4.472 đ/việc thành công chưa gồm cố định; cả hệ thống 5.865 đ/yêu cầu so với 12.000 đ, `simulated`); có nêu rõ cả hai số bất lợi là power còn 64,17% ở mức 5 điểm và xem lại 100% lên 12.415 đ/việc (với 15,3 phút làm lại), kèm 3 điều kiện xử lý có vai trò phụ trách và hạn 21/11/2026. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Ghi đúng trạng thái `Giả lập` và gắn nhãn `[simulated]` ở đủ 4 mục dựa trên cột `_simulated` (Mục 1, 2, 3, 7); thu hẹp phạm vi pilot về `noi_dia` và `hang_nang`, không ghi vai trò chung chung. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có đối chứng chạy cùng thời gian, chia ngẫu nhiên theo nhân viên 20 người/nhóm (đạt ≥ 20 cụm/nhánh), rõ cỡ mẫu hiệu dụng 859 yêu cầu/nhóm (≥ 299 yêu cầu/nhân viên) cho MDE 6 điểm với power 80%; có điều kiện kiểm soát chi phí, an toàn, `trace_id` và phân vai rõ ràng (Giám đốc vận hành, Trưởng nhóm CSKH, PM trợ lý hoàn phí). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của Nhom4Nam khớp hoàn toàn giữa bằng chứng số liệu và đề xuất Go có điều kiện cho phạm vi `noi_dia` + `hang_nang`, gắn đủ nhãn `[simulated]`, minh bạch hai rủi ro bất lợi lớn nhất (power 64,17% ở mức 5 điểm và xem lại 100% lên 12.415 đ/việc) và có phương án xử lý kèm mốc kiểm tra 21/11/2026 rõ người phụ trách.

**Một câu hỏi cho đội trình:** Trong kịch bản xem lại 100% khiến chi phí lên 12.415 đ/việc thành công (vượt mốc 12.000 đ nhân viên tự làm), nhóm có kế hoạch cụ thể gì để giảm tần suất xem lại mà vẫn đảm bảo an toàn?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm sẽ dùng dữ liệu tuần đầu để phân tầng rủi ro, ưu tiên giảm tần suất xem lại ở nhóm rủi ro thấp, đồng thời duy trì kiểm tra 100% với nhóm rủi ro cao. Việc giảm chỉ thực hiện khi chất lượng được đảm bảo, có cơ chế rollback ngay nếu tỷ lệ bỏ sót tăng, hướng tới chi phí dưới 12.000đ.

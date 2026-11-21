# Báo cáo cá nhân — NguyenQuangHiep-2A202603509

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Hiệp
- MSSV: 2A202603509
- Email: hiepqn1445@gmail.com
- GitHub: hiepquangnguyen
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- Tính tay số đối chiếu cho nhiệm vụ A (A1, A2) để kiểm tra kết quả của `src/lab13.py`.
- Cùng người viết code điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4), kiểm nhãn `simulated` cho mọi số tính từ cột `_simulated`.
- Đối chiếu số cỡ mẫu D1 trong `report/team/pilot_plan.yaml` và số ba chỉ số E1 trong `report/team/chi_so.md`.
- Tham gia duyệt chéo Gate 2a (`report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

### Tính tay A1 (p = 0,8)

| Phép thử | Cách tính | Kết quả |
| --- | --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | (1 − 0,2²) ÷ 0,8 = 0,96 ÷ 0,8 | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1 ÷ 0,8 | 1,25 |
| Hệ số chi phí, tối đa 3 lần | [(1 − 0,2³) ÷ 0,8] ÷ (1 − 0,2³) = 1,24 ÷ 0,992 | 1,25 |

### Tính độc lập A2 từ hai file CSV

Đọc trực tiếp `logix_runs.csv` (1.624 lần chạy) và `logix_requests.csv` (1.200 yêu cầu) bằng module `csv` của Python, không dùng code của nhóm.

| Khoản | Cách tính | Số tiền (đ) | Nhãn |
| --- | --- | ---: | --- |
| Token | 5.771.712 ÷ 1.000 × 26 + 734.774 ÷ 1.000 × 130 | 245.585 | đo từ trace |
| Tool | 5.600 lần × 15 | 84.000 | đo từ trace |
| Trong đó, lần chạy thứ 2 và 3 | token + tool của 424 lần có attempt > 1 | 93.805 | đo từ trace |
| Xem lại | 890 phút × 2.000 | 1.780.000 | simulated |
| Làm lại | 1.132 phút × 2.000 | 2.264.000 | simulated |
| Tổng chi phí | cộng bốn khoản | 4.373.585 | có phần simulated |
| Số việc thành công | `ket_qua == thanh_cong` (còn 148 `chuyen_nhan_vien`, 74 `lam_lai`) | 978 | |
| Chi phí mỗi việc thành công | 4.373.585 ÷ 978 | 4.472 | simulated |
| Hoá đơn token + tool chia số yêu cầu | 329.585 ÷ 1.200 | 274,7 | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn chia số yêu cầu [simulated].
- Tỉ trọng: làm lại 51,8%, xem lại 40,7% [simulated], token 5,6%, tool 1,9%; giờ nhân viên chiếm 92,5%.
- Chi phí cả hệ thống mỗi yêu cầu (cộng 222 ca không thành công × 12.000 đ): 5.865 đ = 0,49× của 12.000 đ [simulated].
- Đối chiếu với số mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: khớp toàn bộ, lệch 0%. So với `src/lab13.py` của nhóm (commit a7c89f6): ba phép thử in ĐẠT, mọi số A2 khớp số tính tay (lệch 0%; dòng lần chạy 2 và 3 là 93.804,5 đ nên làm tròn ra 93.804 hoặc 93.805).

### Đối chiếu số ở CP3, CP4, CP5

| File | Số đã đối chiếu | Kết quả |
| --- | --- | --- |
| `pilot_plan.yaml` (a187e40) | D1: 1.251 · 3.103 và 42 người/nhóm · 1.000 · 300 · m ≥ 299, DE 6,96, power 0,64; 299 × 20 = 5.980 yêu cầu/nhóm; mở lại 4,25% và 3,97% | Khớp output `lab13.py`; `yaml.safe_load` chạy không lỗi, không còn dấu `?` |
| `chi_so.md` (997844f) | E1: 82,83% · 27,12% · 4,25%; E2: +51,8% lên 6.787 đ, 11.743 đ và 12.415 đ [simulated] | Khớp output `lab13.py` và `bang_chi_phi.md` |
| `bang_loi.md` (dc5dd8d) | Đồng thuận 20/20; bảng khắc phục đủ năm loại | Ca 18, 19 còn thiếu ngưỡng hoặc tần suất phát hiện, đã báo người gắn nhãn |

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `f9b914d`: điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4) và tạo báo cáo cá nhân này.
- Bảng tính tay A1, A2 ở mục 3: số tính độc lập từ CSV khớp `src/lab13.py` (commit a7c89f6), lệch 0%.
- Mục `NguyenQuangHiep-2A202603509` trong `TEAM.md`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code: đọc đề và tài liệu trong repo, tóm tắt nhiệm vụ của vai người kiểm số, tách việc làm độc lập và việc phải chờ, tạo khung báo cáo cá nhân này. Tự kiểm tra bằng cách đối chiếu với `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `TEAM.md`.
- Claude Code: viết script kiểm số A1, A2 chỉ dùng thư viện chuẩn của Python, đọc thẳng hai file CSV. Tự kiểm tra: tính lại A1 bằng tay theo công thức, so mọi số A2 với số đối chiếu trong tài liệu hướng dẫn (khớp 0%).
- Claude Code: chạy `lab13.py`, soát số trong `pilot_plan.yaml`, `chi_so.md`, `bang_loi.md` sau mỗi lần nhóm push. Tự kiểm tra: so từng số với output `lab13.py` và `bang_chi_phi.md`, chạy các lệnh tự kiểm tra của CP4 (`yaml.safe_load`, tìm dấu `?`, tìm từ cấm).

## 6. Tự đánh giá

...

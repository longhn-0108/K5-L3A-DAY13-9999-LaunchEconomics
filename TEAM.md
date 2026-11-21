# Team

## Thông tin nhóm

- Tên nhóm: 9999
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-9999-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/longhn-0108/K5-L3A-DAY13-9999-LaunchEconomics` · nhánh `main` · commit chốt: *(cập nhật khi chốt cuối buổi)*

## Thành viên

| STT | Họ tên              | MSSV        | Email                          | GitHub           | Vai trò                         |
| --: | --------------------- | ----------- | ------------------------------ | ---------------- | ------------------------------- |
|   1 | Lê Anh Sơn          | 2A202603440 | sonleanh0289@gmail.com         | sonleanh0289-cmd | Người viết code                 |
|   2 | Nguyễn Quang Hiệp   | 2A202603509 | hiepqn1445@gmail.com           | hiepquangnguyen  | Người kiểm số                   |
|   3 | Lưu Văn Việt Đức    | 2A202603445 | luuvanvietduc@gmail.com        | IVietDucI        | Người gắn nhãn 1                |
|   4 | Hoàng Nguyên Long   | 2A202603476 | long.hoangnguyen0108@gmail.com | longhn-0108      | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## LeAnhSon-2A202603440

### Phần việc phụ trách

- Thiết lập môi trường Python (`.venv`) và viết toàn bộ mã nguồn tính toán trong `src/lab13.py` (CP1, CP2, CP4, hỗ trợ E1).
- Hỗ trợ kiểm tra cú pháp `pilot_plan.yaml` và điền số liệu tính thử E1 vào `report/team/chi_so.md`.

### Đóng góp cụ thể

- Hoàn thiện 3 hàm A1 đạt 3/3 phép thử (`1,20 · 1,25 · 1,25`), hàm `mo_hinh(...)` cho A2–A4 và B1–B4, hàm `co_mau(...)` + `statsmodels` cho D1 và chỉ số chạy thử D3/E1 trong `src/lab13.py`.
- Điền 3 chỉ số tính thử + 2 chỉ số tự đề xuất bảng E1 trong `report/team/chi_so.md` và hoàn thiện báo cáo cá nhân `report/team/2A202603440_LeAnhSon.md`.

### Bằng chứng

- `src/lab13.py` (chạy sạch từ đầu đến cuối, khớp 0% sai lệch với số đối chiếu và kết quả độc lập của Người kiểm số).
- `report/team/2A202603440_LeAnhSon.md`, `report/team/chi_so.md`.

## NguyenQuangHiep-2A202603509

### Phần việc phụ trách

- Người kiểm số: tính tay số đối chiếu A1, A2 độc lập với `src/lab13.py` và đối chiếu output của code.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4 và các câu trả lời), gắn nhãn `simulated` cho mọi số tính từ cột `_simulated`.
- Đối chiếu số trong `pilot_plan.yaml` (D1, D3), `chi_so.md` (E1, E2) và `bang_loi.md` (CP3).

### Đóng góp cụ thể

- Tính A1 bằng công thức (1,20 · 1,25 · 1,25) và tính A2 trực tiếp từ hai file CSV bằng thư viện chuẩn của Python: 4.373.585 đ ÷ 978 = 4.472 đ mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn 274,7 đ. Khớp output `src/lab13.py`, lệch 0%.
- Điền đủ `bang_chi_phi.md`: A2 9 dòng, A3 4 loại, A4 2 mức khối lượng, B1 9 kịch bản, B2 xếp hạng, B3 và B4 có số.
- Đối chiếu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, power 0,64), tỉ lệ mở lại 4,25% và 3,97%, ba chỉ số E1 (82,83% · 27,12% · 4,25%) và số trong hai dòng rủi ro E2: khớp output `src/lab13.py` và `bang_chi_phi.md`. Báo lại hai dòng khắc phục ca 18 và 19 trong `bang_loi.md` còn thiếu ngưỡng hoặc tần suất.

### Bằng chứng

- Commit `f9b914d`: `report/team/bang_chi_phi.md` và `report/team/2A202603509_NguyenQuangHiep.md`.
- Bảng tính tay A1, A2 trong mục 3 của `report/team/2A202603509_NguyenQuangHiep.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

### Đóng góp cụ thể

### Bằng chứng

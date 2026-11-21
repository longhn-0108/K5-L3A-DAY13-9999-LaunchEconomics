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

- Tính tay độc lập số liệu A1, A2 từ hai file CSV để kiểm chứng kết quả của `src/lab13.py`.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4), kiểm nhãn `simulated` và rà soát độ lệch số liệu.

### Đóng góp cụ thể

- Đối chiếu độc lập 100% số liệu A1, A2 (lệch 0% so với `src/lab13.py` và số mẫu hướng dẫn).
- Hoàn thiện trọn bộ bảng và câu trả lời A1–A4, B1–B4 trong `report/team/bang_chi_phi.md` và báo cáo cá nhân `report/team/2A202603509_NguyenQuangHiep.md`.

### Bằng chứng

- Commit `f9b914d`, `report/team/bang_chi_phi.md`, `report/team/2A202603509_NguyenQuangHiep.md`.

## LuuVanVietDuc-2A202603445

### Phần việc phụ trách

- Người gắn nhãn 1 ở CP3 (gắn nhãn độc lập 20 ca lỗi theo Google PAIR, tổng hợp `report/team/bang_loi.md`).
- Thiết kế kế hoạch pilot và hoàn thiện `report/team/pilot_plan.yaml` (CP4).

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, đối chiếu đạt đồng thuận 20/20 (100%) và hoàn thiện bảng đề xuất khắc phục 5 ca trong `report/team/bang_loi.md`.
- Hoàn thiện đầy đủ chú thích D1, D2, D3, phương án chia 20 + 20 nhân viên (MDE 6 điểm, power ~0,64 ở 5 điểm) và 3 luật dừng đủ 4 vế trong `report/team/pilot_plan.yaml`.

### Bằng chứng

- Commit `dc5dd8d` (`report/team/bang_loi.md`), commit `a187e40` (`report/team/pilot_plan.yaml`).

## HoangNguyenLong-2A202603476

### Phần việc phụ trách

- Quản lý repo nhóm, cập nhật `TEAM.md` và giữ hồ sơ `report/team/ho_so_launch_v0.md`.
- Người gắn nhãn 2 ở CP3 (gắn nhãn độc lập 20 ca lỗi).
- Hoàn thiện danh sách event, kiểm tra chéo, rủi ro kinh tế (E2) trong `report/team/chi_so.md` và báo cáo nhóm `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, đối chiếu đạt đồng thuận 20/20 (100%) trong `report/team/bang_loi.md`.
- Hoàn thiện 10 event có `trace_id`, mục kiểm tra chéo và 3 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
- Tổng hợp đầy đủ 7 mục và chốt đề xuất **Go có điều kiện** kèm 4 điều kiện cụ thể trong `report/team/ho_so_launch_v0.md`; viết `report/team/group_report.md` và `report/team/2A202603476_HoangNguyenLong.md`.

### Bằng chứng

- Commit `36001be`, `TEAM.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603476_HoangNguyenLong.md`.

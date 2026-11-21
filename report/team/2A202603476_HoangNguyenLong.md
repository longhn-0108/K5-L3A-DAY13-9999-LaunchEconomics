# Báo cáo cá nhân — HoangNguyenLong-2A202603476

## 1. Thông tin thành viên

- Họ tên: Hoàng Nguyên Long
- MSSV: 2A202603476
- Email: long.hoangnguyen0108@gmail.com
- GitHub: longhn-0108
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Quản lý repo nhóm (`K5-L3A-DAY13-9999-LaunchEconomics`) và cập nhật thông tin nhóm trong `TEAM.md`.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR ở CP3 và đối chiếu với Người gắn nhãn 1 (Lưu Văn Việt Đức) trong `report/team/bang_loi.md`.
- Hoàn thiện danh sách event, kiểm tra chéo và bảng rủi ro kinh tế (E2) trong `report/team/chi_so.md`.
- Giữ và tổng hợp hồ sơ một trang `report/team/ho_so_launch_v0.md` (đủ 7 mục, đúng nhãn `simulated`, chốt đề xuất **Go có điều kiện** kèm điều kiện và con số bất lợi).
- Tổng hợp báo cáo nhóm `report/team/group_report.md` và tham gia duyệt chéo Gate 2a (`report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

- Khởi tạo repo nhóm, điền thông tin nhóm và tổng hợp mục đóng góp thành viên trong `TEAM.md`.
- Gắn nhãn độc lập 20 ca lỗi (phân bổ: 4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm), đối chiếu với Người gắn nhãn 1 đạt đồng thuận 20/20 (100%) trong `report/team/bang_loi.md`.
- Điền 10 event có `trace_id`, mục kiểm tra chéo cho cả 5 chỉ số E1 và 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy vào `report/team/chi_so.md`.
- Tổng hợp đầy đủ 7 mục vào `report/team/ho_so_launch_v0.md`, gắn đúng trạng thái (`Giả lập` cho mục 1, 2, 3, 7; `Xong, có bằng chứng` cho mục 4, 5, 6), và chốt đề xuất **Go có điều kiện** (nêu rõ đánh đổi power ~0,64 ở mức 5 điểm và kịch bản xem lại 100% 0,98×–1,03× [simulated] cùng 4 điều kiện có người phụ trách và ngày kiểm tra).
- Viết báo cáo nhóm ngắn `report/team/group_report.md`.

## 4. Bằng chứng

- Repo nhóm: `https://github.com/longhn-0108/K5-L3A-DAY13-9999-LaunchEconomics`
- Các file phụ trách/cập nhật: `TEAM.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini):** Dùng để đọc nhanh tài liệu đề bài, lên kế hoạch chia vai 4 người theo mốc giờ, rà soát checklist nộp bài (`RUBRIC.md`, `SUBMISSION.md`), hỗ trợ soạn cấu trúc trình bày cho `ho_so_launch_v0.md`, `chi_so.md` và `group_report.md`.
- **Cách tự kiểm tra:** Đối chiếu trực tiếp mọi con số trong `ho_so_launch_v0.md` và `chi_so.md` với output của `src/lab13.py`, `bang_chi_phi.md` và `pilot_plan.yaml`; rà soát toàn bộ thư mục `report/team/` để đảm bảo đủ nhãn `simulated`, tuân thủ quy tắc 5 của `README.md`, không ghi vai trò chung chung và không còn dấu `?` trong `pilot_plan.yaml`.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò Người gắn nhãn 2 kiêm giữ hồ sơ, đảm bảo hồ sơ Gate 2a hoàn chỉnh trước mốc 17:00 và thống nhất số liệu xuyên suốt từ A đến E.
- Điểm cần rút kinh nghiệm: cần cài sớm môi trường `.venv` trên máy cá nhân ngay từ đầu buổi để chủ động chạy chéo `src/lab13.py` và kiểm tra YAML song song với đồng đội.

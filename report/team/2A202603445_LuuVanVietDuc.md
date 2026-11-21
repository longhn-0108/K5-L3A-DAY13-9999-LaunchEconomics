# Báo cáo cá nhân — Lưu Văn Việt Đức — 2A202603445

## 1. Thông tin thành viên

- Họ tên: Lưu Văn Việt Đức
- MSSV: 2A202603445
- Email: luuvanvietduc@gmail.com
- Vai trong nhóm: TV3, người gắn nhãn 1. Nhóm 9999, lớp L3A.

## 2. Phần việc phụ trách

Gắn nhãn và phân tích lỗi ở CP3, hoàn thiện kế hoạch pilot CP4, đặc tả chỉ số và rủi ro kinh tế ở CP5 E1–E2.

## 3. Đóng góp cụ thể

- CP3: Gắn nhãn 20 ca, đối chiếu với Hoàng Nguyên Long và ghi đồng thuận 20/20. Hoàn thiện bảng đề xuất khắc phục cho 5 ca đại diện.
- CP4: Điền D1–D3. Viết phương án 20 nhân viên dùng trợ lý và 20 đối chứng, nêu đánh đổi MDE 6 điểm phần trăm và power khoảng 0,64 ở mức 5 điểm. Viết ba luật dừng và kiểm tra YAML.
- CP5: Chạy và đối chiếu ba số E1 là 994/1.200, 48/177 và 51/1.200. Đặc tả hai chỉ số bổ sung, 10 event có trace_id và hai rủi ro chi phí có nhãn simulated.

## 4. Bằng chứng

- CP3: [bang_loi.md](bang_loi.md), commit `dc5dd8d`.
- CP4: [pilot_plan.yaml](pilot_plan.yaml), commit `a187e40`.
- CP5: [chi_so.md](chi_so.md), commit `997844f`. Xử lý xung đột với main tại `92525b1`.

## 5. Công cụ AI đã dùng

Dùng ChatGPT để rà yêu cầu từng checkpoint và Codex để hỗ trợ chỉnh tài liệu. Kiểm tra bằng cách chạy `python lab13.py`, đối chiếu số E1 với CSV, kiểm tra `yaml.safe_load` và chạy `git diff --check`.

## 6. Tự đánh giá

Tôi đã nối được các luật dừng ở CP4 với dữ liệu cần ghi ở CP5. Kết quả E1 hiện mô tả đợt chạy thử giả lập. Để ước tính tác động, pilot cần dữ liệu đủ thời gian theo dõi từ cả nhánh trợ lý và nhánh đối chứng.
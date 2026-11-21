"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py   (cần pandas, numpy, scipy, statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26             # đồng cho 1.000 token đầu vào
GIA_RA = 130             # đồng cho 1.000 token đầu ra
GIA_TOOL = 15            # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000        # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000         # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Số GIẢ LẬP, phải ghi nhãn simulated.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('nan')
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def in_nhiem_vu_a(runs, reqs):
    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    print(f"Token (mọi lần chạy):           {kq['token']:>12,.0f} đ  [đo từ trace]")
    print(f"Tool ({int(runs['tool_calls'].sum()):,} lần gọi):          {kq['tool']:>12,.0f} đ  [đo từ trace]")
    print(f"Trong đó lần chạy 2 & 3:        {kq['chay_lai']:>12,.0f} đ  [đo từ trace]")
    print(f"Xem lại ({int(reqs['phut_xem_lai_simulated'].sum()):,} phút):            {kq['xem_lai']:>12,.0f} đ  [simulated]")
    print(f"Làm lại ({int(reqs['phut_lam_lai_simulated'].sum()):,} phút):          {kq['lam_lai']:>12,.0f} đ  [simulated]")
    print(f"Tổng chi phí:                   {kq['tong']:>12,.0f} đ  [có phần simulated]")
    print(f"Số việc thành công:             {kq['thanh_cong']:>12,d} / {len(reqs):,d}")
    print(f"Chi phí mỗi việc thành công:    {kq['cps']:>12,.0f} đ  [simulated]")
    print(f"Hoá đơn token+tool / yêu cầu:   {kq['hoa_don_moi_yc']:>12,.1f} đ  [đo từ trace]")
    print(f"-> CPS gấp {kq['cps'] / kq['hoa_don_moi_yc']:.1f} lần hoá đơn chia số yêu cầu.")
    print(f"-> Tỉ trọng: làm lại {kq['lam_lai'] / kq['tong'] * 100:.1f}% [simulated], "
          f"xem lại {kq['xem_lai'] / kq['tong'] * 100:.1f}% [simulated].")
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"-> Chi phí cả hệ thống / yêu cầu: {he_thong_moi_yc:,.0f} đ "
          f"({he_thong_moi_yc / BASELINE:.2f}x của 12.000 đ) [simulated].")

    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'TL thành công':>14s} {'Lần chạy/YC':>12s} {'CPS [sim]':>12s} {'So 12k':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl_tc = r['thanh_cong'] / len(sub) * 100
        tb_chay = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>7d} {tl_tc:>13.1f}% {tb_chay:>12.2f} {r['cps']:>10,.0f} đ {r['cps'] / BASELINE:>7.2f}x")

    print('\nTỉ lệ status == ok theo loại và lần thử (attempt):')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    pivot_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(pivot_ok.loc[['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']].round(1).to_string())

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = r_pv['thanh_cong'] / len(reqs)
    for nhan, khoi_luong in [('45.000 yêu cầu/tháng', 45_000), ('Một nửa (22.500/tháng)', 22_500)]:
        viec_thang = khoi_luong * ti_le_tc_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thang
        tong_cps = r_pv['cps'] + co_dinh_moi_viec
        print(f"{nhan:24s} | Việc TC/tháng: {viec_thang:>7,.0f} | Cố định/việc: {co_dinh_moi_viec:>6,.0f} đ "
              f"| CPS+cố định: {tong_cps:>6,.0f} đ ({tong_cps / BASELINE:.2f}x) [simulated]")
    return kq


def in_nhiem_vu_b(runs, reqs, kq_goc):
    print('\n=== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = kq_goc['cps']
    print(f"{'Gốc (A2)':28s} {goc:>10,.0f} đ")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        print(f"{ten:28s} {cps:>10,.0f} đ ({pct:+6.1f}%)")

    print('\n=== B2 · ĐỔI MỘT CẶP ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"Token x2 + Xem lại x2:       {cap:>10,.0f} đ ({(cap / goc - 1) * 100:+6.1f}%) [simulated]")

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI & CHI PHÍ CẢ HỆ THỐNG [simulated] ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý':>14s} {'Không TC':>10s} {'Cả hệ thống':>14s} {'CPS':>10s}")
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_ht = r['tong'] + khong_tc * BASELINE
        print(f"{str(k) + ' lần':10s} {r['tong']:>12,.0f} đ {khong_tc:>10d} {ca_ht:>12,.0f} đ {r['cps']:>8,.0f} đ")

    print('\n=== B4 · XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) [simulated] ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    so_tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    token_tool_pv = (
        (runs_pv['tokens_in'] / 1000.0 * GIA_VAO + runs_pv['tokens_out'] / 1000.0 * GIA_RA).sum()
        + (runs_pv['tool_calls'] * GIA_TOOL).sum()
    )
    tien_xem_100 = co_ok * 5 * LUONG_PHUT
    phut_ll_tb = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated'].mean()

    for nhan, phut_ll in [('Đề bài (9 phút/ca làm lại)', 9.0),
                          (f'Dữ liệu thực tế ({phut_ll_tb:.1f} phút/ca)', phut_ll_tb)]:
        tien_ll = so_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = token_tool_pv + tien_xem_100 + tien_ll
        cps_b4 = tong_b4 / so_tc
        hoa_von_phut = (so_tc * BASELINE - token_tool_pv - tien_ll) / (co_ok * LUONG_PHUT)
        print(f"{nhan:34s} -> Tổng: {tong_b4:>10,.0f} đ | CPS: {cps_b4:>6,.0f} đ "
              f"({cps_b4 / BASELINE:.2f}x) | Hoà vốn: <= {hoa_von_phut:.1f} phút/lần xem")


def in_nhiem_vu_d_va_e(reqs):
    print('\n=== D1 · CỠ MẪU PILOT (baseline=0.70, +5 điểm, alpha=0.05, power=0.80, ICC=0.02) ===')
    icc = 0.02
    n_5 = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_5 * de_75)
    so_nv_moi_nhom = math.ceil(n_nv_75 / 75)
    n_max_20nv = int(20 / icc)
    n_max_6depot = int(6 / icc)
    n_6 = co_mau(0.70, 0.76)
    # 20m / (1 + (m - 1)*0.02) >= n_6  =>  (20 - 0.02*n_6)*m >= 0.98*n_6
    m_6 = math.ceil((1 - icc) * n_6 / (20 - icc * n_6))
    de_6 = 1 + (m_6 - 1) * icc
    h_5 = proportion_effectsize(0.75, 0.70)
    power_o_5diem = NormalIndPower().power(effect_size=h_5, nobs1=n_6, alpha=0.05, ratio=1.0)

    print(f"a) Chia theo yêu cầu (MDE 5 điểm):          {n_5:,d} yêu cầu/nhóm")
    print(f"b) Theo nhân viên (m=75, DE={de_75:.2f}):          {n_nv_75:,d} yêu cầu/nhóm "
          f"-> {so_nv_moi_nhom} NV/nhóm (tổng {so_nv_moi_nhom * 2} > 40 NV)")
    print(f"c) 20 nhân viên/nhóm (giới hạn c/ICC):      tối đa {n_max_20nv:,d} < {n_5:,d} (không đạt 5 điểm)")
    print(f"d) 6 depot/nhóm (giới hạn c/ICC):           tối đa {n_max_6depot:,d}")
    print(f"e) Mức chênh 6 điểm (n={n_6}/nhóm, 20 NV):    m >= {m_6} yêu cầu/người (DE={de_6:.2f})")
    print(f"   -> Nếu tác động thật chỉ 5 điểm (n={n_6}): power = {power_o_5diem:.2f}")

    print('\n=== D3 & E1 · CHỈ SỐ TRONG ĐỢT CHẠY THỬ (1.200 YÊU CẦU) ===')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0))
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1)
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    an_toan_pv = (pv['mo_lai_trong_7_ngay'] == 1)

    print(f"Chỉ số chính (đóng 24h, không mở lại 7 ngày): {chinh.mean() * 100:.2f}% ({int(chinh.sum())}/{len(reqs)})")
    print(f"Chỉ số dùng (tỉ lệ bỏ qua gợi ý sua+bo):      {bo_qua.mean() * 100:.2f}% ({int(bo_qua.sum())}/{len(xem)})")
    print(f"Chỉ số an toàn (mở lại 7 ngày - toàn mẫu):    {an_toan.mean() * 100:.2f}% ({int(an_toan.sum())}/{len(reqs)})")
    print(f"Chỉ số an toàn (mở lại 7 ngày - noi_dia+hn):  {an_toan_pv.mean() * 100:.2f}% ({int(an_toan_pv.sum())}/{len(pv)})")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    kq_goc = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, kq_goc)
    in_nhiem_vu_d_va_e(reqs)

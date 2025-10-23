
from asm_nv import *

# Danh sách nhân viên
ds_nv = []

#Y1
def nhap_danh_sach_va_luu_file():
    print("Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"\n--- Nhân viên thứ {i+1} ---")
        loai = input("Loại (1.Hành chính, 2.Tiếp thị, 3.Trưởng phòng): ")

        ma_nv = input("Mã nhân viên: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == "1":
            nv = nhanVien(ma_nv, ho_ten, luong)
        elif loai == "2":
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Hoa hồng (%): "))
            nv = TiepThi(ma_nv, ho_ten, luong, doanh_so, hoa_hong)
        elif loai == "3":
            phu_cap = float(input("Phụ cấp trách nhiệm: "))
            nv = TruongPhong(ma_nv, ho_ten, luong, phu_cap)
        else:
            print(" Loại không hợp lệ, bỏ qua!")
            continue

        ds_nv.append(nv)
    print(" Đã nhập danh sách nhân viên xong.")
# Y2
def doc_va_xuat_danh_sach():
    print("Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.")
# Y3
def tim_nhan_vien_theo_ma():
    print("Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
    ma = input("Nhập mã nhân viên cần tìm: ")
    print(f"{'Mã NV':<10}{'Họ tên':<25}{'Lương':<15}{'Thu nhập':<15}")
    for nv in ds_nv:
        if nv.ma_nv == ma:
            print(nv)
            return
    print("Không tìm thấy nhân viên.")
# Y4
def xoa_nhan_vien_theo_ma():
    print("Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
# Y5
def cap_nhat_thong_tin_nhan_vien():
    print("Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.")
# Y6

def tim_nhan_vien_theo_khoang_luong():
    print("Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
    min_l = float(input("Nhập lương tối thiểu: "))
    max_l = float(input("Nhập lương tối đa: "))
    print(f"\nNhân viên có lương từ {min_l:,} đến {max_l:,}:")
    print(f"{'Mã NV':<10}{'Họ tên':<25}{'Lương':<15}{'Thu nhập':<15}")
    for nv in ds_nv:
        if min_l <= nv.luong <= max_l:
            print(nv)
# Y7
def sap_xep_theo_ho_ten():
    print("Y7. Sắp xếp nhân viên theo họ và tên.")
    ds_nv.sort(key=lambda nv: nv.ho_ten.split()[-1])
    print(" Đã sắp xếp danh sách theo tên.")
    for nv in ds_nv:
        print(nv)

# Y8
def sap_xep_theo_thu_nhap():
    print("Y8. Sắp xếp nhân viên theo thu nhập.")
    ds_nv.sort(key=lambda nv: nv.getThuNhap(), reverse=True)
    print("Đã sắp xếp danh sách theo thu nhập giảm dần.")
    for nv in ds_nv:
        print(nv)

# Y9
def xuat_5_nhan_vien_thu_nhap_cao_nhat():
    print("Y9. Xuất 5 nhân viên có thu nhập cao nhất.")
    top5 = sorted(ds_nv, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    print("TOP 5 NHÂN VIÊN CÓ THU NHẬP CAO NHẤT:")
    print(f"{'Mã NV':<10}{'Họ tên':<25}{'Lương':<15}{'Thu nhập':<15}")
    for nv in top5:
        print(nv)



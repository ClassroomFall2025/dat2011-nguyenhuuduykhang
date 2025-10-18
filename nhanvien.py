# class NhanVien:
#     def __init__(self, ma_nv, ho_ten, luong):
#         self.ma_nv = ma_nv
#         self.ho_ten = ho_ten
#         self.luong = luong

#     # Hàm tính thu nhập (được ghi đè ở lớp con)
#     def getThuNhap(self):
#         return self.luong

#     # Xuất thông tin nhân viên
#     def xuat(self):
#         print(f"Mã NV: {self.ma_nv:<5} | Họ tên: {self.ho_ten:<20} | "
#               f"Lương: {self.luong:>10,.0f} | Thu nhập: {self.getThuNhap():>10,.0f}")
# class TiepThi(NhanVien):
#     def __init__(self, ma_nv, ho_ten, luong, doanh_so, hoa_hong):
#         super().__init__(ma_nv, ho_ten, luong)  # Gọi lại constructor lớp cha
#         self.doanh_so = doanh_so
#         self.hoa_hong = hoa_hong

#     # Ghi đè phương thức tính thu nhập
#     def getThuNhap(self):
#         return self.luong + self.doanh_so * self.hoa_hong

#     def xuat(self):
#         print(f"Mã NV: {self.ma_nv:<5} | Họ tên: {self.ho_ten:<20} | Tiếp Thị | "
#               f"Lương: {self.luong:>10,.0f} | Thu nhập: {self.getThuNhap():>10,.0f}")
# class TruongPhong(NhanVien):
#     def __init__(self, ma_nv, ho_ten, luong, phu_cap):
#         super().__init__(ma_nv, ho_ten, luong)
#         self.phu_cap = phu_cap

#     def getThuNhap(self):
#         return self.luong + self.phu_cap

#     def xuat(self):
#         print(f"Mã NV: {self.ma_nv:<5} | Họ tên: {self.ho_ten:<20} | Trưởng Phòng | "
#               f"Lương: {self.luong:>10,.0f} | Thu nhập: {self.getThuNhap():>10,.0f}")




import csv

def nhap_danh_sach_va_luu_file():
    print("Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    danh_sach = []

    while True:
        ma_nv = input("Nhập mã nhân viên: ")
        ho_ten = input("Nhập họ tên: ")
        luong = float(input("Nhập lương: "))
        phong_ban = input("Nhập phòng ban: ")

        # Thêm nhân viên vào danh sách
        danh_sach.append([ma_nv, ho_ten, luong, phong_ban])

        tiep = input("Bạn có muốn nhập thêm nhân viên khác không? (c/k): ")
        if tiep.lower() != 'c':
            break

    # Ghi danh sách vào file CSV
    with open("nhanvien.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Mã NV", "Họ tên", "Lương", "Phòng ban"])
        writer.writerows(danh_sach)
   
    print(" Đã lưu danh sách nhân viên vào file nhanvien.csv")

def doc_va_xuat_danh_sach(ten_file="nhanvien.csv"):
    print("Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.")
    
    try:
        with open(ten_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # bỏ dòng tiêu đề

            print("\n--- DANH SÁCH NHÂN VIÊN ---")
            for row in reader:
                ma_nv, ho_ten, luong, phong_ban = row
                print(f"Mã NV: {ma_nv} | Họ tên: {ho_ten} | Lương: {luong} | Phòng ban: {phong_ban}")

    except FileNotFoundError:
        print(f"⚠️ File {ten_file} chưa tồn tại. Hãy chạy chức năng Y1 trước để tạo file.")
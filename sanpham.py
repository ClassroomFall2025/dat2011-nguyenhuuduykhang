# class sanpham:
#     def __init__(self, tensp, gia, giam_gia=0):
#         self.__tensp = tensp
#         self.__gia = gia
#         self.__giam_gia = giam_gia

#     def get_ten(self):
#         return self.__tensp

#     def get_ten(self, ten_sp):
#         self.__tensp = ten_sp

#     def get_gia(self):
#         return self.__gia
    
#     def set_gia(self, gia_sp):
#         self.__gia = gia_sp

#     def get_giam_gia(self):
#         return self.__giam_gia

#     def get_giam_gia(self, giam_gia_sp):
#          self.__giam_gia = giam_gia_sp

#     def thue_nhap_khau(self):
#         return self.__gia * 0.1
    
#     def nhap_thong_tin(self):
#         self.__tensp = input("Nhập tên sản phẩm: ")
#         self.__gia = float(input("Nhập giá sản phẩm: "))
#         self.__giam_gia = float(input("Nhập giảm giá sản phẩm (%): "))

#     def xuat_thong_tin(self):
#         print(f"Tên sản phẩm: {self.__tensp}")
#         print(f"Giá sản phẩm: {self.__gia}")
#         print(f"Giảm giá: {self.__giam_gia}%")
#         print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")

from asm_nv import NhanVien, TiepThi, TruongPhong
def nhap_danh_sach_va_luu_file(self):
    print("Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    self.danh_sach_nv = []
    while True:
        print("\n--- NHẬP NHÂN VIÊN ---")
        print("1. Nhân viên hành chính")
        print("2. Nhân viên tiếp thị")
        print("3. Trưởng phòng")
        print("0. Thoát nhập")
        chon = input(" Chọn loại nhân viên: ")

        if chon == "0":
            break

        ma_nv = input("Nhập mã nhân viên: ")
        ho_ten = input("Nhập họ tên: ")
        luong = float(input("Nhập lương cơ bản: "))

        if chon == "1":
            nv = NhanVien(ma_nv, ho_ten, luong)
        elif chon == "2":
            doanh_so = float(input("Nhập doanh số: "))
            ty_le = float(input("Nhập tỷ lệ hoa hồng (vd: 0.05): "))
            nv = TiepThi(ma_nv, ho_ten, luong, doanh_so, ty_le)
        elif chon == "3":
            luong_trach_nhiem = float(input("Nhập lương trách nhiệm: "))
            nv = TruongPhong(ma_nv, ho_ten, luong, luong_trach_nhiem)
        else:
            print(" Lựa chọn không hợp lệ.")
            continue
        self.danh_sach_nv.append(nv)
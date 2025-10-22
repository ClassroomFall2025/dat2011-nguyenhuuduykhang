class NhanVien:
    def __init__(self, ma, ho_ten, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.luong = luong

    def getThuNhap(self):
        return self.luong

    def getThueThuNhap(self):
        thu_nhap = self.getThuNhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return thu_nhap * 0.10
        elif thu_nhap >= 15000000:
            return thu_nhap * 0.12
        else:
            return 0
    def xuat(self):
        print(f"Mã NV: {self.ma}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Lương: {self.luong:,.0f}")
        print(f"Thu nhập: {self.getThuNhap():,.0f}")
        print(f"Thuế thu nhập: {self.getThueThuNhap():,.0f}")
        print("-" * 40)


class TiepThi(NhanVien):
    def __init__(self, ma, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma, ho_ten, luong)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def getThuNhap(self):
        return self.luong + self.doanh_so * self.hoa_hong


class TruongPhong(NhanVien):
    def __init__(self, ma, ho_ten, luong, luong_trach_nhiem):
        super().__init__(ma, ho_ten, luong)
        self.luong_trach_nhiem = luong_trach_nhiem

    def getThuNhap(self):
        return self.luong + self.luong_trach_nhiem

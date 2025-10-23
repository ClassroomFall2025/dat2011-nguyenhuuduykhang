class nhanVien:
    def __init__(self, ma_nv, ho_ten, luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong = float(luong)

    def getThuNhap(self):
        """Thu nhập mặc định = lương"""
        return self.luong

    def getThueThuNhap(self):
        """Tính thuế theo quy định"""
        thu_nhap = self.getThuNhap()
        if thu_nhap < 9_000_000:
            return 0
        elif thu_nhap <= 15_000_000:
            return (thu_nhap - 9_000_000) * 0.1
        else:
            return (thu_nhap - 15_000_000) * 0.12 + 600_000

    def __str__(self):
        return f"{self.ma_nv:<10}{self.ho_ten:<25}{self.luong:<15,.0f}{self.getThuNhap():<15,.0f}"


class TiepThi(nhanVien):
    def __init__(self, ma_nv, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)

    def getThuNhap(self):
        return self.luong + self.doanh_so * self.hoa_hong / 100


class TruongPhong(nhanVien):
    def __init__(self, ma_nv, ho_ten, luong, phu_cap):
        super().__init__(ma_nv, ho_ten, luong)
        self.phu_cap = float(phu_cap)

    def getThuNhap(self):
        return self.luong + self.phu_cap
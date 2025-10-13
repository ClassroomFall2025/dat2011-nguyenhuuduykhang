class Hcn:
    def __init__(self, chieu_dai, chieu_rong):
        self.__chieu_dai = chieu_dai
        self.__chieu_rong = chieu_rong
    def get_chu_vi(self):
        return (self.__chieu_dai + self.__chieu_rong) * 2
    def get_dien_tich(self):
        return self.__chieu_dai * self.__chieu_rong
    def xuat(self):
        print(f"chiều dài hình chữ nhật: {self.__chieu_dai}")
        print(f"chiều rộng hình chữ nhật: {self.__chieu_rong}")
        print(f"chu vi hình chữ nhật: {self.get_chu_vi()}")
        print((f"diện tích hình chữ nhật: {self.get_dien_tich()}"))
        
    def nhap_thong_tin(self):
        self.__chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
        self.__chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
class HinhVuong(Hcn):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)
    def xuat(self):
        print(f"cạnh hình vuông: {self.canh}")
        print(f"chu vi hình vuông: {self.get_chu_vi()}")
        print(f"diện tích hình vuông: {self.get_dien_tich()}")
    
    def nhap_thong_tin(self):
        self.canh = float(input("Nhập cạnh hình vuông: "))
        super().__init__(self.canh, self.canh)

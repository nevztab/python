class araba():

    def __init__(self,marka,renk):
        self.fiyat=1500000
        self.renk=renk
        self.marka=marka
    
    def satınAl(self):
        print(f"{self.fiyat}₺ karşılığında {self.renk} bir {self.marka} satın aldınız")


araba(input("Hangi marka araba istersiniz: "),input("Peki rengi ne olsun: ")).satınAl()
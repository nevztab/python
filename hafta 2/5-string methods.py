
adSoyad='nevzat ulaş'

sonuc=adSoyad.capitalize()       #ilk harfi büyütme
print(sonuc)

sonuc=adSoyad.split()            #boşluktan ayır
print(sonuc)

sonuc=adSoyad.upper()            #hepsini büyüt
print(sonuc)

sonuc=adSoyad.lower()            #hepsini küçült
print(sonuc)

sonuc=adSoyad.strip()            # baş ve sondaki boşlukları siler
print(sonuc)

sonuc=adSoyad.index("e")         # karakterin bulunduğu konumu bumla (yok ise hata)
print(sonuc)

sonuc=adSoyad.count('d')         # karakterin bulunduğu konumu bumla (yok ise -1)
print(sonuc)

ad="nevzat"
soyad="ulaş"

isim=list((ad,soyad)) #liste oluşturma

oyunlar=["pes","gta vice city","cs 1.6"] #oyun listesi

print(len(oyunlar)) #liste eleman sayısı

print(oyunlar[1]) #2. elemanı yazdırma
print(oyunlar[:2]) #3. elemana kadar yazdırma




#----------------------METODLAR----------------------#

print(oyunlar.append("minecraft")) #listeye eleman ekleme
print(oyunlar.insert(0,"pes 2013")) #1. elemanı deiştirme
print(oyunlar.remove("minecraft")) #eleman silme
print(oyunlar.pop(0)) #sıra numarası ile eleman silme 
print(oyunlar.clear()) #listeyi temizleme
del oyunlar #listeyi silme



üyeler=["ahmet","mehmet","ali","veli","hasan"]
print(üyeler.sort()) #A'dan z'ye sıralama
print(üyeler.reverse()) #tersine çevirme



oyunlar=["pes 2013","gta vice city","cs 1.6"] 
üyeler=["ahmet","mehmet","ali","veli","hasan"]

print(oyunlar+üyeler) #2 listeyi birleştirme
print(oyunlar.extend(üyeler)) #listeyi genişletme



#----------------------İNPUT----------------------#
def sorgu():
    bilgi=input("Adını soyadını ve yaşını öğrenebilirmiyim:\n").split()
    if len(bilgi)!=3:
        print("eksik feya yanlış yazdınız")
        sorgu()
    ad=bilgi[0]
    soyad=bilgi[1]
    yas=int(bilgi[2])
    
    print(f"Hoşgeldin {ad}")

sorgu()




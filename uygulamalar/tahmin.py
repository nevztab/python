import random


puan=[100,100,100,100,100]
yapma=0
sayi=0


def bul(a,puan,yapma,sayi):
    if a==True:   
        if yapma==0:
            sayi=random.randint(1,10)
            tahmin=int(input("1 ile 10 arasında sayı girin: "))

        if yapma==1:
            sayi=random.randint(1,25)
            tahmin=int(input("1 ile 25 arasında sayı girin: "))
    
        if yapma==2:
            sayi=random.randint(1,50)
            tahmin=int(input("1 ile 50 arasında sayı girin: "))

        if yapma==3:
            sayi=random.randint(1,75)
            tahmin=int(input("1 ile 75 arsında sayı girin: "))
    
        if yapma==4:
            sayi=random.randint(1,100)
            tahmin=int(input("1 ile 100 arasında sayı girin: "))

    if a==False:
        tahmin=int(input("Tekrar sayı girin: "))

    if sayi>tahmin:
        puan[yapma]=puan[yapma]-10
        print("Yukarı")
        bul(False,puan,yapma,sayi)

    if sayi<tahmin:
        puan[yapma]=puan[yapma]-10
        print("Aşşağı")
        bul(False,puan,yapma,sayi)

    if sayi==tahmin:
        buldun(yapma)

    a=False

def buldun(yapma):
    yapma=yapma+1
    if yapma==5:
        puanort=int((puan[0]+puan[1]+puan[2]+puan[3]+puan[4])/5)
        if puanort<0:
            print("Kaybettiniz")
        else:
            print(f"Tebrikler, 100/{puanort} puan aldınız")


    if yapma!=5:
        print("Tebrikler bir sonraki aşamaya geçtin")
        bul(True,puan,yapma,sayi)
    
bul(True,puan,yapma,sayi)

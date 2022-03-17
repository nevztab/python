for i in range (10): #10 kez hello yaz
    print ('hello')


for i in range(10): #0 dan 9 a i yi yaz
    print(i)


listem= [1, 2,3,4]

for eleman in listem: #listedeki elemanları 2 ile çarparak yaz
    print (eleman*2)


for sayi in range (50,100): #50 den 100 e kadar tek/çift yazdırma

    if sayi%2==0: 
        print (f'çift {sayi}') 

    elif sayi%2==1: 
        print (f' tek {sayi}')



toplam=0
sayilar=[13,15,45,4,50]

for i in sayilar: #toplam değ,erini eski toplam değerine listenin elamnlarını sırayla ekleme
    toplam=toplam+i

print(toplam)

for i in sayilar 
 if i>10:
    print(i)

arkadaslar=list(('fatmanur', 'ayşe', 'hakan'))
 
for i in arkadaslar:
   if (len(i)>5): print (i)

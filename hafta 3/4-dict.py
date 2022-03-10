
sozluk={

'bmw': 'almanya', 'togg' : 'türkiye',

'yil': 1000

}

#elemanlar erişim sonuc=sozluk.get('yil')

sonuc=sozluk['bmw'] sonuc=sozluk.keys ()

sonuc=sozluk.values() sonuc-sozluk.items()

print (sonuc)

sozluk.pop('togg')

sozluk.popitem() 
sozluk.clear() 
del sozluk['yil'] 

print (sozluk)

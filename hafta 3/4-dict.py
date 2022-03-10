sozluk={
'bmw': 'almanya ',
'togg' : 'türkiye',
'yil': 1000
}

#-----------------metods-----------------#
sozluk.get('yil') 
sozluk['bmw'] 
sozluk.keys()
sozluk.values()
sozluk.items()
sozluk.pop('togg')
sozluk.popitem() 
sozluk.clear() 
del sozluk['yil'] 

print (sozluk)

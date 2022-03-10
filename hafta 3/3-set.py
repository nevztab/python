oyunlar={'Valorant', 'Pubg', 'Cs Go', 'Mortal Combat'}
cikisTarihleri=[1990, 2000, 2010]

oyunlar.add('Pes 13') #ilk indexe ekle
oyunlar.update(cikisTarihleri) #set i cikisTarihleri listesi ekleyerek güncelle
oyunlar.remove(1995) #eleman siler. bulamazsa uyarı verir
oyunlar.discard (1995) #eleman siler. bulamazsa uyarı vermez
oyunlar.clear() #set listesinin içini boşalt

print (oyunlar)

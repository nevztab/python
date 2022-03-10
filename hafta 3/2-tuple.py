arabalar=("bmw","mercedes","supra") #tuple liste oluşturma

print(arabalar)
print(arabalar.count("bmw")) #adedini bulma
print(arabalar.count("supra")) #index numarasını bulma


#---------------Listeyi Güncelleme---------------#

x = list(arabalar) #tuple => list
x[1] = "tesla" #listeye ekleme
arabalar = tuple(arabalar) #list => tuple

print(arabalar)

#---------------Listeyi Güncelleme---------------#

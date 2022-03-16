a=20
b=15

if a>b:
    print(f'{a} bayktür {b} den')

elif a<b:
    print (f' {a} küçüktür {b} den')

else:
    print (f'{a} denktir {b} ye')

if a>b:
    if a%2==0:
        print (f'{a} büyüktür {b} den ve {a} çifttir')

elif a%2==1:
    print (f'{a} büyüktür {b} den ve {a} tektir')

elif a<b:
    print (f'{a} küçüktür {b} den')

else:
    print (f'{a} denktir {b} ye')

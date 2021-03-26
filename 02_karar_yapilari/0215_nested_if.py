
sayi=int(input("Lütfen bir sayi giriniz:"))

if sayi>0:
    if sayi<=100:
        print("Sayi 0 la yüz arasındadır.")
    elif sayi>100:
        print("Sayi 100'den büyüktür")
else:
    sayi=int(input("Lütfen yeni bir sayi giriniz:"))
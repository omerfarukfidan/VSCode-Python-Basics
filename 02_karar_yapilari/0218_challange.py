sayi1 = int(input("Lütfen ilk sayiyi giriniz: "))
sayi2 = int(input("Lütfen ikicni sayiyi giriniz: "))

if sayi1 % sayi2 == 0:
    print(f"{sayi1}, {sayi2}'ye tam bölünür!!!")
elif sayi1 % sayi2 != 0:
    print(f"{sayi1}, {sayi2}'ye tam bölünmez!!!")

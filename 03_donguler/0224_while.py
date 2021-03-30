teklerinToplami=0
ciftlerinToplami=0
sayi=int(input("lütfen bir sayı giriniz,çıkan için 0 a basınız :"))
while sayi!=0:
    if sayi%2==0:
        ciftlerinToplami+=sayi
    else:
        teklerinToplami+=sayi
        

    sayi=int(input("lütfen bir sayı giriniz,çıkan için 0 a basınız :"))
print(f"tek sayıların toplami {teklerinToplami} dır.")
print(f"çift sayıların toplami {ciftlerinToplami} dır.")
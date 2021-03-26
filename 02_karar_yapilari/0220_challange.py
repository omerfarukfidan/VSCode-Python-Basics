

sinavNotu1, sinavNotu2 = int(input("İlk sınav notunu giriniz: ")), int(input("İkinci sınav notunu giriniz: "))


ortalama = (sinavNotu1+sinavNotu2)/2

if sinavNotu1>100:
    print("100'den büyük bir not giremezsiniz lütfen tekrar giriniz:")

elif sinavNotu2>100:
    print("100'den büyük bir not giremezsiniz lütfen tekrar giriniz:")

else:

    if ortalama >= 85:
        print(f"yıl sonu notu {ortalama}, başarı durumu PEKİYİ")
    elif ortalama >= 70:
        print(f"yıl sonu notu {ortalama}, başarı durumu İYİ")
    elif ortalama >= 55:
        print(f"yıl sonu notu {ortalama}, başarı durumu ORTA")
    elif ortalama >= 45:
        print(f"yıl sonu notu {ortalama}, başarı durumu GEÇER")
    else:
        print(f"yıl sonu notu {ortalama}, başarı durumu GEÇMEZ")

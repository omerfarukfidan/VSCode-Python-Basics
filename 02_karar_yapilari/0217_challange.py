kisaKenar=int(input("Lütfen kısa kenar girniz:"))
uzunKenar=int(input("Lütfen uzun kenar giriniz:"))

if kisaKenar>uzunKenar:
    print("Kısa kenar uzun kenardan uzun olamaz lütfen tekrar giriniz:")
    kisaKenar=int(input("Lütfen kısa kenar girniz:"))
    uzunKenar=int(input("Lütfen uzun kenar giriniz:"))
elif uzunKenar>kisaKenar:
    print(f"Şeklin çevresi: {2*(kisaKenar+uzunKenar)}")    
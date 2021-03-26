"""
A Kenarı B Kenarı Eşit Girilir İse → Karenin Alanı ...
Ecodation Teknoloji
A Kenarı B Kenarı Eşit Girilmsez İse → Dikdörtgenin Alanı ...
"""

kenar1 = int(input("Lütfen ilk kenar uzunlugunu giriniz:"))
kenar2 = int(input("Lütfen ikinci kenar uzunlugunu giriniz:"))

if kenar1 == kenar2:
    print(f"Karenin alanı:{kenar1*kenar2}")
elif kenar1 != kenar2:
    print(f"Dikdörtgenin alanı:{kenar1*kenar2}")

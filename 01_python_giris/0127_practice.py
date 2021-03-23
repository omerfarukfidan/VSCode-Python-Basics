print("""
    Leylek Uygulamasına Hoşgeldiniz!!!
    Sürüş Ücreti → 0.59/dk.
""")
s = int(input("sürüş için geçen süre (saat)\t: "))
d = int(input("sürüş için geçen süre (dakika)\t: "))
toplamDakika = s*60
toplamDakika += d
print(f"sürüş için geçen toplam süre {s}:{d} - {toplamDakika} dk. da bitmiştir")
print(f"kartınızdan çekilen tutare {round(toplamDakika * 0.59, 2)}")
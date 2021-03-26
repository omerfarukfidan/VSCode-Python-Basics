kargo = 7.5
urunFiyati = float(
    input("Lütfen satın alınan ürünlerin toplam maliyetini giriniz:"))
odenecekTutar = urunFiyati + kargo
if urunFiyati > 250:
    odenecekTutar -= kargo 

print("Odenecek toplam tutar: ", odenecekTutar)

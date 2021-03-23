

urunFiyati=int(input("Aldığınız ürünün fiyatı:"))
kdvOranı=float(input("Kdv oranı:"))
print(f"Toplam tutar {urunFiyati+(urunFiyati*kdvOranı)}")
"""
Lütfen 1. Sayıyı Giriniz : 4
Lütfen 1. Sayıyı Giriniz : 6
Lütfen 1. Sayıyı Giriniz : 8
4, 6, 8 sayılarının ortalaması 6.0
"""
sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))
sayi3 = int(input("Lütfen 3. Sayıyı Giriniz : "))

ort = (sayi1+sayi2+sayi3)/3

print("{}, {}, {} sayılarının ortalaması: {}".format(sayi1,sayi2,sayi3, ort ))
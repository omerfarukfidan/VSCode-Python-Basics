"""
kullanıcı adı user
şifre 123

kullanıcı adı hatalı tekar deneyin yazdır kullancıı adı admin123 olmalı
kullanıcı adına admin girdi ama şifreyi yanlıs girdi şifre 123456
"""

kullaniciAdi = input("Lütfen kullanıcı adınızı giriniz: ")
parola = (input("Lütfen parolayı giriniz: "))

if kullaniciAdi == "admin1234":
    if parola == "123456":
        print("Login başarılı.")
elif kullaniciAdi != "admin1234":
    kullaniciAdi = input(
        "Yanlış giriş yaptınız lütfen tekrar kullanıcı adınızı giriniz: ")
    parola = (input("Lütfen parolayı giriniz: "))
elif parola != "123456":
    kullaniciAdi = input(
        "Yanlış giriş yaptınız lütfen tekrar kullanıcı adınızı giriniz: ")
    parola = (input("Lütfen parolayı giriniz: "))

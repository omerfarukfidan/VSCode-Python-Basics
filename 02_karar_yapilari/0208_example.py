grade1=int(input("Lütfen 1. sınav notunuzu giriniz:"))
grade2=int(input("Lütfen 2. sınav notunuzu giriniz:"))
grade3=int(input("Lütfen 3. sınav notunuzu giriniz:"))
gectiMi=True
if grade1<=30:
    gectiMi=False
if grade2<=30:
    gectiMi=False
if grade3<=30:
    gectiMi=False
if gectiMi==False:
    print("KALDINIZ")


sum=(grade1+grade2+grade3)/3

if sum>=50:
    print("GEÇTİNİZ")
print(f"Ortalama notunuz {sum}")


num = int(input("Kac adet maas girmek istediginizi giriniz: "))
i = 0
salary=0
while i < num:
    money = float(input(f"{i+1}. kisinin maasini giriniz:"))
    salary += money
    i+=1

    average = salary/num
if average > 1000:
        print("Firma iyi maas veriyor!")

elif average < 1000:
        

        print("Firma yetersiz maas veriyor!")

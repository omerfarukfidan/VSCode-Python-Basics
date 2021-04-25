sum=0
counter=0
print("Döngüden çıkış yapmak için \'q\' giriniz")
while(True):
    number = int(input("Lütfen bir sayi giriniz: "))
    if number%2 !=0:
        counter+=1
        sum+=number
        average=sum/counter
    elif number%2==0:
        print("Çift bir sayi girdiniz lütfen tekrar deneyin!!!")
        continue
    elif char(number)==q:
        break


print(f"Girilen tek sayilarin ortalamasi: {average}")
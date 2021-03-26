s1=int(input("Lütfen ilk sayiyi giriniz:"))
s2=int(input("Lütfen ikinci sayiyi giriniz:"))
s3=int(input("Lütfen üçüncü sayiyi giriniz:"))

if s1<s2:
    s1, s2=s2, s1
if s1<s3:
    s1, s3=s3, s1
if s2<s3:
    s2, s3=s3, s2

print(f"{s1}>{s2}>{s3}")
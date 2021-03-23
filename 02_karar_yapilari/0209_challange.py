"""
bakiyesi 5000 TL. olan bir banka müşterisi
EFT yapacaksın
bankaKodu = 101
eftBankaKodu = 102
%5
transfer ..... input

"""
totalMoney=5000

bankCode=101
otherBankCode=102

tester=int(input("If you want to continue with the same bank please enter 101, otherwise enter 102:"))
sendingMoney=int(input("How muchy money do you want to send:"))
if tester==102:
    totalMoney=5000-(sendingMoney+sendingMoney*0.05)
    print(f"Current money in your account: {totalMoney}")

if tester==101:
    print(f"Current money in your account: {totalMoney-sendingMoney}")
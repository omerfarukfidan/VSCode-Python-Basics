"""
Güncel Bakiyeniz 4000
yurtiçi uçuşlarda kdv %18
kontuar görevlisi  klavyeden bilet fiyatını
bavul ağırlığı 15kg. üzerinde her bir ağırlık için
bilet fiyatına 5 tl. ek ücret güncellemesi yapılacak
günün sonudna ekrana output
Güncel Bilet Fiyatı 150 TL.
"""

currentMoney=4000
valueOfTicket=float(input("Please enter the value of ticket:"))
weightOfBeg=20

if weightOfBeg>=15:
    diff=weightOfBeg-15
    valueOfTicket+=5
print(f"Current ticket cost: {valueOfTicket}")
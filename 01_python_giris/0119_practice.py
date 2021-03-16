
number = int(input("Please enter a three digit number:"))
num1=number//100
num2=(number-100*num1)//10
num3=(number-(10*num2+100*num1))

sum=num1+num2+num3
print("Sum=",sum)
#wap to reverse three digit number


num=int(input("enter the three digit number: "))
a=num%10
num=num//10
b=num%10
reserve=(a*10)+b
c=num//10
reserve=(reserve*10)+c
print("reserve:",reserve)

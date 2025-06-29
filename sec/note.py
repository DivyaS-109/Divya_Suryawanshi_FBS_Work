 #to fine the total number note foe a given amount.
amount=int(input("enter the amount: "))

#500
n500=amount//500
r_amount=amount %500

#200
n200=r_amount//200
r_ammount=amount %200

#100
n100=r_amount//100
r_ammount=amount %100

#50
n50=r_amount//50
r_ammount=amount %50

#20
n20=r_amount//20
r_ammount=amount %20

#10
n10=r_amount//10
r_ammount=amount %10

print("paid the amount:",amount)
print("note of 500:",n500)
print("note of 200:",n200)
print("note of 100:",n100)
print("note of 50:",n50)
print("note of 20:",n20)
print("note of 10:",n10)
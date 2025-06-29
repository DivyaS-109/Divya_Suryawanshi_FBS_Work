#convert distance given in feet and inches into meter and centimeter
feet=int(input("enter the feet: "))
inches=int(input("enter the inches: "))
meter=(feet*0.3048)
centimeter=(inches*2.54)
print("convert feet into meter is:",meter)
print("convert inches into centimeter",centimeter)
#convert the tine in mm hh sec into sec.
hr=int(input("enter the hourse: "))
min=int(input("enter the minutes: "))
sec=int(input("enter the seccond "))
tsec=(hr*3600+min*60+sec)
print("total second is:",tsec)
#wap calculate total salary of employe based on based on basic.
salary=int(input("enter salary of employee: "))
da=salary*0.10
ta=salary*0.12
hr=salary*0.15
print("dearness alounce=",da)
print("travel allounce+",ta)
print("house rent allounce=",hr)
total_amount=salary+da+ta+hr
print("total amount=",total_amount)

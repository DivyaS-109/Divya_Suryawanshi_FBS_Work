##write a program enter the p.t.r  and calculate compond interest.


p=int(input("enter principle"))
t=int(input(" enter thr no.time "))
r=int(input("enter rate of interest "))
n=int(input("enter the no. of time interest "))
a=(p*(1+r/n))**(n*t)
print("compount interest:",a)
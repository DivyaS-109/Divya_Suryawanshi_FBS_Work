#write a program to convert days into year ,week and days.

days=float(input("enter the days :"))
year=days//365
weeks=days//7
days=days%7
print("year:",year )
print("weeks:",weeks)
print("days:",days)
#wap to calculate the celling prise od book besed on cost prise and discount.

costprise=int(input("enter the cost prise "))
discount=int(input("enter the discount:"))
d_amount=((discount/100)*costprise)
selling_prise=(costprise-d_amount)
print("discount amount:",d_amount)
print("selling prise is:",selling_prise)
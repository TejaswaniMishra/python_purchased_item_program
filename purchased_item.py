item1=float(input("Enter the cost of 1st item: "))
i1=int(input("Enter quantity of item 1: "))
item2=float(input("Enter the cost of 2nd item: "))
i2=int(input("Enter quantity of 2nd item: "))
item3=float(input("Enter the cost of 3rd item: "))
i3=int(input("Enter quantity of 3rd item: "))
sum=item1*i1+item2*i2+item3*i3
if (sum> 50*85):
  discount=(10/100)*sum
  total=sum-discount
  print(f"The final cost of the purchased items after discount of rupees {discount:.2f}is : {total:.2f}")
else:
  print(f"The final cost of purchased items is :{sum:.2f}")

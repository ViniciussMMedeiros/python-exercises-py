# Program to get the price of three products and print wich one you will buy, knowing that your decisions is always for the cheaper.

product1 = float(input("Enter the price of the first product: "))
product2 = float(input("Enter the price of the second product: "))
product3 = float(input("Enter the price of the third product: "))

if product1 < product2 and product2 < product3:
  print(product1)
elif product2 < product3:
  print(product2)
else:
  print(product3)
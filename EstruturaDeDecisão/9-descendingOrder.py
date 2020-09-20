# Program to get three numbers and print them in a descending order

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num3 > num2:
  aux = num3
  num3 = num2
  num2 = aux

if num2 > num1:
  aux = num2
  num2 = num1
  num1 = aux

if num3 > num2:
  aux = num3
  num3 = num2
  num2 = aux

print(f"{num1:0.2f}, {num2:0.2f} and {num3:0.2f}")
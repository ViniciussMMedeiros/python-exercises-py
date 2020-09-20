import math

a = float(input("Enter the value of 'a': "))

if a > 0:
  b = float(input("Enter the value of 'b': "))
  c = float(input("Enter the value of 'c': "))

discriminant = math.pow(b, 2) - 4 * a * c
x1 = (-b + math.sqrt(discriminant)) / 2*a
x2 = (-b - math.sqrt(discriminant)) / 2*a

if discriminant < 0:
  print("There are no real roots.")
elif discriminant == 0:
  print("The equation has only one real root: ")
  print(x1)
elif discriminant > 0:
  print("The equation has two real roots: ")
  print(x1)
  print(x2)
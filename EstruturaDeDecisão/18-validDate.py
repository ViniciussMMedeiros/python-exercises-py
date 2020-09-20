print("\t\tProgram to check either if a given date is valid or not")

day = int(input("Enter a day (dd): "))
month = int(input("Enter a month(mm): "))
year = int(input("Enter a year(yyyy): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  if day > 0 and day <= 31 and year > 0:
    print("Valid date.")
  else:
    print("Invalid date.")
elif month == 4 or month == 6 or month == 9 or month == 1:
  if day > 0 and day <= 30 and year > 0:
    print("Valid date.")
  else:
    print("Invalid date.")
elif month == 2:
  if day > 0 and day <= 29 and year > 0:
    print("Valid date.")
  else:
    print("Invalid date.")
else:
  print("Invalid date.")
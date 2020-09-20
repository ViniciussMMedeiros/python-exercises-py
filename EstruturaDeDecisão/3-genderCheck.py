# Program to take a letter and print Female (if the input is F), Male (if the input is M) or Invalid Input otherwise.

genre = input("Enter a letter ('F' for female or 'M' for male): ")

if genre == 'F':
  print("Female")
elif genre == 'M':
  print("Male")
else:
  print("Invalid input")

# Program to get which shift do you study and return a message of Good morning, Good afternoon or Good evening.

shift = input("Which shift do you study ? ('M' = Morning, 'A' = Afternoon, 'E' = Evening) ")

if shift == 'M':
  print("Good morning!")
elif shift == 'A':
  print("Good afternoon!")
elif shift == 'E':
  print("Good evening!")
else:
  print("Error")
# Program to take the hourly wage and the numbers of worked hours in the month, printing the total wage in that month.

hourlyWage = float(input("Enter your hourly wage: "))
hoursWorkedMonth = int(input("Enter how many hours do your work per month: "))

totalWage = hourlyWage * hoursWorkedMonth

print("Your wage, considering the informed data, is: ", totalWage)
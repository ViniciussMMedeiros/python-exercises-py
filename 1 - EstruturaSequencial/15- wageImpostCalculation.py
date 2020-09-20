# Program to get the hourly wage and the number of hours worked in a refered month. Calculates and prints the total wage in that month, considering the discounts.
# income tax = 11%
# inss = 8%
# syndicate = 5%
# print the gross salary, ir, inss, syndicate and net salary.

hourlyWage = float(input("Enter your hourly wage: "))
hoursWorkedMonth = int(input("Enter how many hours did you work this refered month: "))

grossSalary = hourlyWage * hoursWorkedMonth
ir = grossSalary * 0.11
inss = grossSalary * 0.08
syndicate = grossSalary * 0.05
netSalary = grossSalary - ir - inss - syndicate

print("Gross salary: R$", grossSalary)
print("IR (11%): R$", ir)
print("INSS (8%): R$", inss)
print("Syndicate (5%): R$", syndicate)
print("Net salary: R$", netSalary)

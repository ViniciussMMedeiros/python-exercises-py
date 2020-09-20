hourlyWage = float(input("Enter your hourly wage: "))
hoursWorked = int(input("Enter how many hours you worked in the specific month: "))

grossSalary = hourlyWage * hoursWorked

inss = grossSalary * 0.1
fgts = grossSalary * 0.11
syndicate = grossSalary * 0.03

if grossSalary <= 900.00:
  ir = 0
  netSalary = (grossSalary * 0.87)
elif grossSalary > 900.00 and grossSalary <= 1500.00:
  ir = grossSalary * 0.05
  netSalary = (grossSalary * 0.82)
elif grossSalary > 1500.00 and grossSalary <= 2500.00:
  ir = grossSalary * 0.1
  netSalary = (grossSalary * 0.77)
elif grossSalary > 2500.00:
  ir = grossSalary * 0.2
  netSalary = (grossSalary * 0.67)

discounts = ir + inss + grossSalary * 0.03

print("Gross Salary:", grossSalary)
print("IR:", ir)
print("INSS:", inss)
print("FGTS:", fgts)
print("Syndicate:", syndicate)
print("Discounts:", discounts)
print("Net Salary:", netSalary)


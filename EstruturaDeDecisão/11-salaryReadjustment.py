salary = float(input("Enter your salary: "))

if salary <= 280.00:
  adjustedSalary = salary * 1.2
  value = adjustedSalary - salary
  percentage = 20
elif salary > 280.00 and salary < 700.00:
  adjustedSalary = salary * 1.15
  value = adjustedSalary - salary
  percentage = 15
elif salary >= 700.00 and salary < 1500.00:
  adjustedSalary = salary * 1.1
  value = adjustedSalary - salary
  percentage = 10
elif salary >= 1500.00:
  adjustedSalary = salary * 1.05
  value = adjustedSalary - salary
  percentage = 5

print("Salary before readjustment:", salary)
print(f"Percentage applied: {percentage}%")
print("The increased value:", value)
print("Adjusted salary:", adjustedSalary)
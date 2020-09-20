# Program to convert fahrenheit to celsius
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Enter the temperature in Fahrenheit degrees: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"The temperature informed in fahrenheit is equal to {celsius:0.1f} celsius degrees.")
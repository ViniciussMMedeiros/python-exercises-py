# Program to take 2 integers and 1 real number. Calculate and prints:
# the product of twice the first with half the second
# the sum of the triple the first with the third
# the third cubed

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

productTwiceHalf = (num1 * 2) * (num2 / 2)
sumTriple = (num1 * 3) + num3
cubed = num3 ** 3

print('O produto do dobro do primeiro com metade do segundo é: ', productTwiceHalf)
print('A soma do triplo do primeiro com o terceiro é: ', sumTriple)
print(f'O terceiro elevado ao cubo: {cubed:0.2f}')
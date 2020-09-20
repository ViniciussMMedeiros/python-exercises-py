# Program to take the height of a person and print their ideal weight
# (72.7*height) - 58

height = float(input('Enter the height: '))

idealWeight = (72.7*height) - 58

print(f"Your ideal weight is: {idealWeight:0.2f}")
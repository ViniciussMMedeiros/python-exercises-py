# Program to take a person's height and print their ideal weight
# Male: (72.7*h) - 58
# Female: (62.1*h) - 44.7

maleFemale = input('Enter "m" for male and "f" for female: ')
height = float(input('Enter your height: '))

if maleFemale == 'm':
  idealWeight = (72.7 * height) - 58
elif maleFemale == 'f':
  idealWeight = (62.1 * height) - 44.7

print(f'Your ideal weight is: {idealWeight:0.2f}')
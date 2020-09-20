# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Program to take 4 notes and print the average

noteOne = float(input('Enter the first note: '))
noteTwo = float(input('Enter the second note: '))
noteThree = float(input('Enter the third note: '))
noteFour = float(input('Enter the fourth note: '))

average = (noteOne + noteTwo + noteThree + noteFour) / 4

print("The average is: ", average)

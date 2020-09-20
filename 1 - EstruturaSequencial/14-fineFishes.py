# Program to calculate the fine that have to be paid for every kilogram that exceeds the limit of 50kg. For every kg above the limit a fine of R$ 4,00 have
# to be paid. The program will take the weight of the fishes, calculate the excess and print the value of the fine.

weight = float(input("Enter the weight of the fishes: "))

excess = weight - 50

fine = 4.00 * excess

print(f'The total weight of the fishes is {weight} kilograms, being {excess} kilograms above the limit of 50kg permitted. The applied fine will be R$ {fine}.')
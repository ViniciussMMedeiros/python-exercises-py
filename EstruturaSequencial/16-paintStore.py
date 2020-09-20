# Program to get the square metres of an area to be painted. Considering that the paint covers an area of 3 meters per litre and that the paint is sold
# in cans of 18 liters wich cost R$ 80,00.
# Inform to the user the quantity of cans of paint that must be bought and total price.

areaMetres = float(input("Enter how many square metres are in the area to be painted: "))
litres = areaMetres / 3.0
cansOfPaint = litres / 18
value = cansOfPaint * 80.00

print(f"You will have to buy {cansOfPaint:0.2f} cans of paint, wich will cost: R$ {value:0.2f}")
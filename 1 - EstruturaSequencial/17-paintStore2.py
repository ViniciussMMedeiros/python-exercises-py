import math
# Program to get the square metres of an area to be painted. Considering that the paint covers an area of 6 meters per litre and that the paint is sold
# in cans of 18 liters wich cost R$ 80,00 or in cans of 3,6 liters wich cost R& 25,00.
# Inform to the user the quantity of cans of paint that must be bought and total price.
# Situations:
# Only buy cans of 18 litres.
# Only buy cans of 3,6 litres.
# Mix both cans. Add 10% and round the values up. Consider full cans only.

areaMetres = float(input("Enter how many square metres are in the area to be painted: "))
litres = areaMetres / 6.0
bigCanLitre = litres / 18.0
bigCansOfPaint = 0
smallCansOfPaint = 0


if litres >= 18 and (bigCanLitre % 1) <= 0.5:
  bigCansOfPaint = math.ceil(litres / 18)
  value = bigCansOfPaint * 80.00
elif litres >= 18 and litres % 18 > 1:
  bigCansOfPaint = math.ceil(litres / 18)
  smallCansOfPaint = math.ceil((bigCanLitre) / 3.6)
  value = bigCansOfPaint * 80.00 + smallCansOfPaint * 25.00
elif litres < 11.52:
  smallCansOfPaint = math.ceil(litres / 3.6)
  value = smallCansOfPaint * 25.00

print("Big cans of paint (18 litres): ", bigCansOfPaint)
print("Small cans of paint (3,6 litres): ", smallCansOfPaint)
print("Value: ", value)

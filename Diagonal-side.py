import math
a = float(input("Enter the diagonal of square: "))

side = math.sqrt(a*a/2)

print("The area of the suare is", round(side* side,3),"and the perimeter of square is",round( 4* side,3), "with side", round(side,3))
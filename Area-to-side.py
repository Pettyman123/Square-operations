import math
a = float(input("Enter the area of square: "))

if a>0:
    print("The side of the square is", math.sqrt(a))
else:
    print("Area cannot be 0 or negative")
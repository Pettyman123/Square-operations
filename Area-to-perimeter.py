import math
a = float(input("Enter the area of square: "))

if a>0:
    side = math.sqrt(a)
    print("The perimeter of square is", 4*side)
else:
    print("The area cannot br 0 or negative")
import math as m
numberOfSides=int(input())
lengthOfSide=int(input())
Perimeter=numberOfSides*lengthOfSide
Apothem=(lengthOfSide/ (2 * m.tan(m.pi / numberOfSides)))
print(round(Perimeter*Apothem/2))

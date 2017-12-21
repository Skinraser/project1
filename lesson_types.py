import math

# Calculate square of rectangle
# ----------------------------------------------------------------------------------------------------------------------
width = 10
height = 20
rectangle_square = width * height
print("Площадь прямоугольника при высоте %d и ширине %d равна: %d" % (height, width, rectangle_square))

# Calculate hypotenuse
# ----------------------------------------------------------------------------------------------------------------------
Catheter1 = 4
Catheter2 = 4
hypotenuse = math.sqrt(Catheter1**2 + Catheter2**2)
print("Гипотенуза при катете = %d cm. и катете = %d cm. равна : %.2f cm." % (Catheter1, Catheter2, hypotenuse))

# Calculate circle square
# ----------------------------------------------------------------------------------------------------------------------
radius = 10
circle_square = radius**2 * math.pi
print("Площадь круга при радиусе %d см равна %.3f кв.см" % (radius, circle_square))

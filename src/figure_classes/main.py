from src.figure_classes.Circle import Circle
from src.figure_classes.Triangle import Triangle
from src.figure_classes.Square import Square
from src.figure_classes.Rectangle import Rectangle

circle = Circle(7)
triangle = Triangle(6, 7, 6)
square = Square(5)
rectangle = Rectangle(4, 8)

print(circle)
print("------------------------")
print(triangle)
print("------------------------")
print(square)
print("------------------------")
print(rectangle)
print("------------------------")
print("The sum of the {0}'s area and {1}'s area is {2}.".format(triangle.name, square.name, triangle.add_area(square)))


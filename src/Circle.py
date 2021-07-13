from src.Figure import Figure
from math import pi


class Circle(Figure):
	def __init__(self, radius):
		self.name = "Circle"
		self.radius = float(radius)
		self.area = self.get_area()
		self.perimeter = self.get_perimeter()

	def get_perimeter(self):
		return "{0:.2f}".format(2 * pi * self.radius)

	def get_area(self):
		return "{0:.2f}".format(pi * self.radius * self.radius)
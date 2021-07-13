from src.Figure import Figure


class Rectangle(Figure):

	def __init__(self, side_a, side_b):
		self.name = "Rectangle"
		self.side_a = float(side_a)
		self.side_b = float(side_b)
		self.area = self.get_area()
		self.perimeter = self.get_perimeter()

	def get_area(self):
		return "{0:.2f}".format(self.side_a * self.side_b)

	def get_perimeter(self):
		return "{0:.2f}".format(2 * (self.side_a + self.side_b))
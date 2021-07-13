from src.Figure import Figure


class Square(Figure):

	def __init__(self, side):
		self.name = "Square"
		self.side = float(side)
		self.area = self.get_area()
		self.perimeter = self.get_perimeter()

	def get_area(self):
		return "{0:.2f}".format(self.side * self.side)

	def get_perimeter(self):
		return "{0:.2f}".format(self.side * 4)
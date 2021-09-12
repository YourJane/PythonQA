from src.figure_classes.Figure import Figure


class Triangle(Figure):
	def __init__(self, side_a, side_b, side_c):
		self.name = "Triangle"
		self.side_a = float(side_a)
		self.side_b = float(side_b)
		self.side_c = float(side_c)
		self.area = self.get_area()
		self.perimeter = self.get_perimeter()

	def get_perimeter(self):
		return "{0:.2f}".format(self.side_a + self.side_b + self.side_c)

	def get_area(self):
		p = float(self.get_perimeter()) / 2
		s = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
		return "{0:.2f}".format(s)

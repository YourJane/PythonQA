class Figure:

	def __init__(self):
		self.name = "Figure"
		self.area = self.get_area()
		self.perimeter = self.get_perimeter()
		if type(self) == Figure:
			raise Exception("Figure must be subclassed.")

	def get_perimeter(self):
		return "Perimeter for Figure couldn't be defined"

	def get_area(self):
		return "Area for Figure couldn't be defined"

	def __str__(self):
		a = "This is {0}.".format(self.name)
		b = "\nIt's area = {0};\nIt's perimeter = {1}.".format(self.area, self.perimeter)
		return a + b

	def add_area(self, figure):
		if isinstance(figure, Figure):
			return "{0:.2f}".format(float(self.area) + float(figure.area))
		else:
			raise ValueError("Both terms must be geometric figures")
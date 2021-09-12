import pytest
from src.figure_classes.Rectangle import Rectangle
from src.figure_classes.Square import Square
from src.figure_classes.Circle import Circle
from src.figure_classes.Triangle import Triangle


@pytest.fixture(scope="session")
def create_test_objects(request):
	test_circle = Circle(10)
	test_square = Square(9)
	test_rectangle = Rectangle(7, 14)
	test_triangle = Triangle(9, 5, 5)
	return locals()
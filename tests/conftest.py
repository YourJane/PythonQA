import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


@pytest.fixture(scope="session")
def create_test_objects(request):
	test_circle = Circle(10)
	test_square = Square(9)
	test_rectangle = Rectangle(7, 14)
	test_triangle = Triangle(9, 5, 5)
	return locals()
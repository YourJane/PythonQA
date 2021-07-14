import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
from src.Figure import Figure
from . import conftest


def test_instantiate_base_class():
	with pytest.raises(Exception):
		print(Figure())


@pytest.mark.circle
def test_circle_create():
	test_circle_once = Circle(6)
	assert isinstance(test_circle_once, Figure)
	assert test_circle_once.name == "Circle"


@pytest.mark.circle
def test_circle_get_perimeter(create_test_objects):
	assert create_test_objects["test_circle"].perimeter == "62.83"


@pytest.mark.circle
def test_circle_get_area(create_test_objects):
	assert create_test_objects["test_circle"].area == "314.16"


@pytest.mark.circle
def test_circle_radius_value_float():
	with pytest.raises(ValueError):
		return Circle("test")


@pytest.mark.square
def test_square_create():
	test_square_once = Square(4)
	assert isinstance(test_square_once, Figure)
	assert test_square_once.name == "Square"


@pytest.mark.square
def test_square_get_perimeter(create_test_objects):
	assert create_test_objects["test_square"].perimeter == "36.00"


@pytest.mark.square
def test_square_get_area(create_test_objects):
	assert create_test_objects["test_square"].area == "81.00"


@pytest.mark.square
def test_square_side_value_float():
	with pytest.raises(ValueError):
		return Square("test")


@pytest.mark.rectangle
def test_rectangle_create():
	test_rectangle_once = Rectangle(4, 8)
	assert isinstance(test_rectangle_once, Figure)
	assert test_rectangle_once.name == "Rectangle"


@pytest.mark.rectangle
def test_rectangle_get_perimeter(create_test_objects):
	assert create_test_objects["test_rectangle"].perimeter == "42.00"


@pytest.mark.rectangle
def test_rectangle_get_area(create_test_objects):
	assert create_test_objects["test_rectangle"].area == "98.00"


@pytest.mark.rectangle
def test_rectangle_one_side_value_float():
	with pytest.raises(ValueError):
		return Rectangle(6, "test")


@pytest.mark.rectangle
def test_rectangle_zero_sides_value_float():
	with pytest.raises(ValueError):
		return Rectangle("test", "test")


@pytest.mark.triangle
def test_triangle_create():
	test_triangle_once = Triangle(8.00, 8, 8)
	assert isinstance(test_triangle_once, Figure)
	assert test_triangle_once.name == "Triangle"


@pytest.mark.triangle
def test_triangle_get_perimeter(create_test_objects):
	assert create_test_objects["test_triangle"].perimeter == "19.00"


@pytest.mark.triangle
def test_triangle_get_area(create_test_objects):
	assert create_test_objects["test_triangle"].area == "9.81"


@pytest.mark.triangle
def test_triangle_one_side_value_float():
	with pytest.raises(ValueError):
		return Triangle(6, "test", 6.00)


@pytest.mark.triangle
def test_triangle_zero_sides_value_float():
	with pytest.raises(ValueError):
		return Triangle("test", "test", "test")


@pytest.mark.addarea
def test_add_area_method_two_figure(create_test_objects):
	assert create_test_objects["test_triangle"].add_area(create_test_objects["test_circle"]) == "323.97"


@pytest.mark.addarea
def test_add_area_method_two_obj(create_test_objects):
	class Test:
		def __init__(self):
			self.name = "Test"

	with pytest.raises(ValueError):
		create_test_objects["test_square"].add_area(Test())


@pytest.mark.addarea
def test_add_area_method_one_figure(create_test_objects):
	with pytest.raises(ValueError):
		create_test_objects["test_rectangle"].add_area(45)
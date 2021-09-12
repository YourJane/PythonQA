import pytest
from src.figure_classes.Rectangle import Rectangle
from src.figure_classes.Square import Square
from src.figure_classes.Circle import Circle
from src.figure_classes.Triangle import Triangle
from src.figure_classes.Figure import Figure


def test_instantiate_base_class():
	with pytest.raises(Exception):
		print(Figure())


@pytest.mark.circle
def test_circle_create():
	test_circle_once = Circle(6)
	assert isinstance(test_circle_once, Figure), "The instance of the created object should be Figure"
	assert test_circle_once.name == "Circle", "The name of the created figure should be Circle"


@pytest.mark.circle
def test_circle_get_perimeter(create_test_objects):
	assert create_test_objects["test_circle"].perimeter == "62.83", \
		f"Incorrect perimeter value for the tested circle"


@pytest.mark.circle
def test_circle_get_area(create_test_objects):
	assert create_test_objects["test_circle"].area == "314.16", \
		f"Incorrect area value for the tested circle"


@pytest.mark.circle
def test_circle_radius_value_float():
	with pytest.raises(ValueError):
		return Circle("tests")


@pytest.mark.square
def test_square_create():
	test_square_once = Square(4)
	assert isinstance(test_square_once, Figure), "The instance of the created object should be Figure"
	assert test_square_once.name == "Square", "The name of the created figure should be Square"


@pytest.mark.square
def test_square_get_perimeter(create_test_objects):
	assert create_test_objects["test_square"].perimeter == "36.00", \
		f"Incorrect perimeter value for the tested square"


@pytest.mark.square
def test_square_get_area(create_test_objects):
	assert create_test_objects["test_square"].area == "81.00", \
		f"Incorrect area value for the tested square"


@pytest.mark.square
def test_square_side_value_float():
	with pytest.raises(ValueError):
		return Square("tests")


@pytest.mark.rectangle
def test_rectangle_create():
	test_rectangle_once = Rectangle(4, 8)
	assert isinstance(test_rectangle_once, Figure), "The instance of the created object should be Figure"
	assert test_rectangle_once.name == "Rectangle", "The name of the created figure should be Rectangle"


@pytest.mark.rectangle
def test_rectangle_get_perimeter(create_test_objects):
	assert create_test_objects["test_rectangle"].perimeter == "42.00", \
		f"Incorrect perimeter value for the tested rectangle"


@pytest.mark.rectangle
def test_rectangle_get_area(create_test_objects):
	assert create_test_objects["test_rectangle"].area == "98.00", \
		f"Incorrect area value for the tested rectangle"


@pytest.mark.rectangle
def test_rectangle_one_side_value_float():
	with pytest.raises(ValueError):
		return Rectangle(6, "tests")


@pytest.mark.rectangle
def test_rectangle_zero_sides_value_float():
	with pytest.raises(ValueError):
		return Rectangle("tests", "tests")


@pytest.mark.triangle
def test_triangle_create():
	test_triangle_once = Triangle(8.00, 8, 8)
	assert isinstance(test_triangle_once, Figure), "The instance of the created object should be Figure"
	assert test_triangle_once.name == "Triangle", "The name of the created figure should be Triangle"


@pytest.mark.triangle
def test_triangle_get_perimeter(create_test_objects):
	assert create_test_objects["test_triangle"].perimeter == "19.00", \
		f"Incorrect perimeter value for the tested triangle"


@pytest.mark.triangle
def test_triangle_get_area(create_test_objects):
	assert create_test_objects["test_triangle"].area == "9.81", \
		f"Incorrect area value for the tested triangle"


@pytest.mark.triangle
def test_triangle_one_side_value_float():
	with pytest.raises(ValueError):
		return Triangle(6, "tests", 6.00)


@pytest.mark.triangle
def test_triangle_zero_sides_value_float():
	with pytest.raises(ValueError):
		return Triangle("tests", "tests", "tests")


@pytest.mark.addarea
def test_add_area_method_two_figure(create_test_objects):
	assert create_test_objects["test_triangle"].add_area(create_test_objects["test_circle"]) == "323.97", \
		"Incorrect sum value of the tested triangle and circle"


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

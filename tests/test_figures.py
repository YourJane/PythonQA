import pytest
# from src.Rectangle import Rectangle
# from src.Square import Square
# from src.Circle import Circle
# from src.Triangle import Triangle
from src.Figure import Figure


# @pytest.fixture(scope="session")
# def create_test_objects():

def test_instantiate_base_class():
	with pytest.raises(Exception):
		print(Figure())

def test_create_circle():


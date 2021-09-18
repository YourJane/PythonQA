import pytest

from examples_from_lectures.api_testing_ddt.test_data.test_data import auth_endpoints


@pytest.mark.parametrize("data", auth_endpoints)
def test_with_generator(data):
    print(data)
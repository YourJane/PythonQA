import time
import pytest


# @pytest.fixture
# def something():
#     return something_else()

@pytest.fixture(scope="session", autouse=True)
def setup_environment(request):
    time.sleep(1)
    print("building app")

    def final():
        print("de-building app")

    request.addfinalizer(final)

# @pytest.fixture(scope="function")  #default


def division(a, b):
    # raise Exception
    return a / b


def test_division():
    assert division(0, 5) == 5


def test_division_1():
    with pytest.raises(ZeroDivisionError):
        division(0, 0)
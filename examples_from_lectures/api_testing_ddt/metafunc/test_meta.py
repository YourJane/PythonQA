# https://docs.pytest.org/en/stable/parametrize.html#parametrize-basics
# Should pass --input as param to pytest

# def test_valid_string(inp):
#     assert inp.isalpha(), "Contains not only letters"
#
#
# def test_upper_string(inp):
#     assert inp.isupper(), "Not upper case string"


def test_compute(limited_param, inp):
    assert limited_param < 4
    assert inp.isalpha()
import pytest
import requests
from conftest import get_breweries_by
from conftest import base_url_var

BREWERY_CITY = get_breweries_by(base_url_var, "city")


@pytest.mark.parametrize("brewery_city", BREWERY_CITY)
def test_filter_breweries_by_city(brewery_city, base_url):
    target = requests.get(f"{base_url}?by_city={brewery_city}")
    breweries_cities = get_breweries_by(f"{base_url}?by_city={brewery_city}", "city")

    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    for city in breweries_cities:
        assert brewery_city in city, f"The city should be {brewery_city}"


def test_display_breweries_per_page_default(base_url):
    target = requests.get(base_url + "?per_page")
    actual_amount = 0
    for brewery in target.json(): actual_amount += 1
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    assert actual_amount == 20, "The default amount of breweries per page should be 20"


@pytest.mark.parametrize("per_page, expected", [(0, 0), (1, 1), (25, 25), (50, 50), (51, 50)])
def test_display_breweries_per_page(base_url, per_page, expected):
    target = requests.get(base_url + f"?per_page={per_page}")
    actual_amount = 0
    for brewery in target.json(): actual_amount += 1
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    assert actual_amount == expected, f"The amount of breweries per page should be {expected}"


@pytest.mark.parametrize("query", ["maryland", "territor"])
def test_search_breweries(base_url, query):
    target = requests.get(base_url + f"/search?query={query}")
    for brewery in target.json():
        brewery_values = ""
        for value in brewery.values():
            brewery_values += str(value).lower() + " "

        assert query in brewery_values, f"Only the brewery that contain {query} should be in the list"


@pytest.mark.parametrize("query", ["Dog", "Almanac"])
def test_breweries_autocomplete(base_url, query):
    target = requests.get(base_url + f"/autocomplete?query={query}")
    brewery_name_list = []
    for brewery in target.json():
        brewery_name_list.append(brewery.get("name"))

    for name in brewery_name_list:
        assert query in name, f"The name of the brewery should contain {query}"


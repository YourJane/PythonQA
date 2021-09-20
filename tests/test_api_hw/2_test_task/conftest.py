import pytest
import requests
import re

base_url_var = "https://api.openbrewerydb.org/breweries"


@pytest.fixture
def base_url():
    return base_url_var


""" get_breweries_by function can be used to test filter by city, name, state, brewery_type"""


def get_breweries_by(url, key):
    response_json = requests.get(url).json()
    brewery_filtered_list = []

    for brewery in response_json:
        brewery_filter = brewery.get(key)
        if brewery_filter not in brewery_filtered_list:
            if "-" in brewery_filter or " " in brewery_filter:
                brewery_filter_f = re.sub('-| ', "_", brewery_filter)
                brewery_filtered_list.append(brewery_filter_f.lower())
            else:
                brewery_filtered_list.append(brewery_filter.lower())
        else:
            continue

    return brewery_filtered_list



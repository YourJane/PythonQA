import pytest
import requests
from jsonschema import validate
import re


def test_breeds_list(base_url):
    target = requests.get(base_url+"list/all")

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    validate(instance=target.json(), schema=schema)


def test_random_image(base_url, get_all_breeds_list):
    target = requests.get(base_url+"image/random")
    response = target.json()
    response_url = response["message"].split("/")
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    assert response_url[-2] in get_all_breeds_list, f"There is no {response_url[-2]} in the breeds list"


@pytest.mark.parametrize("breed_index", [1, 2, 3, 4])
def test_breed_images(breed_index, get_all_breeds_list, base_url_breed):
    target = requests.get(base_url_breed + get_all_breeds_list[breed_index] + "/images")
    response = target.json()
    breed_in_urls = []
    for url in response['message']:
        url_i = url.split("/")
        if url_i[-2] not in breed_in_urls:
            breed_in_urls.append(url_i[-2])
        else:
            continue

    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    assert len(breed_in_urls) == 1, "Should be only one breed in the list"
    assert breed_in_urls[0] == get_all_breeds_list[breed_index], \
        f"The breed should be {get_all_breeds_list[breed_index]}"


@pytest.mark.parametrize("selected_amount, expected_amount",
                         [
                             (0, 1),
                             (1, 1),
                             (25, 25),
                             (50, 50),
                             (51, 50)
                         ])
def test_count_displayed_images(selected_amount, expected_amount, base_url):
    target = requests.get(base_url + "image/random/" + f"{selected_amount}")
    response = target.json()
    images = []
    for url in response['message']:
        images.append(url)
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    assert len(images) == expected_amount, \
        f"The expected length is {expected_amount}. The actual is {len(images)}"


def test_browse_breed_list(base_url_breed, get_all_master_breed_list, get_all_sub_breed_list, get_master_and_sub_breed):
    if len(get_master_and_sub_breed[1]) > 0:
        target = \
            requests.get(
                base_url_breed + get_master_and_sub_breed[0] + f"/{get_master_and_sub_breed[1]}" + "/images/random/")
    else:
        target = requests.get(base_url_breed + get_master_and_sub_breed[0] + "/images/random/")
    response = target.json()
    response_url = re.split('/|-', response["message"])

    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    if len(get_master_and_sub_breed[1]) > 0:
        assert response_url[-3] in get_all_master_breed_list, f"There is no {response_url[-3]} in the breeds list"
        assert response_url[-2] in get_all_sub_breed_list, f"There is no {response_url[-2]} in the breeds list"
    else:
        assert response_url[-2] in get_all_master_breed_list, f"There is no {response_url[-2]} in the breeds list"

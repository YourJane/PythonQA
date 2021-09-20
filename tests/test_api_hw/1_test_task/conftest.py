import pytest
import requests
import random


@pytest.fixture
def base_url_breeds():
    return "https://dog.ceo/api/breeds/"


@pytest.fixture
def base_url_breed():
    return "https://dog.ceo/api/breed/"


def get_breeds_list():
    target = requests.get("https://dog.ceo/api/breeds/list/all").json()
    full_breeds_list = []
    master_breeds_list = []
    sub_breeds_list = []

    for key, value in list(target["message"].items()):
        full_breeds_list.append(key)
        master_breeds_list.append(key)
        if len(value) > 0:
            for i in value:
                full_breeds_list.append(i)
                sub_breeds_list.append(i)
        else:
            continue

    return full_breeds_list, master_breeds_list, sub_breeds_list


@pytest.fixture
def get_all_breeds_list():
    full_breeds_list = get_breeds_list()
    return full_breeds_list[0]


@pytest.fixture
def get_all_master_breed_list():
    master_breeds_list = get_breeds_list()
    return master_breeds_list[1]


@pytest.fixture
def get_all_sub_breed_list():
    sub_breeds_list = get_breeds_list()
    return sub_breeds_list[2]


@pytest.fixture
def get_random_index():
    breeds_list = get_breeds_list()
    return random.randint(0, len(breeds_list[1])-1)


def get_breeds_dict():
    target = requests.get("https://dog.ceo/api/breeds/list/all").json()
    breeds_dict = {}
    for key, value in list(target["message"].items()):
        breeds_dict[key] = value

    return breeds_dict


def get_random_breed():
    breeds_dict = get_breeds_dict()
    keys = breeds_dict.keys()
    number = random.randint(0, len(keys) - 1)
    i = 0
    selected_key = ""
    while i != number:
        for key in keys:
            if i == number:
                selected_key = key
                break
            i += 1

    selected_value = ""

    if len(breeds_dict[selected_key]) > 1:
        index = random.randint(0, len(breeds_dict[selected_key])-1)
        ind = -1
        while ind != index:
            ind += 1
            for value in breeds_dict[selected_key]:
                if ind == index:
                    selected_value = value
                    break
                ind += 1
    else:
        for value in breeds_dict[selected_key]:
            selected_value = value

    return selected_key, selected_value


@pytest.fixture
def get_master_and_sub_breed():
    return get_random_breed()

import pytest
import requests


def test_create_resource(base_url):
    target = requests.post(base_url + "posts",
                           data={
                               "title": "test",
                               "body": "test test",
                               "userId": 111

    })
    assert target.status_code == 201, f"Status code is {target.status_code}, expected 201"
    assert target.json()["title"] == "test", "The title of the created resource should be 'test'"
    assert target.json()["body"] == "test test", "The body of the created resource should be 'test test'"
    assert target.json()["userId"] == "111", "The userId of the created resource should be '111'"
    assert type(target.json()["id"]) == int, "The id should be added to the created resource," \
                                             "and it's value should be int"


def test_update_resource(base_url):
    target = requests.put(base_url + "posts/1", data={
        "userId": 23
    })
    assert target.json()["userId"] == "23", "Expected the new value for the userId to be '23'"


def test_delete_resource(base_url):
    target = requests.delete(base_url + "posts/1")

    assert target.json() == {}, "Expected json to be empty"


@pytest.mark.parametrize("user_id", ["1", "2", "3", "4"])
def test_filter_by_user_id(base_url, user_id):
    target = requests.get(base_url + f"posts?userId={user_id}")

    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    for post in target.json():
        assert post["userId"] == int(user_id), f"Expected post to be made by user with userId = '{user_id}'"


@pytest.mark.parametrize("post_id", ["1", "2", "3", "4"])
def test_listing_nested_resources(base_url, post_id):
    target = requests.get(base_url + f"posts/{post_id}/comments")
    assert target.status_code == 200, f"Status code is {target.status_code}, expected 200"
    for post in target.json():
        assert post["postId"] == int(post_id), f"Expected to see comments posted under post with posyId = '{post_id}'"



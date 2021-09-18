import pytest
import requests


def test_url_status(url, status_code):
    target = requests.get(url)
    assert target.status_code == int(status_code), f"Status code should be {status_code}"

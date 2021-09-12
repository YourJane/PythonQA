import pytest
import requests

AUTH_DATA = {"login": "admin", "password": "admin"}


def pytest_addoption(parser):
    parser.addoption("--url", default="https://my-api-examaple.herokuapp.com/api", help="Url for tests api location")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def session(base_url):
    _session = requests.Session()
    _session.request("login", base_url + "/auth/login", json=AUTH_DATA)
    return _session

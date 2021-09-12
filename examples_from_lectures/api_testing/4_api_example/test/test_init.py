import pytest

# WARNING Bad Example: (Never use sensitive data like this!)
# See: https://www.youtube.com/watch?v=L9-I4NibguY


@pytest.mark.skip(reason="Нужно сначала аройти авторизацию")
def test_init_database(base_url, session):
    response = session.request("create", "{}/create/init".format(base_url))
    try:
        assert response.json().get("status") == "created"
    except AssertionError:
        raise AssertionError(response.json())


@pytest.mark.skip(reason="Нужно сначала аройти авторизацию")
def test_reinit_database(base_url, session):
    response = session.request("recreate", "{}/create/reinit".format(base_url))
    try:
        assert response.json().get("status") == "table dropped and created"
    except AssertionError:
        raise AssertionError(response.json())
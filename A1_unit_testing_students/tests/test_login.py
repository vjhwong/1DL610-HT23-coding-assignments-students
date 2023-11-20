from ..login import login
import pytest

#@pytest.fixture
#def login_stub1(mocker):
#    return mocker.patch('login.input', return_value="name")
def test_int_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mark")

    result = login()

    print(result)


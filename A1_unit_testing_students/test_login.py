import os
from login import login
import pytest
import shutil


@pytest.fixture
def copy_json_file():
    # Set up
    shutil.copy('users.json', 'copy_users.json')
    yield
    # Teardown
    os.remove('copy_users.json')

def test_add_new_user(monkeypatch, copy_json_file):
    responses = iter(["Mark", "nopass", "yes", "1234567Q#"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == {'username': 'Mark', 'password': 'nopass', 'wallet': 0}

def test_login(monkeypatch, copy_json_file):
    responses = iter(["Ramanathan", "Notaproblem23*"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Ramanathan', 'wallet': 100}

def test_login_int(monkeypatch):
    responses = iter([4, 4, 4])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == None

def test_login_float(monkeypatch):
    responses = iter([4.2, 4.2, 4.2])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == None

def test_login_list(monkeypatch):
    responses = iter([[], [], []])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == None

def test_login_list(monkeypatch):
    responses = iter(["a"*(10**10), ["a"*(10**10)], ["a"*(10**10)]])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == None
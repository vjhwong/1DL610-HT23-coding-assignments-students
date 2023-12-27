import os
import shutil

import pytest

from login import login


@pytest.fixture(scope="module")
def copy_json_file():
    # Set up
    os.chdir("tests")
    shutil.copy('../users.json', 'users.json')

    yield

    # Teardown
    os.remove('users.json')
    os.chdir("..")

# test 1
def test_add_new_user1(copy_json_file, monkeypatch):
    responses = iter(["Mark", "nopass", "yes", "1234567Q#"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result == {'username': 'Mark', 'password': '1234567Q#', 'wallet': 0}

# test 2
def test_login1(monkeypatch, copy_json_file):
    responses = iter(["Ramanathan", "Notaproblem23*"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Ramanathan', 'wallet': 100}

# test 3
def test_login2(monkeypatch, copy_json_file):
    responses = iter(["Samantha", "SecurePass123/^"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Samantha', 'wallet': 150}

# test 4
def test_login3(monkeypatch, copy_json_file):
    responses = iter(["Maximus", "StrongPwd!23"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Maximus', 'wallet': 75}

#test 5
def test_login4(monkeypatch, copy_json_file):
    responses = iter(["Lily", "Bloom.,ing456"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Lily', 'wallet': 100}

#test 6
def test_login5(monkeypatch, copy_json_file):
    responses = iter(["Sunny", "BrightDa%#$y456"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Sunny', 'wallet': 120}

#test 7
def test_login6(monkeypatch, copy_json_file):
    responses = iter(["Shadow", "Steal#$%thyCat789"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    assert result == {'username': 'Shadow', 'wallet': 80}

# test 8
def test_add_new_user2(monkeypatch, copy_json_file):
    responses = iter(["Mark", "nopass1", "no"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None

# test 9
def test_add_new_user3(monkeypatch, copy_json_file):
    responses = iter(["Mark", "nopass1", "yes", "pass"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None

# test 10
def test_add_new_user4(monkeypatch, copy_json_file):
    responses = iter(["Mark", "nopass1", "yes", "nopass111"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None




# Invalid test 1
def test_login_int(monkeypatch):
    responses = iter([4, 4, 4])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None

# Invalid test 2
def test_login_float(monkeypatch):
    responses = iter([4.2, 4.2, 4.2])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None

# Invalid test 3
def test_login_list(monkeypatch):
    responses = iter([[], [], []])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()
    assert result is None


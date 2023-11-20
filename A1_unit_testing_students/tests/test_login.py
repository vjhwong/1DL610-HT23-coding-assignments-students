import os
from ..login import login
import pytest
import shutil


@pytest.fixture
def copy_json_file():
    # Set up
    shutil.copy('users.json', 'copy_users.json')
    yield
    # Teardown
    os.remove('copy_users.json')

def test_int_input(monkeypatch, copy_json_file):
    responses = iter(["Mark", "nopass", "yes", "1234567Q#"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = login()

    print(result)


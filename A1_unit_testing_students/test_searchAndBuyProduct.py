# from unittest.mock import DEFAULT

from products import *
import pytest
import os
import shutil
from unittest.mock import call

@pytest.fixture(scope="session")
def copy_csv_file():
    # Set up
    os.chdir("tests")
    shutil.copy('../products.csv', 'products.csv')
    # cwd = os.getcwd()
    # print(cwd)

    yield
    # Teardown
    os.remove('products.csv')

@pytest.fixture
def login_stub(mocker):
    return mocker.patch('products.login', return_value='login')



@pytest.fixture
def display_csv_as_table_stub(mocker):
    return mocker.patch('products.display_csv_as_table', return_value='csv_as_table')


@pytest.fixture
def display_filtered_table_stub(mocker):
    return mocker.patch('products.display_filtered_table', return_value='filtered_table')

# return mocker.patch('products.display_filtered_table', side_effect=side_effect,return_value='filtered_table')
# def side_effect(*args, **kwargs):
#    print("test")
#    return DEFAULT

@pytest.fixture
def checkoutAndPayment_stub(mocker):
    return mocker.patch('products.checkoutAndPayment', return_value='')


@pytest.fixture
def dummy_csv_file(tmp_path):
    # Create a CSV file without a header
    csv_filename = tmp_path / 'dummy.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['Apple', 1.0, 10])
        csv_writer.writerow(['Banana', 0.5, 20])
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename

"""
def test_1_assert_login_call(login_stub, mocker):
    result = searchAndBuyProduct()
    login_stub.assert_called_once()
"""


def test_1_all(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, dummy_csv_file, mocker, monkeypatch):
    responses = iter(["all", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once_with("products.csv")
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_2_all_uppercase(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, dummy_csv_file, mocker, monkeypatch):
    responses = iter(["ALL", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once_with("products.csv")
    checkoutAndPayment_stub.assert_called_once_with("login")

"""
def test_3_(login_stub, display_csv_as_table_stub, mocker, monkeypatch):
    result = searchAndBuyProduct()
    login_stub.assert_called_once_with()
"""

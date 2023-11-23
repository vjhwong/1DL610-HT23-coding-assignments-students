# from unittest.mock import DEFAULT

from products import *
import pytest
import os
import shutil
from unittest.mock import call

@pytest.fixture(scope="module")
def copy_csv_file():
    # Set up
    os.chdir("tests")
    shutil.copy('../products.csv', 'products.csv')

    yield

    # Teardown
    os.remove('products.csv')
    os.chdir("..")

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

def test_1_all(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["all", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once_with("products.csv")
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_2_all_uppercase(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["ALL", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once_with("products.csv")
    checkoutAndPayment_stub.assert_called_once_with("login")


def test_3_single(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_filtered_table_stub.assert_called_once_with("products.csv", "Apple")
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_4_pair(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple, Banana", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_filtered_table_stub.assert_called_once_with("products.csv", "Apple, Banana")
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_5_single_bad(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["no", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    display_filtered_table_stub.assert_called_once_with("products.csv", "no")
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_6_single_two_calls(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple", "n", "Milk", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_filtered_table_stub.call_count == 2
    display_filtered_table_stub.assert_has_calls([call('products.csv', 'Apple'), call('products.csv', 'Milk')])
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_7_pair_two_calls(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple, Banana", "n", "Milk", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_filtered_table_stub.call_count == 2
    display_filtered_table_stub.assert_has_calls([call('products.csv', 'Apple, Banana'), call('products.csv', 'Milk')])
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_8_pair_single_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple, Banana", "n", "all", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_filtered_table_stub.call_count == 1
    display_filtered_table_stub.assert_called_once_with('products.csv', 'Apple, Banana')
    assert display_csv_as_table_stub.call_count == 1
    display_csv_as_table_stub.assert_called_once_with('products.csv')
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_9_pair_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["all", "n", "aLl", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_csv_as_table_stub.call_count == 2
    display_csv_as_table_stub.assert_has_calls([call('products.csv'), call('products.csv')])
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_10_many_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["all", "n", "all", "n", "all", "n", "all", "n", "all", "n", "all", "n", "all", "n", "all", "n", "all", "n", "aLl", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_csv_as_table_stub.call_count == 10
    display_csv_as_table_stub.assert_has_calls([call('products.csv')])
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_11_single_many_calls(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    responses = iter(["Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "n", "Apple", "y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))

    result = searchAndBuyProduct()

    login_stub.assert_called_once()
    assert display_filtered_table_stub.call_count == 10
    display_filtered_table_stub.assert_has_calls([call('products.csv', 'Apple')])
    checkoutAndPayment_stub.assert_called_once_with("login")

def test_1_invalid_int(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    with pytest.raises(AttributeError):
        responses = iter([1, "y"])
        monkeypatch.setattr("builtins.input", lambda msg: next(responses))

        result = searchAndBuyProduct()

def test_2_invalid_float(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    with pytest.raises(AttributeError):
        responses = iter([1.1, "y"])
        monkeypatch.setattr("builtins.input", lambda msg: next(responses))

        result = searchAndBuyProduct()

def test_3_invalid_list(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    with pytest.raises(AttributeError):
        responses = iter([[], "y"])
        monkeypatch.setattr("builtins.input", lambda msg: next(responses))

        result = searchAndBuyProduct()
from products import *
import pytest


@pytest.fixture
def login_stub(mocker):
    return mocker.patch('products.login', return_value=None)


@pytest.fixture
def display_csv_as_table_stub(mocker):
    return mocker.patch('products.display_csv_as_table', return_value='csv_as_table')


@pytest.fixture
def display_filtered_table_stub(mocker):
    return mocker.patch('products.display_filtered_table', return_value='filtered_table')


@pytest.fixture
def checkoutAndPayment_stub(mocker):
    return mocker.patch('checkout_and_payment.checkoutAndPayment', return_value='')

"""
def test_1_assert_login_call(login_stub, mocker):
    result = searchAndBuyProduct()
    login_stub.assert_called_once()
"""


def test_2_(login_stub, display_csv_as_table_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    result = searchAndBuyProduct()
    responses = iter(["all,y,y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once()

"""
def test_3_(login_stub, display_csv_as_table_stub, mocker, monkeypatch):
    result = searchAndBuyProduct()
    login_stub.assert_called_once_with()
"""

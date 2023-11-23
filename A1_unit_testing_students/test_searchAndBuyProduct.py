from products import *
import pytest


@pytest.fixture
def login_stub(mocker):
    return mocker.patch('login.login', return_value='login')


@pytest.fixture
def display_csv_as_table_stub(mocker):
    return mocker.patch('products.display_csv_as_table', return_value='csv_as_table')


@pytest.fixture
def display_filtered_table_stub(mocker):
    return mocker.patch('products.display_filtered_table', return_value='filtered_table')


@pytest.fixture
def checkoutAndPayment_stub(mocker):
    return mocker.patch('checkout_and_payment.checkoutAndPayment', return_value='')


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


def test_2_(login_stub, display_csv_as_table_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    result = searchAndBuyProduct()
    responses = iter(["all,y,y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    login_stub.assert_called_once()
    display_csv_as_table_stub.assert_called_once()
    checkoutAndPayment_stub.assert_called_once()

"""
def test_3_(login_stub, display_csv_as_table_stub, mocker, monkeypatch):
    result = searchAndBuyProduct()
    login_stub.assert_called_once_with()
"""

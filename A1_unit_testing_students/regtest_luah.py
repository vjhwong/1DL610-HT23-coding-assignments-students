import os
import shutil

import pytest

import test_display_csv_as_table
import test_display_filtered_table
import test_login
import test_logout
import test_searchAndBuyProduct
from checkout_and_payment import *


@pytest.fixture #(scope="module")
def copy_json_file():
    # Set up
    os.chdir("tests")
    shutil.copy('../users.json', 'users.json')

    yield

    # Teardown
    os.remove('users.json')
    os.chdir("..")

@pytest.fixture #(scope="module")
def copy_csv_file():
    # Set up
    os.chdir("tests")
    shutil.copy('../products.csv', 'products.csv')

    yield

    # Teardown
    os.remove('products.csv')
    os.chdir("..")

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def non_empty_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Product("Product1", 10.0, 2))
    shopping_cart.add_item(Product("Product2", 20.0, 1))
    return shopping_cart

@pytest.fixture
def empty_csv_file(tmp_path):
    # Create an empty CSV file
    csv_filename = tmp_path / 'empty.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([])
    return csv_filename


@pytest.fixture
def header_only_csv_file(tmp_path):
    # Create a CSV file with only a header
    csv_filename = tmp_path / 'header_only.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product', 'Price', 'Units'])
    return csv_filename

@pytest.fixture
def csv_file_without_header(tmp_path):
    # Create a CSV file without a header
    csv_filename = tmp_path / 'no_header.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Apple', 1.0, 10])
        csv_writer.writerow(['Banana', 0.5, 20])
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename

@pytest.fixture
def different_delimiter_csv_file(tmp_path):
    # Create a CSV file with ; as delimiter
    csv_filename = tmp_path / 'different_delimiter.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')  # Set the delimiter to semicolon
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['Apple', 1.0, 10])
        csv_writer.writerow(['Banana', 0.5, 20])
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename

@pytest.fixture
def login_stub(mocker):
    return mocker.patch('products.login', return_value='login')

@pytest.fixture
def display_csv_as_table_stub(mocker):
    return mocker.patch('products.display_csv_as_table', return_value='csv_as_table')

@pytest.fixture
def display_filtered_table_stub(mocker):
    return mocker.patch('products.display_filtered_table', return_value='filtered_table')

@pytest.fixture
def checkoutAndPayment_stub(mocker):
    return mocker.patch('products.checkoutAndPayment', return_value='')

@pytest.fixture
def logout_stub(mocker):
    return mocker.patch('checkout_and_payment.logout', return_value=True)

## LOGIN
def test_login_1(copy_json_file, monkeypatch):
    test_login.test_add_new_user1(copy_json_file, monkeypatch)

def test_login_2(copy_json_file, monkeypatch):
    test_login.test_login1(monkeypatch, copy_json_file)

def test_login_3(copy_json_file, monkeypatch):
    test_login.test_login2(monkeypatch, copy_json_file)

def test_login_4(copy_json_file, monkeypatch):
    test_login.test_login3(monkeypatch, copy_json_file)

def test_login_5(copy_json_file, monkeypatch):
    test_login.test_login4(monkeypatch, copy_json_file)

## LOGOUT
def test_logout_1(copy_csv_file, empty_cart):
    test_logout.test_1_empty_cart(copy_csv_file, empty_cart)

def test_logout_2(monkeypatch, copy_csv_file, non_empty_cart):
    test_logout.test_2_logout_confirm(monkeypatch, copy_csv_file, non_empty_cart)

def test_logout_3(monkeypatch, copy_csv_file, non_empty_cart):
    test_logout.test_3_logout_deny(monkeypatch, copy_csv_file, non_empty_cart)

def test_logout_4(monkeypatch, copy_csv_file, non_empty_cart):
    test_logout.test_4_logout_confirm_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart)

def test_logout_5(monkeypatch, copy_csv_file, non_empty_cart):
    test_logout.test_5_logout_deny_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart)

## DIPLAY_CSV_AS_TABLE

def test_display_csv_as_table_1():
    test_display_csv_as_table.test_1_display_file_not_found()

def test_display_csv_as_table_2(empty_csv_file, capsys):
    test_display_csv_as_table.test_2_display_empty_csv_file(empty_csv_file, capsys)

def test_display_csv_as_table_3(header_only_csv_file, capsys):
    test_display_csv_as_table.test_3_display_csv_header_only_file(header_only_csv_file, capsys)

def test_display_csv_as_table_4(csv_file_without_header, capsys):
    test_display_csv_as_table.test_4_display_csv_without_header(csv_file_without_header, capsys)

def test_display_csv_as_table_5(different_delimiter_csv_file, capsys):
    test_display_csv_as_table.test_5_display_csv_different_delimiters(different_delimiter_csv_file, capsys)

## DISPLAY_FILTERED_TABLE

def test_display_filtered_table_1(copy_csv_file, capsys):
    test_display_filtered_table.test_1(copy_csv_file, capsys)

def test_display_filtered_table_2(copy_csv_file, capsys):
    test_display_filtered_table.test_2(copy_csv_file, capsys)

def test_display_filtered_table_3(copy_csv_file, capsys):
    test_display_filtered_table.test_3(copy_csv_file, capsys)

def test_display_filtered_table_4(empty_csv_file, capsys):
    test_display_filtered_table.test_4_empty_csv(empty_csv_file, capsys)

def test_display_filtered_table_5():
    test_display_filtered_table.test_5_file_not_found_csv()

## SEARCHANDBUYPRODUCT

def test_searchAndBuyProduct_1(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_1_all(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)

def test_searchAndBuyProduct_2(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_2_all_uppercase(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)

def test_searchAndBuyProduct_3(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_3_single(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)

def test_searchAndBuyProduct_4(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_4_pair(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)

def test_searchAndBuyProduct_5(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_5_single_bad(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)

## test for new implementation

def test_regtest_1(login_stub, monkeypatch, capsys, logout_stub):
    responses = iter(["2", "c", "n", "r", "2", "l", "y"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = checkoutAndPayment(login_stub)
    captured = capsys.readouterr()
    assert "Banana added to your cart." in captured.out
    assert "['Banana', 1.0, 15]" in captured.out
    assert "Banana removed from your cart." in captured.out
    assert "You have been logged out" in captured.out

def test_regtest_2(login_stub, monkeypatch, capsys, logout_stub):
    user = {"username": "user",
            "wallet": 1000}
    responses = iter(["2", "c", "n", "r", "2", "2", "c", "y", "l", "y"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = checkoutAndPayment(user)
    captured = capsys.readouterr()
    assert "Banana added to your cart." in captured.out
    assert "['Banana', 1.0, 15]" in captured.out
    assert "Banana removed from your cart." in captured.out
    assert "Thank you for your purchase, user! Your remaining balance is 999.0" in captured.out
    assert "You have been logged out" in captured.out

def test_regtest_3(login_stub, monkeypatch, capsys, logout_stub):
    user = {"username": "user",
            "wallet": 1000}
    responses = iter(["r", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = checkoutAndPayment(user)
    captured = capsys.readouterr()
    assert "There are no items in the cart to remove" in captured.out
    assert "You have been logged out" in captured.out
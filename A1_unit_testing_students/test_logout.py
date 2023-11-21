import builtins

import pytest
from A1_unit_testing_students.logout import logout

from checkout_and_payment import *
import shutil
import os


@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def one_item_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Product("Product1", 10.0, 2))
    return shopping_cart


@pytest.fixture
def non_empty_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Product("Product1", 10.0, 2))
    shopping_cart.add_item(Product("Product2", 20.0, 1))
    return shopping_cart


@pytest.fixture
def many_items_cart():
    shopping_cart = ShoppingCart()
    for i in range(1, 11):
        product_name = f"Product{i}"
        product_price = i*10.0
        product_quantity = i
        shopping_cart.add_item(Product(product_name, product_price, product_quantity))
    return shopping_cart


@pytest.fixture
def copy_csv_file():
    # Set up
    shutil.copy('products.csv', 'copy_products.csv')
    yield
    # Teardown
    os.remove('copy_products.csv')


# Test 1
def test_empty_cart(copy_csv_file, empty_cart):
    result = logout(empty_cart)
    assert result is True


# Test 2
def test_logout_confirm(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert non_empty_cart.items == []
    assert result is True


# Test 3
def test_logout_deny(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["N"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


# Test 4
def test_logout_confirm_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert non_empty_cart.items == []
    assert result is True


# Test 5
def test_logout_deny_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


# Test 6
def test_logout_single_item_confirm(monkeypatch, copy_csv_file, one_item_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(one_item_cart)
    assert one_item_cart.items == []
    assert result is True


# Test 7
def test_logout_single_item_deny(monkeypatch, copy_csv_file, one_item_cart):
    responses = iter(["N"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(one_item_cart)
    assert result is False


# Test 8
def test_logout_random_confirmation(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["x"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


# Test 9
def test_logout_many_items_confirm(monkeypatch, copy_csv_file, many_items_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(many_items_cart)
    assert many_items_cart.items == []
    assert result is True


# Test 10
def test_logout_many_items_deny(monkeypatch, copy_csv_file, many_items_cart):
    responses = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(many_items_cart)
    assert result is False

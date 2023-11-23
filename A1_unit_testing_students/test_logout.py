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
def int_item_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.items = 0
    return shopping_cart


@pytest.fixture
def str_item_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.items = " "
    return shopping_cart


@pytest.fixture
def float_item_cart():
    shopping_cart = ShoppingCart()
    shopping_cart.items = 1.1
    return shopping_cart


@pytest.fixture
def copy_csv_file():
    # Set up
    shutil.copy('products.csv', 'copy_products.csv')
    yield
    # Teardown
    os.remove('copy_products.csv')


def test_1_empty_cart(copy_csv_file, empty_cart):
    result = logout(empty_cart)
    assert result is True


def test_2_logout_confirm(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert non_empty_cart.items == []
    assert result is True


def test_3_logout_deny(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["N"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


def test_4_logout_confirm_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert non_empty_cart.items == []
    assert result is True


def test_5_logout_deny_case_insensitive(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


def test_6_logout_single_item_confirm(monkeypatch, copy_csv_file, one_item_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(one_item_cart)
    assert one_item_cart.items == []
    assert result is True


def test_7_logout_single_item_deny(monkeypatch, copy_csv_file, one_item_cart):
    responses = iter(["N"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(one_item_cart)
    assert result is False


def test_8_logout_random_confirmation(monkeypatch, copy_csv_file, non_empty_cart):
    responses = iter(["x"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(non_empty_cart)
    assert result is False


def test_9_many_items_confirm(monkeypatch, copy_csv_file, many_items_cart):
    responses = iter(["Y"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(many_items_cart)
    assert result is True


def test_10_many_items_deny(monkeypatch, copy_csv_file, many_items_cart):
    responses = iter(["N"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    result = logout(many_items_cart)
    assert result is False


def test_1_invalid_logout_int_item(copy_csv_file, int_item_cart):
    with pytest.raises(TypeError):
        logout(int_item_cart)


def test_2_invalid_logout_str_items(copy_csv_file, str_item_cart):
    with pytest.raises(AttributeError):
        logout(str_item_cart)


def test_3_invalid_logout_float_items(copy_csv_file, float_item_cart):
    with pytest.raises(TypeError):
        logout(float_item_cart)

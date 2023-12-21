import pytest
from products import *
from login import *
import os
import shutil

@pytest.fixture(scope="module")
def copy_files():
    # Set up
    os.chdir("tests")
    shutil.copy('../products.csv', 'products.csv')
    shutil.copy('../users.json', 'users.json')

    yield

    # Teardown
    os.remove('users.json')
    os.remove('products.csv')
    os.chdir("..")

def test_smoke_1(monkeypatch, copy_files, capsys):
    responses = iter(["Ramanathan", "Notaproblem23*", "all", "n", "Banana", "y", "r", "1", "r", "-2", "r", "2000", "r", "1", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "1. Apple - $2.0 - Units: 10" in captured.out
    assert "There are no items in the cart to remove" in captured.out
    assert "Apple added to your cart." in captured.out
    assert "Not a valid product number" in captured.out
    assert "Apple removed from your cart." in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_2(monkeypatch, copy_files, capsys):
    responses = iter(["name", "incorrect password", "no", "name", "incorrect password", "yes", "P@ssword1", "all","y","l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "You have been logged out" in captured.out

def test_smoke_3(monkeypatch, copy_files, capsys):
    responses = iter(["name", "incorrect password", "yes", "asdjflkajsfdA2*", "Ramanathan", "Notaproblem23*", "all", "y", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "User with same username already exists" in captured.out
    assert "Successfully logged in" in captured.out
    assert "[\'Laptop\', \'800\', \'1\']\n" in captured.out
    assert "1. Apple - $2.0 - Units: 10" in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_4(monkeypatch, copy_files, capsys):
    responses = iter(["Ramanathan", "Notaproblem23*", "all", "y", "c", "no", "c", "y", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Your basket is empty. Please add items before checking out." in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_5(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "1", "c", "y", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Apple added to your cart" in captured.out
    assert "['Apple', 2.0, 10]" in captured.out
    assert "Thank you for your purchase, Rover! Your remaining balance is 48.0" in captured.out

def test_smoke_6(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "20", "c", "y", "7", "l", "y"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Salmon added to your cart." in captured.out
    assert "['Salmon', 10.0, 2]" in captured.out
    assert "Thank you for your purchase, Rover! Your remaining balance is 40.0" in captured.out
    assert "Carrot added to your cart." in captured.out
    assert "Your cart is not empty.You have following items" in captured.out
    assert "['Carrot', 0.5, 20]" in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_7(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "71", "71", "71", "67", "c", "y", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Backpack added to your cart." in captured.out
    assert "['Backpack', 15.0, 1]" in captured.out
    assert "Thank you for your purchase, Rover! Your remaining balance is 0.0" in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_8(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "6", "6", "6", "6", "6", "6", "c", "y", "r", "6", "r", "6", "r", "6", "r", "6", "r", "6", "r", "6", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Watermelon added to your cart." in captured.out
    assert "['Watermelon', 10.0, 1]" in captured.out
    assert "You don't have enough money to complete the purchase" in captured.out
    assert "Please try again!" in captured.out
    assert "Watermelon removed from your cart." in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_9(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "6", "2", "45", "53", "55", "65", "c", "y", "r", "55", "r", "53", "c", "y", "l"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "Watermelon added to your cart." in captured.out
    assert "Banana added to your cart." in captured.out
    assert "Laundry Detergent added to your cart." in captured.out
    assert "Headphones added to your cart." in captured.out
    assert "TV added to your cart." in captured.out
    assert "Sunglasses added to your cart." in captured.out
    assert "['Watermelon', 10.0, 1]" in captured.out
    assert "You don't have enough money to complete the purchase" in captured.out
    assert "Please try again!" in captured.out
    assert "TV removed from your cart." in captured.out
    assert "Headphones removed from your cart." in captured.out
    assert "Thank you for your purchase, Rover! Your remaining balance is 25.5" in captured.out
    assert "You have been logged out" in captured.out

def test_smoke_10(monkeypatch, copy_files, capsys):
    responses = iter(["Rover", "Dog12@34", "all", "y", "6", "r", "r", "l", "y"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = searchAndBuyProduct()

    captured = capsys.readouterr()
    assert "Successfully logged in" in captured.out
    assert "67. Pens - $0.5 - Units: 10" in captured.out
    assert "Carrot added to your cart." in captured.out
    assert "r is not an integer" in captured.out
    assert "Your cart is not empty.You have following items" in captured.out
    assert "['Carrot', 0.5, 20]" in captured.out
    assert "You have been logged out" in captured.out
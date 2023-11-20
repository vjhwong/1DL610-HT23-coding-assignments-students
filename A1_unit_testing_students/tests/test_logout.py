import pytest
from ..logout import logout

from ..checkout_and_payment import *
import shutil
import os

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def load_stub(mocker):
    return mocker.patch('load_products_from_csv', return_value=[])


#@pytest.fixture
#def cart_with_items():
#    cart = ShoppingCart()
#    cart.add_item(Product("Product1", 10.0, 2))
#    cart.add_item(Product("Product2", 20.0, 1))
#   return cart

@pytest.fixture
def copy_csv_file():
    # Set up
    shutil.copy('..\products.csv', 'copy_products.csv')
    yield
    # Teardown
    os.remove('copy_products.csv')

def test_1(copy_csv_file, load_stub):
    result = logout(empty_cart)

    #result = logout(empty_cart)


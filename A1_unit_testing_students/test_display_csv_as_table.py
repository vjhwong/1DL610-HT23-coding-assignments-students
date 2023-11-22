from products import *
import pytest
import os
import shutil
import sys


@pytest.fixture
def copy_csv_file():
    # Set up
    shutil.copy('products.csv', 'copy_products.csv')
    yield
    # Teardown
    os.remove('copy_products.csv')

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
        csv_writer.writerow(['Product', 'Price', 'Units'])  # Writing only the header
    return csv_filename


@pytest.fixture
def csv_file_without_header(tmp_path):
    # Create a CSV file without a header using the pytest tmp_path fixture
    csv_filename = tmp_path / 'no_header.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Apple', 1.0, 10])  # Example row without a header
        csv_writer.writerow(['Banana', 0.5, 20])
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        display_csv_as_table("no_csv.csv")


def test_empty_csv_file(empty_csv_file, capsys):
    # Test displaying an empty CSV file
    display_csv_as_table(empty_csv_file)

    # Capture printed output
    captured = capsys.readouterr()
    assert captured.out == '[]\n'


def test_display_csv_header_only_file(header_only_csv_file, capsys):
    # Test displaying a CSV file with only a header
    display_csv_as_table(header_only_csv_file)

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the header is printed correctly
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out


def test_display_csv_without_header(csv_file_without_header, capsys):
    # Test displaying a CSV file without a header
    display_csv_as_table(csv_file_without_header)

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the header is not present in the output
    assert 'Product' not in captured.out
    assert 'Price' not in captured.out
    assert 'Units' not in captured.out

    # Assert that the rows are printed correctly
    assert 'Apple' in captured.out
    assert 'Banana' in captured.out
    assert 'Orange' in captured.out


def test_full_csv_file(copy_csv_file, capsys):
    display_csv_as_table("products.csv")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
     "['Apple', '2', '10']\n"
     "['Banana', '1', '15']\n"
     "['Orange', '1.5', '8']\n"
     "['Grapes', '3', '5']\n"
     "['Strawberry', '4', '12']\n"
     "['Watermelon', '10', '1']\n"
     "['Carrot', '0.5', '20']\n"
     "['Broccoli', '1.5', '10']\n"
     "['Tomato', '1', '15']\n"
     "['Cucumber', '1', '12']\n"
     "['Potato', '0.75', '18']\n"
     "['Onion', '0.8', '20']\n"
     "['Bell Pepper', '1.2', '8']\n"
     "['Lettuce', '2', '5']\n"
     "['Spinach', '2.5', '7']\n"
     "['Milk', '3', '10']\n"
     "['Eggs', '2', '24']\n"
     "['Cheese', '5', '8']\n"
     "['Chicken Breast', '7', '4']\n"
     "['Salmon', '10', '2']\n"
     "['Ground Beef', '6', '5']\n"
     "['Pasta', '1', '15']\n"
     "['Rice', '1.5', '10']\n"
     "['Bread', '2', '8']\n"
     "['Butter', '3', '6']\n"
     "['Yogurt', '2', '12']\n"
     "['Ice Cream', '4', '6']\n"
     "['Chocolate', '2.5', '8']\n"
     "['Coffee', '5', '4']\n"
     "['Tea', '2', '10']\n"
     "['Soda', '1.5', '12']\n"
     "['Water', '1', '20']\n"
     "['Juice', '3', '8']\n"
     "['Chips', '2.5', '10']\n"
     "['Cookies', '3', '8']\n"
     "['Cereal', '2', '12']\n"
     "['Oatmeal', '1.5', '15']\n"
     "['Peanut Butter', '3', '6']\n"
     "['Jelly', '2', '8']\n"
     "['Toothpaste', '1.5', '10']\n"
     "['Shampoo', '2', '8']\n"
     "['Soap', '1', '12']\n"
     "['Toilet Paper', '0.75', '24']\n"
     "['Towel', '4', '6']\n"
     "['Laundry Detergent', '3.5', '8']\n"
     "['Dish Soap', '1.5', '12']\n"
     "['Broom', '5', '4']\n"
     "['Trash Bags', '2', '10']\n"
     "['Light Bulbs', '1', '15']\n"
     "['Batteries', '3', '6']\n"
     "['Phone Charger', '5', '4']\n"
     "['Laptop', '800', '1']\n"
     "['Headphones', '50', '1']\n"
     "['Bluetooth Speaker', '30', '1']\n"
     "['TV', '500', '1']\n"
     "['Microwave', '80', '1']\n"
     "['Coffee Maker', '40', '1']\n"
     "['Toaster', '20', '1']\n"
     "['Blender', '30', '1']\n"
     "['Vacuum Cleaner', '100', '1']\n"
     "['Dumbbells', '20', '2']\n"
     "['Yoga Mat', '15', '1']\n"
     "['Running Shoes', '60', '1']\n"
     "['Backpack', '25', '1']\n"
     "['Sunglasses', '10', '1']\n"
     "['Hat', '8', '1']\n"
     "['Gloves', '5', '1']\n"
     "['Umbrella', '7', '1']\n"
     "['Notebook', '2', '5']\n"
     "['Pens', '0.5', '10']\n"
     "['Backpack', '15', '1']\n")
    assert captured.out == expected_output






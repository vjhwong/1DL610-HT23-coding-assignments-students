from products import *
import pytest
import os
import shutil


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
def csv_file_with_missing_values(tmp_path):
    # Create a CSV file with missing values
    csv_filename = tmp_path / 'missing_values.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['Apple', 1.0, ''])  # Missing 'Units' value in the second row
        csv_writer.writerow(['Banana', '', 20])  # Missing 'Price' value in the third row
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename


@pytest.fixture
def special_characters_csv_file(tmp_path):
    # Create a CSV file with special characters
    csv_filename = tmp_path / 'special_characters.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        header = ['Product', 'Price', 'Units']
        csv_writer.writerow(header)
        data = [['Apple', '$5.00', 10], ['Banana', '€2.50', 20], ['Orange', '¥3.00', 15]]
        csv_writer.writerows(data)
    return csv_filename


@pytest.fixture
def irregular_spacing_csv_file(tmp_path):
    # Create a CSV file with irregular spacing
    csv_filename = tmp_path / 'irregular_spacing.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write rows with irregular spacing
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['Apple', 1.0, 10])
        csv_writer.writerow(['Banana',    0.5, 20])  # Irregular spacing
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename


@pytest.fixture
def quoted_values_csv_file(tmp_path):
    # Create a CSV file with quoted values
    csv_filename = tmp_path / 'quoted_values.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['"Apple"', '"2.5"', '"10"'])
        csv_writer.writerow(['"Banana"', '"1.5"', '"20"'])
        csv_writer.writerow(['"Orange"', '"3.0"', '"15"'])
    return csv_filename


def test_1_display_file_not_found():
    with pytest.raises(FileNotFoundError):
        display_csv_as_table("no_csv.csv")


def test_2_display_empty_csv_file(empty_csv_file, capsys):
    display_csv_as_table(empty_csv_file)
    captured = capsys.readouterr()
    assert captured.out == '[]\n'


def test_3_display_csv_header_only_file(header_only_csv_file, capsys):
    display_csv_as_table(header_only_csv_file)
    captured = capsys.readouterr()
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out


def test_4_display_csv_without_header(csv_file_without_header, capsys):
    display_csv_as_table(csv_file_without_header)
    captured = capsys.readouterr()
    # Assert that the header is not present in the output
    assert 'Product' not in captured.out
    assert 'Price' not in captured.out
    assert 'Units' not in captured.out

    # Assert that the rows are printed
    assert 'Apple' in captured.out
    assert 'Banana' in captured.out
    assert 'Orange' in captured.out


def test_5_display_csv_different_delimiters(different_delimiter_csv_file, capsys):
    display_csv_as_table(different_delimiter_csv_file)
    captured = capsys.readouterr()
    # Assert that the header is printed
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out

    # Assert that the rows are printed
    assert 'Apple' in captured.out
    assert '1.0' in captured.out
    assert '10' in captured.out


def test_6_display_csv_with_missing_values(csv_file_with_missing_values, capsys):
    display_csv_as_table(csv_file_with_missing_values)
    captured = capsys.readouterr()
    # Assert that the header is printed correctly
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out

    # Assert that rows are printed, even with missing values
    assert 'Apple' in captured.out
    assert 'Banana' in captured.out
    assert 'Orange' in captured.out

    # Assert that missing values are indicated
    assert '[]' not in captured.out


def test_7_display_csv_special_characters(special_characters_csv_file, capsys):
    display_csv_as_table(special_characters_csv_file)
    captured = capsys.readouterr()
    # Assert that the header is printed correctly
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out

    # Assert that rows with special characters are printed correctly
    assert 'Apple' in captured.out
    assert '$5.00' in captured.out
    assert '10' in captured.out
    assert 'Banana' in captured.out
    assert '€2.50' in captured.out
    assert '20' in captured.out
    assert 'Orange' in captured.out
    assert '¥3.00' in captured.out
    assert '15' in captured.out


def test_8_display_csv_irregular_spacing(irregular_spacing_csv_file, capsys):
    display_csv_as_table(irregular_spacing_csv_file)
    captured = capsys.readouterr()
    # Assert that the header is printed correctly
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out

    # Assert that rows are printed with irregular spacing
    assert 'Banana' in captured.out
    assert '0.5' in captured.out


def test_9_display_csv_quoted_values(quoted_values_csv_file, capsys):
    display_csv_as_table(quoted_values_csv_file)
    captured = capsys.readouterr()
    # Assert that the header is printed correctly
    assert 'Product' in captured.out
    assert 'Price' in captured.out
    assert 'Units' in captured.out

    # Assert that rows with quoted values are printed correctly
    assert '"Apple"' in captured.out
    assert '"2.5"' in captured.out
    assert '"10"' in captured.out


def test_10_display_full_csv_file(copy_csv_file, capsys):
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






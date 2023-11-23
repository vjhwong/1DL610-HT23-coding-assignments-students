from products import *
import pytest
import shutil
import os
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
    # Create an empty CSV file using the pytest tmp_path fixture
    csv_filename = tmp_path / 'empty.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([])  # Writing an empty row to create an empty CSV file
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

@pytest.fixture
def different_delimiter_csv_file(tmp_path):
    # Create a CSV file with a different delimiter (e.g., semicolon)
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
    # Create a CSV file with missing values using the pytest tmp_path fixture
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
    # Create a CSV file with special characters using the pytest tmp_path fixture
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
    # Create a CSV file with irregular spacing using the pytest tmp_path fixture
    csv_filename = tmp_path / 'irregular_spacing.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write rows with irregular spacing
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['Apple', 1.0, 10])
        csv_writer.writerow(['Banana',    0.5, 20])  # Irregular spacing before '0.5'
        csv_writer.writerow(['Orange', 0.8, 15])
    return csv_filename


@pytest.fixture
def quoted_values_csv_file(tmp_path):
    # Create a CSV file with quoted values using the pytest tmp_path fixture
    csv_filename = tmp_path / 'quoted_values.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product', 'Price', 'Units'])
        csv_writer.writerow(['"Apple"', '"2.5"', '"10"'])
        csv_writer.writerow(['"Banana"', '"1.5"', '"20"'])
        csv_writer.writerow(['"Orange"', '"3.0"', '"15"'])
    return csv_filename


def test_1(copy_csv_file, capsys):
    display_filtered_table("products.csv","all")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n")
    assert captured.out == expected_output

def test_2(copy_csv_file, capsys):
    display_filtered_table("products.csv","Orange")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
                       "['Orange', '1.5', '8']\n")
    assert captured.out == expected_output

def test_3(copy_csv_file, capsys):
    display_filtered_table("products.csv","Orange Onion")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
                        "['Orange', '1.5', '8']\n"
                        "['Onion', '0.8', '20']\n")
    assert captured.out == expected_output

def test_4_empty_csv(empty_csv_file, capsys):
    with pytest.raises(ValueError):
        display_filtered_table(empty_csv_file,"Onion")
        captured = capsys.readouterr()
        expected_output = ()
        assert captured.out == expected_output


def test_5_file_not_found_csv():
    with pytest.raises(FileNotFoundError):
        display_filtered_table("no_csv.csv", "search")

def test_6_header_only_csv(header_only_csv_file, capsys):
    display_filtered_table(header_only_csv_file, "Orange Onion")
    captured = capsys.readouterr()
    expected_output = "['Product', 'Price', 'Units']\n"
    assert captured.out == expected_output

def test_7_csv_without_header(csv_file_without_header, capsys):
    with pytest.raises(ValueError):
        display_filtered_table(csv_file_without_header, "Apple Banana")
        captured = capsys.readouterr()
        expected_output = ("['Apple', 1.0, 10]\n"
                           "['Banana', 0.5, 20]")
        assert captured.out == expected_output

def test_8_different_delimiter_csv_file(different_delimiter_csv_file, capsys):
    with pytest.raises(ValueError):
        display_filtered_table(different_delimiter_csv_file,"Apple")
        captured = capsys.readouterr()
        expected_output = ("['Product', 'Price', 'Units']\n"
                           "['Apple', 1.0, 10]\n")
        assert captured.out == expected_output

def test_9_missing_values(csv_file_with_missing_values, capsys):
    display_filtered_table(csv_file_with_missing_values, "Apple")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
                       "['Apple', '1.0', '']\n")
    assert captured.out == expected_output

def test_10_special_characters(special_characters_csv_file, capsys):
    display_filtered_table(special_characters_csv_file, "Apple")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
                       "['Apple', '$5.00', '10']\n")
    assert captured.out == expected_output


def test_11_irregular_spacing_csv_file(irregular_spacing_csv_file, capsys):
    display_filtered_table(irregular_spacing_csv_file, "Apple")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n"
                       "['Apple', '1.0', '10']\n")
    assert captured.out == expected_output

def test_12_quoted_values_csv_file(quoted_values_csv_file, capsys):
    display_filtered_table(quoted_values_csv_file, "Apple")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n")
    assert captured.out == expected_output

def test_1_invalid_type_int(copy_csv_file, capsys):
    with pytest.raises(TypeError):
        display_filtered_table(copy_csv_file, 1)
        captured = capsys.readouterr()
        expected_output = ("['Product', 'Price', 'Units']\n")
        assert captured.out == expected_output

def test_2_invalid_type_float(copy_csv_file, capsys):
    with pytest.raises(TypeError):
        display_filtered_table(copy_csv_file, 4.2)
        captured = capsys.readouterr()
        expected_output = ("['Product', 'Price', 'Units']\n")
        assert captured.out == expected_output


def test_3_invalid_type_list(copy_csv_file, capsys):
    with pytest.raises(TypeError):
        display_filtered_table(copy_csv_file, [])
        captured = capsys.readouterr()
        expected_output = ("['Product', 'Price', 'Units']\n")
        assert captured.out == expected_output



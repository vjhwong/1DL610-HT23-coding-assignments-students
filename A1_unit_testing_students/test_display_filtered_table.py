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


def test_1(copy_csv_file, capsys):
    display_filtered_table("products.csv","all")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n")
    assert captured.out == expected_output

def test_2(copy_csv_file, capsys):
    display_filtered_table("products.csv","Orange")
    captured = capsys.readouterr()
    expected_output = ("['Product', 'Price', 'Units']\n['Orange', '1.5', '8']\n")
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

#def test_9(capsys):

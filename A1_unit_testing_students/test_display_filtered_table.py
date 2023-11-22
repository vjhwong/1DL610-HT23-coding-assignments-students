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
    with pytest.raises(
    display_filtered_table(empty_csv_file,"Onion")
    captured = capsys.readouterr()
    expected_output = ()
    assert captured.out == expected_output


def test_file_not_found_csv():
    with pytest.raises(FileNotFoundError):
        display_filtered_table("no_csv.csv", "search")
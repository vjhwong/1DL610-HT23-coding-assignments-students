import pytest
import test_login
from test_login import copy_json_file
import test_logout
from test_logout import *
import test_display_csv_as_table
from test_display_filtered_table import *
import test_display_filtered_table
from test_display_filtered_table import *
import test_searchAndBuyProduct
from test_searchAndBuyProduct import *

""" Regtest for test_login """


def test_reg_login_1(copy_json_file, monkeypatch):
    test_login.test_login5(monkeypatch, copy_json_file)


def test_reg_login_2(monkeypatch, copy_json_file):
    test_login.test_login6(monkeypatch, copy_json_file)


def test_reg_login_3(monkeypatch, copy_json_file):
    test_login.test_add_new_user2(monkeypatch, copy_json_file)


def test_reg_login_4(monkeypatch, copy_json_file):
    test_login.test_add_new_user3(monkeypatch, copy_json_file)


def test_reg_login_5(monkeypatch, copy_json_file):
    test_login.test_add_new_user4(monkeypatch, copy_json_file)


"""Regtest for test_logout"""


def test_reg_logout_1(monkeypatch, copy_csv_file, one_item_cart):
    test_logout.test_6_logout_single_item_confirm(monkeypatch, copy_csv_file, one_item_cart)


def test_reg_logout_2(monkeypatch, copy_csv_file, one_item_cart):
    test_logout.test_7_logout_single_item_deny(monkeypatch, copy_csv_file, one_item_cart)


def test_reg_logout_3(monkeypatch, copy_csv_file, non_empty_cart):
    test_logout.test_8_logout_random_confirmation(monkeypatch, copy_csv_file, non_empty_cart)


def test_reg_logout_4(monkeypatch, copy_csv_file, many_items_cart):
    test_logout.test_9_many_items_confirm(monkeypatch, copy_csv_file, many_items_cart)


def test_reg_logout_5(monkeypatch, copy_csv_file, many_items_cart):
    test_logout.test_10_many_items_deny(monkeypatch, copy_csv_file, many_items_cart)


"""Regtest for test_display_csv_as_table"""


def test_reg_display_csv_as_table_1(csv_file_with_missing_values, capsys):
    test_display_csv_as_table.test_6_display_csv_with_missing_values(csv_file_with_missing_values, capsys)


def test_reg_display_csv_as_table_2(special_characters_csv_file, capsys):
    test_display_csv_as_table.test_7_display_csv_special_characters(special_characters_csv_file, capsys)


def test_reg_display_csv_as_table_3(irregular_spacing_csv_file, capsys):
    test_display_csv_as_table.test_8_display_csv_irregular_spacing(irregular_spacing_csv_file, capsys)


def test_reg_display_csv_as_table_4(quoted_values_csv_file, capsys):
    test_display_csv_as_table.test_9_display_csv_quoted_values(quoted_values_csv_file, capsys)


def test_reg_display_csv_as_table_5(copy_csv_file, capsys):
    test_display_csv_as_table.test_10_display_full_csv_file(copy_csv_file, capsys)


"""Regtest for test_display_filtered_table"""


def test_reg_display_filtered_table_1(header_only_csv_file, capsys):
    test_display_filtered_table.test_6_header_only_csv(header_only_csv_file, capsys)


def test_reg_display_filtered_table_2(csv_file_without_header, capsys):
    test_display_filtered_table.test_7_csv_without_header(csv_file_without_header, capsys)


def test_reg_display_filtered_table_3(csv_file_without_header, capsys):
    test_display_filtered_table.test_8_different_delimiter_csv_file(csv_file_without_header, capsys)


def test_reg_display_filtered_table_4(different_delimiter_csv_file, capsys):
    test_display_filtered_table.test_9_missing_values(different_delimiter_csv_file, capsys)


def test_reg_display_filtered_table_5(special_characters_csv_file, capsys):
    test_display_filtered_table.test_10_special_characters(special_characters_csv_file, capsys)


"""Regtest for test_searchAndBuyProduct"""


def test_reg_searchAndBuyProduct_1(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_6_single_two_calls(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)


def test_reg_searchAndBuyProduct_2(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_7_pair_two_calls(copy_csv_file, login_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)


def test_reg_searchAndBuyProduct_3(copy_csv_file, login_stub, display_csv_as_table_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_8_pair_single_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, display_filtered_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)


def test_reg_searchAndBuyProduct_4(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_9_pair_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)


def test_reg_searchAndBuyProduct_5(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch):
    test_searchAndBuyProduct.test_10_many_all_calls(copy_csv_file, login_stub, display_csv_as_table_stub, checkoutAndPayment_stub, mocker, monkeypatch)


"""Tests for card payment"""



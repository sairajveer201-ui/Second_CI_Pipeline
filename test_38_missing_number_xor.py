"""Test cases for Program 38."""

import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle_number():
    assert module.missing_number([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert module.missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert module.missing_number([1, 2, 3, 4]) == 5


def test_single_missing_number():
    assert module.missing_number([]) == 1


def test_larger_list():
    assert module.missing_number([1, 2, 3, 5, 6, 7, 8, 9, 10]) == 4
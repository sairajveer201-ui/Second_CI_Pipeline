"""Test cases for Program 37."""

import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_by_two():
    assert module.rotate_string("hello", 2) == "lohel"


def test_rotate_by_zero():
    assert module.rotate_string("hello", 0) == "hello"


def test_rotate_by_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_by_more_than_length():
    assert module.rotate_string("hello", 7) == "lohel"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
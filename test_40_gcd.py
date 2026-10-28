"""Test cases for Program 40."""

import importlib

module = importlib.import_module("40_gcd")


def test_normal_numbers():
    assert module.gcd(48, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 5) == 1


def test_one_number_is_zero():
    assert module.gcd(10, 0) == 10


def test_negative_numbers():
    assert module.gcd(-48, 18) == 6


def test_both_numbers_zero():
    assert module.gcd(0, 0) == 0
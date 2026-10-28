"""Test cases for Program 31: Check Pangram."""

import importlib

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False


def test_pangram_case_insensitive():
    assert module.is_pangram(
        "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    ) is True


def test_pangram_empty_string():
    assert module.is_pangram("") is False
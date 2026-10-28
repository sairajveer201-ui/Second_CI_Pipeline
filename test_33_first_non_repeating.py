"""Test cases for Program 33."""

import importlib

module = importlib.import_module("33_first_non_repeating")


def test_normal_string():
    assert module.first_non_repeating("swiss") == "w"


def test_all_characters_repeat():
    assert module.first_non_repeating("aabbcc") is None


def test_first_character_is_unique():
    assert module.first_non_repeating("abcabcx") == "x"


def test_empty_string():
    assert module.first_non_repeating("") is None
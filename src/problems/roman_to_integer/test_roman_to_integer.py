import pytest
from roman_to_integer import *

def test_1():
    assert roman_to_integer.solution("III") == 3


def test_2():
    assert roman_to_integer.solution("LVIII") == 58


def test_3():
    assert roman_to_integer.solution("MCMXCIV") == 1994

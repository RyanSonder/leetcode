import pytest
import pytest_benchmark
from roman_to_integer import *

def test_1(benchmark):
    result = benchmark(roman_to_integer.solution, "III")
    assert result == 3


def test_2(benchmark):
    result = benchmark(roman_to_integer.solution, "LVIII")
    assert result == 58


def test_3(benchmark):
    result = benchmark(roman_to_integer.solution, "MCMXCIV")
    assert result == 1994

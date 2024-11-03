import pytest
from rotate_string import *

def test_rotate_string_1(benchmark):
    result = benchmark(rotate_string.solution, "abcde", "cdeab")
    assert result == True

def test_rotate_string_2(benchmark):
    result = benchmark(rotate_string.solution, "abcde", "bcdea")
    assert result == False



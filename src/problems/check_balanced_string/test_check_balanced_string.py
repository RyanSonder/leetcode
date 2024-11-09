import pytest
from check_balanced_string import *

def test_check_balanced_string_1(benchmark):
    result = benchmark(check_balanced_string.solution, check_balanced_string.solution, "1234")
    assert result == False

def test_check_balanced_string_2(benchmark):
    result = benchmark(check_balanced_string.solution, check_balanced_string.solution, "24123")
    assert result == True


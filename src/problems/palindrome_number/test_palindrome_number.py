import pytest
from palindrome_number import *

def test_1(benchmark):
    result = benchmark(palindrome_number.solution, x=121)
    assert result == True

def test_2(benchmark):
    result = benchmark(palindrome_number.solution, x=-121)
    assert result == False

def test_3(benchmark):
    result = benchmark(palindrome_number.solution, x=10)
    assert result == False
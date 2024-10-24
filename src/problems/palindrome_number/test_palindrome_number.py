import pytest
from palindrome_number import *

def test_palindrome_number_1(benchmark):
    result = benchmark(palindrome_number.solution, x=121)
    assert result == True

def test_palindrome_number_2(benchmark):
    result = benchmark(palindrome_number.solution, x=-121)
    assert result == False

def test_palindrome_number_3(benchmark):
    result = benchmark(palindrome_number.solution, x=10)
    assert result == False
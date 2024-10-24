import pytest
from palindrome_number import *

def test_palindrome_number_1(benchmark):
    result = benchmark(palindrome_number.solution, x=121)
    assert result == True # 2.08 : 420.32 ? 533.79

def test_palindrome_number_2(benchmark):
    result = benchmark(palindrome_number.solution, x=-121)
    assert result == False

def test_palindrome_number_3(benchmark):
    result = benchmark(palindrome_number.solution, x=10)
    assert result == False # 1.00 : 256.64

def test_palindrome_number_4(benchmark):
    result = benchmark(palindrome_number.solution, x=12345678987654320)
    assert result == False # 16.09 : 1890.47 ? 4129.34

def test_palindrome_number_5(benchmark):
    result = benchmark(palindrome_number.solution, x=12345678987654321)
    assert result == True # 16.09 : 1913.04 ? 4129.34

def test_palindrome_number_6(benchmark):
    result = benchmark(palindrome_number.solution, x=123454321)
    assert result == True # 8.09 : 815.55 ? 2076.14

def test_palindrome_number_7(benchmark):
    result = benchmark(palindrome_number.solution, x=123454320)
    assert result == False # 8.09 : 831.33 ? 2076.14

def test_palindrome_number_8(benchmark):
    result = benchmark(palindrome_number.solution, x=-12345678987654321)
    assert result == False
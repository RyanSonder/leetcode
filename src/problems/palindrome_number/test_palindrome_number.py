import pytest
from palindrome_number import *

def test_1():
    assert palindrome_number.solution(x=121) == True

def test_2():
    assert palindrome_number.solution(x=-121) == False

def test_3():
    assert palindrome_number.solution(x=10) == False
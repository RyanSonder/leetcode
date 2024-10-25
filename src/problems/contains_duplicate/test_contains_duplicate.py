import pytest
from contains_duplicate import *

def test_contains_duplicate_1(benchmark):
    result = benchmark(contains_duplicate.solution, [1,2,3,1])
    assert result == True

def test_contains_duplicate_2(benchmark):
    result = benchmark(contains_duplicate.solution, [1,2,3,4])
    assert result == False

def test_contains_duplicate_3(benchmark):
    result = benchmark(contains_duplicate.solution, [1,1,1,3,3,4,3,2,4,2])
    assert result == True

def test_contains_duplicate_4(benchmark):
    result = benchmark(contains_duplicate.solution, [0,1,2,3,4,5,6,7,8,9])
    assert result == False
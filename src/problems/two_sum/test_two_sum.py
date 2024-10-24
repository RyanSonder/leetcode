import pytest
from two_sum import *

def test_two_sum_1(benchmark):
    result = benchmark(two_sum.solution, nums=[2,7,11,15], target=9)
    assert result == [0,1]

def test_two_sum_2(benchmark):
    result = benchmark(two_sum.solution, nums=[3,2,4], target=6)
    assert result == [1,2]

def test_two_sum_3(benchmark):
    result = benchmark(two_sum.solution, nums=[3,3], target=6)
    assert result == [0,1]
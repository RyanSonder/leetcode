import pytest
from product_of_array_except_self import *

def test_product_of_array_except_self_1(benchmark):
    result = benchmark(product_of_array_except_self.solution, [1,2,3,4])
    assert result == [24,12,8,6]

def test_product_of_array_except_self_2(benchmark):
    result = benchmark(product_of_array_except_self.solution, [-1,1,0,-3,3])
    assert result == [0,0,9,0,0]



import pytest
from two_sum import *

def test_1():
    assert two_sum.solution(nums=[2,7,11,15], target=9) == [0,1]

def test_2():
    assert two_sum.solution(nums=[3,2,4], target=6) == [1,2]

def test_3():
    assert two_sum.solution(nums=[3,3], target=6) == [0,1]
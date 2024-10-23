import pytest
from add_two_numbers import *

def test_1():
    assert add_two_numbers.solution(l1=[2,4,3], l2=[5,6,7]) == [7,0,8]

def test_2():
    assert add_two_numbers.solution(l1=[0], l2=[0]) == [0]

def test_3():
    assert add_two_numbers.solution(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]) == [8,9,9,9,0,0,0,1]
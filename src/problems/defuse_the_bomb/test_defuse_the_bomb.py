import pytest
from defuse_the_bomb import *

def test_defuse_the_bomb_1(benchmark):
    result = benchmark(DefuseTheBomb.solution, DefuseTheBomb, code=[5,7,1,4], k=3)
    assert result == [12,10,16,13]

def test_defuse_the_bomb_2(benchmark):
    result = benchmark(DefuseTheBomb.solution, DefuseTheBomb, code=[1,2,3,4], k=0)
    assert result == [0,0,0,0]

def test_defuse_the_bomb_3(benchmark):
    result = benchmark(DefuseTheBomb.solution, DefuseTheBomb, code=[2,4,9,3], k=-2)
    assert result == [12,5,6,13]
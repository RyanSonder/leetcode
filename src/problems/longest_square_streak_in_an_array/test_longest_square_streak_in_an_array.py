import pytest
from longest_square_streak_in_an_array import *

def test_longest_square_streak_in_an_array_1(benchmark):
    result = benchmark(longest_square_streak_in_an_array.solution, [4,3,6,16,8,2])
    assert result == 3

def test_longest_square_streak_in_an_array_2(benchmark):
    result = benchmark(longest_square_streak_in_an_array.solution, [2,3,5,6,7])
    assert result == -1



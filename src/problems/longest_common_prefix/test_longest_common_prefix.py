import pytest
from longest_common_prefix import *

def test_longest_common_prefix_1(benchmark):
    result = benchmark(longest_common_prefix.solution, ["flower","flow","flight"])
    assert result == "fl"

def test_longest_common_prefix_2(benchmark):
    result = benchmark(longest_common_prefix.solution, ["dog","racecar","car"])
    assert result == ""

def test_longest_common_prefix_3(benchmark):
    result = benchmark(longest_common_prefix.solution, ["perhaps","perchance","peruse","percussion","periwinkle"])
    assert result == "per"


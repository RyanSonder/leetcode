import pytest
from top_k_frequent_elements import *


def test_top_k_frequent_elements_1(benchmark):
    result = benchmark(top_k_frequent_elements.solution, nums=[1, 2, 2, 3, 3, 3], k=2)
    assert result == [2, 3]


def test_top_k_frequent_elements_2(benchmark):
    result = benchmark(top_k_frequent_elements.solution, nums=[7, 7], k=1)
    assert result == [7]


def test_top_k_frequent_elements_3(benchmark):
    result = benchmark(
        top_k_frequent_elements.solution,
        nums=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],
        k=4,
    )
    assert result == [3, 4, 5, 6]

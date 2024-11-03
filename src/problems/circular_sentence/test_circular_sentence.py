import pytest
from circular_sentence import *

def test_circular_sentence_1(benchmark):
    result = benchmark(circular_sentence.solution, "leetcode exercises sound delightful")
    assert result == True

def test_circular_sentence_2(benchmark):
    result = benchmark(circular_sentence.solution, "eetcode")
    assert result == True

def test_circular_sentence_3(benchmark):
    result = benchmark(circular_sentence.solution, "Leetcode is cool")
    assert result == False

def test_circular_sentence_4(benchmark):
    result = benchmark(circular_sentence.solution, "leetcode exercises sound delightful leetcode exercises sound delightful leetcode exercises sound delightful leetcode exercises sound delightful leetcode exercises sound delightful leetcode exercises sound delightful")
    assert result == True
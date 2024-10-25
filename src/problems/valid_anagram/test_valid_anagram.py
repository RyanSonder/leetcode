import pytest
from valid_anagram import *

def test_valid_anagram_1(benchmark):
    result = benchmark(valid_anagram.solution, "anagram", "nagaram")
    assert result == True

def test_valid_anagram_2(benchmark):
    result = benchmark(valid_anagram.solution, "rat", "car")
    assert result == False

def test_valid_anagram_3(benchmark): # Base case
    result = benchmark(valid_anagram.solution, "long", "short")
    assert result == False

def test_valid_anagram_3(benchmark): # Worst case
    result = benchmark(valid_anagram.solution, "conversationalists", "conservationalists")
    assert result == True
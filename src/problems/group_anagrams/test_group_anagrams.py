import pytest
from group_anagrams import *

def test_group_anagrams_1(benchmark): # Using a lambda to fix the benchmarking problem
    result = benchmark(lambda: group_anagrams.solution(["eat","tea","tan","ate","nat","bat"]))
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert {tuple(sorted(sublist)) for sublist in result} == {tuple(sorted(sublist)) for sublist in expected}

def test_group_anagrams_2(benchmark):
    result = benchmark(group_anagrams.solution, [""])
    assert result == [[""]]

def test_group_anagrams_3(benchmark):
    result = benchmark(group_anagrams.solution, ["a"])
    assert result == [["a"]]

def test_group_anagrams_4(benchmark): 
    result = benchmark(lambda: group_anagrams.solution(["abcd", "read", "abdc", "raft", "acdb", "dear", "bcad", "fart", "dbca", "dare", "dcba"]))
    expected = [["raft", "fart"],["read", "dear", "dare"],["abcd", "abdc", "acdb", "bcad", "dbca", "dcba"]]
    assert {tuple(sorted(sublist)) for sublist in result} == {tuple(sorted(sublist)) for sublist in expected}

from bin_search import binary_search
import random
import pytest


def test_binary_search_sorted():
    for _ in range(100):
        arr = sorted(random.sample(range(-1000, 1000), 100))
        target = random.choice(arr)
        result = binary_search(arr, target)
        assert arr[result] == target


def test_binary_search_not_found():
    for _ in range(100):
        arr = sorted(random.sample(range(-1000, 1000), 100))
        target = random.randint(1000, 2000)
        result = binary_search(arr, target)
        assert result == -1


def test_binary_search_single_element_found():
    for _ in range(100):
        arr = [random.randint(-1000, 1000)]
        target = arr[0]
        result = binary_search(arr, target)
        assert result == 0


def test_binary_search_single_element_not_found():
    for _ in range(100):
        arr = [random.randint(-1000, 1000)]
        target = arr[0] + 1
        result = binary_search(arr, target)
        assert result == -1


def test_binary_search_duplicates():
    for _ in range(100):
        arr = sorted([1] * 100)
        target = 1
        result = binary_search(arr, target)
        assert result != -1


def test_binary_search_empty():
    for _ in range(100):
        arr = []
        target = random.randint(-1000, 1000)
        result = binary_search(arr, target)
        assert result == -1

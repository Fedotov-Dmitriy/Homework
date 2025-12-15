from buble_sort import bubble_sort
import pytest
import random


def test_bubble_sort_sorted():
    for _ in range(100):
        arr = random.sample(range(-1000, 1000), 100)
        bubble_sort(arr)
        assert arr == sorted(arr)


def test_bubble_sort_all_elements_same():
    for _ in range(100):
        arr = [5] * 100
        bubble_sort(arr)
        assert arr == [5] * 100


def test_bubble_sort_negative_numbers():
    for _ in range(100):
        arr = random.sample(range(-1000, 1000), 100)
        bubble_sort(arr)
        assert arr == sorted(arr)


def test_bubble_sort_single_element():
    for _ in range(100):
        arr = [random.randint(-1000, 1000)]
        bubble_sort(arr)
        assert arr == arr


def test_bubble_sort_empty():
    for _ in range(100):
        arr = []
        bubble_sort(arr)
        assert arr == []


def test_bubble_sort_mixed_numbers():
    for _ in range(100):
        arr = random.sample(range(-1000, 1000), 100)
        bubble_sort(arr)
        assert arr == sorted(arr)

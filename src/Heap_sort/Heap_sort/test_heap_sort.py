from heap_sort import heap_sort


import pytest


def test_heap_sort_base():
    arr = [12, 11, 13, 5, 6, 7]

    heap_sort(arr)

    assert arr == [5, 6, 7, 11, 12, 13]


def test_heap_sort_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7]

    heap_sort(arr)

    assert arr == [1, 2, 3, 4, 5, 6, 7]


def test_heap_sort_reverse():
    arr = [7, 6, 5, 4, 3, 2, 1]

    heap_sort(arr)

    assert arr == [1, 2, 3, 4, 5, 6, 7]


def test_heap_sort_dubl():
    arr = [1, 1, 2, 3, 6, 5, 8, 4, 8]

    heap_sort(arr)

    assert arr == [1, 1, 2, 3, 4, 5, 6, 8, 8]


def test_heap_sort_single():
    arr = [1]

    heap_sort(arr)

    assert arr == [1]


def test_heap_sort_empty():
    arr = []

    heap_sort(arr)

    assert arr == []


def test_heap_sort_negative():
    arr = [-2, -3, -4, -2, -1]

    heap_sort(arr)

    assert arr == [-4, -3, -2, -2, -1]


def test_heap_sort_mixed():
    arr = [1, 2, -1, 0, -2, 10, -4]

    heap_sort(arr)

    assert (arr) == [-4, -2, -1, 0, 1, 2, 10]


def test_heap_sort_duplicates():
    arr = [7, 7, 7, 7, 7]

    heap_sort(arr)

    assert arr == [7, 7, 7, 7, 7]


def test_heap_sort_large_values():
    arr = [1000000, 1, -500000, 0, 999999]

    heap_sort(arr)

    assert arr == [-500000, 0, 1, 999999, 1000000]


def test_heap_sort_invalid_type():
    arr = [1, "two", 3]

    with pytest.raises(TypeError):
        heap_sort(arr)

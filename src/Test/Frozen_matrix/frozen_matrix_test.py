
import pytest

from .frozen_matrix import FrozenMatrix  


def test_frozen_matrix_basic():
    fm = FrozenMatrix([[1, 2], [3, 4]])

    assert fm.shape == (2, 2)
    assert fm.rows == 2
    assert fm.cols == 2
    assert len(fm) == 2

    assert fm[0] == (1, 2)
    assert fm[1] == (3, 4)

    assert list(fm) == [(1, 2), (3, 4)]


def test_frozen_matrix_eq_and_hash_and_set_dict_usage():
    a = FrozenMatrix([[1, 2], [3, 4]])
    b = FrozenMatrix([[1, 2], [3, 4]])
    c = FrozenMatrix([[5, 6], [7, 8]])

    assert a == b
    assert a != c
    assert hash(a) == hash(b)

    s = {a, b, c}
    assert len(s) == 2

    d = {a: "first", c: "second"}
    assert d[b] == "first"
    assert d[c] == "second"


def test_frozen_matrix_invalid_input():
    with pytest.raises(ValueError):
        FrozenMatrix([])

    with pytest.raises(ValueError):
        FrozenMatrix([[1, 2], [3]])

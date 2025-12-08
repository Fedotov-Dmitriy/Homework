
import pytest

from .Matrix_package import Matrix


def test_matrix_add_and_scalar_mul():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])

    c = a + b
    assert c.shape == (2, 2)
    assert c[0] == [6, 8]
    assert c[1] == [10, 12]

    d = a * 2
    e = 2 * a
    assert d[0] == [2, 4]
    assert d[1] == [6, 8]
    assert e[0] == [2, 4]
    assert e[1] == [6, 8]


def test_matrix_matmul_and_det():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[7, 8], [9, 10], [11, 12]])

    c = a @ b
    assert c.shape == (2, 2)
    assert c[0] == [58, 64]
    assert c[1] == [139, 154]

    m = Matrix([[1, 2], [3, 4]])
    assert m.det() == pytest.approx(-2.0)
    assert abs(m) == pytest.approx(-2.0)


def test_add_raises_on_different_shapes():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[1, 2, 3]])

    with pytest.raises(ValueError):
        _ = a + b

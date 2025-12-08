from typing import Iterable, Iterator, List, Tuple, Union

Number = Union[int, float]


class Matrix:
    __slots__ = ("_data", "_rows", "_cols")

    def __init__(self, data: Iterable[Iterable[Number]]):
        rows_list: List[List[Number]] = [list(row) for row in data]

        if not rows_list or not rows_list[0]:
            raise ValueError(
                "Матрица не должна быть пустой и должна содержать хотя бы "
                "один столбец"
            )

        rows = len(rows_list)
        cols = len(rows_list[0])

        if any(len(row) != cols for row in rows_list):
            raise ValueError(
                "Все строки матрицы должны быть одинаковой длины"
            )

        self._data = rows_list
        self._rows = rows
        self._cols = cols

    @property
    def shape(self) -> Tuple[int, int]:
        return self._rows, self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def __len__(self) -> int:
        return self._rows

    def __getitem__(self, index: int) -> List[Number]:
        return self._data[index]

    def __iter__(self) -> Iterator[List[Number]]:
        return iter(self._data)

    def __repr__(self) -> str:
        return f"Matrix({self._data!r})"

    def items(self) -> Iterator[Tuple[int, int, Number]]:
        for i, row in enumerate(self._data):
            for j, value in enumerate(row):
                yield i, j, value

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.shape != other.shape:
            ra, ca = self.shape
            rb, cb = other.shape
            raise ValueError(
                f"Нельзя сложить матрицы разных размеров: "
                f"A({ra}x{ca}), B({rb}x{cb})"
            )

        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return Matrix(result)

    def __radd__(self, other: "Matrix") -> "Matrix":
        return self.__add__(other)

    def __mul__(self, other: Number) -> "Matrix":
        if isinstance(other, (int, float)):
            result = [
                [other * value for value in row]
                for row in self._data
            ]
            return Matrix(result)
        return NotImplemented

    def __rmul__(self, other: Number) -> "Matrix":
        return self.__mul__(other)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.cols != other.rows:
            raise ValueError(
                f"Несовместимые размеры для умножения: "
                f"A({self.rows}x{self.cols}), B({other.rows}x{other.cols})"
            )

        m, n, p = self.rows, self.cols, other.cols
        result: List[List[Number]] = [[0] * p for _ in range(m)]

        for i in range(m):
            for k in range(n):
                a_ik = self._data[i][k]
                row_bk = other._data[k]
                for j in range(p):
                    result[i][j] += a_ik * row_bk[j]

        return Matrix(result)

    def det(self) -> float:
        if self.rows != self.cols:
            raise ValueError(
                f"Матрица должна быть квадратной, получено "
                f"{self.rows}x{self.cols}"
            )

        n = self.rows
        m: List[List[float]] = [
            [float(value) for value in row] for row in self._data
        ]

        det_sign = 1.0

        for i in range(n):
            pivot_row = i
            for r in range(i + 1, n):
                if abs(m[r][i]) > abs(m[pivot_row][i]):
                    pivot_row = r

            if m[pivot_row][i] == 0:
                return 0.0

            if pivot_row != i:
                m[i], m[pivot_row] = m[pivot_row], m[i]
                det_sign *= -1.0

            for r in range(i + 1, n):
                factor = m[r][i] / m[i][i]
                for c in range(i, n):
                    m[r][c] -= factor * m[i][c]

        det = det_sign
        for i in range(n):
            det *= m[i][i]

        return det

    def __abs__(self) -> float:
        return self.det()

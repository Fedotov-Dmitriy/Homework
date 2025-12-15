class FrozenMatrix:
    __slots__ = ("_data", "_rows", "_cols", "_hash")

    def __init__(self, data):
        rows_list = [list(row) for row in data]

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

        frozen_rows = tuple(tuple(row) for row in rows_list)

        self._data = frozen_rows
        self._rows = rows
        self._cols = cols
        self._hash = hash(self._data)

    @property
    def shape(self):
        return self._rows, self._cols

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def __len__(self):
        return self._rows

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"FrozenMatrix({self._data!r})"

    def __eq__(self, other):
        if isinstance(other, FrozenMatrix):
            return self._data == other._data
        return NotImplemented

    def __hash__(self):
        return self._hash

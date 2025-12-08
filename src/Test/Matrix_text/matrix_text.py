from typing import List, Tuple, Union

from .matrix import Matrix

Number = Union[int, float]


def matrix_to_mtx(matrix: Matrix) -> str:
    rows, cols = matrix.shape
    entries: List[Tuple[int, int, Number]] = []

    for i in range(rows):
        row = matrix[i]
        for j in range(cols):
            value = row[j]
            if value != 0:
                entries.append((i + 1, j + 1, value))

    nnz = len(entries)
    lines: List[str] = []
    lines.append("%%MatrixMarket matrix coordinate real general")
    lines.append(f"{rows} {cols} {nnz}")

    for i, j, value in entries:
        lines.append(f"{i} {j} {value}")

    return "\n".join(lines) + "\n"


def matrix_from_mtx(text: str) -> Matrix:
    raw_lines = text.splitlines()
    index = 0

    while index < len(raw_lines) and not raw_lines[index].strip():
        index += 1

    if index >= len(raw_lines):
        raise ValueError("Пустые данные mtx")

    header = raw_lines[index].strip()
    index += 1

    if not header.lower().startswith("%%matrixmarket"):
        raise ValueError("Некорректный заголовок формата mtx")

    body_lines: List[str] = []

    for k in range(index, len(raw_lines)):
        line = raw_lines[k].strip()
        if not line or line.startswith("%"):
            continue
        body_lines.append(line)

    if not body_lines:
        raise ValueError("Отсутствуют данные матрицы в формате mtx")

    size_parts = body_lines[0].split()
    if len(size_parts) != 3:
        raise ValueError("Некорректная строка размера матрицы в mtx")

    rows = int(size_parts[0])
    cols = int(size_parts[1])
    nnz = int(size_parts[2])

    entry_lines = body_lines[1:]

    if len(entry_lines) != nnz:
        raise ValueError("Количество элементов не совпадает с nnz в mtx")

    data: List[List[Number]] = [[0.0] * cols for _ in range(rows)]

    for line in entry_lines:
        parts = line.split(maxsplit=3)
        if len(parts) < 3:
            raise ValueError("Некорректная строка элемента матрицы в mtx")
        i_str, j_str, v_str = parts[:3]
        i = int(i_str) - 1
        j = int(j_str) - 1
        value = float(v_str)
        data[i][j] = value

    return Matrix(data)

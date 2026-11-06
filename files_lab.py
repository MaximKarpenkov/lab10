from pathlib import Path


def read_matrix(path):
    """Читает матрицу из файла и возвращает список списков.

    Формат:
      первая строка: R C (два положительных целых)
      далее R строк по C целых чисел.
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    # Допустим один пустой перевод в конце — уже не окажется в splitlines,
    # но лишние пустые строки внутри считаем ошибкой.
    if not lines:
        raise ValueError("Файл пуст: ожидался заголовок 'R C'")

    # Заголовок
    try:
        parts = lines[0].split()
    except Exception:
        raise ValueError("Строка 1: не удалось разобрать заголовок")

    if len(parts) != 2:
        raise ValueError("Строка 1: ожидалось два числа (R C)")

    try:
        rows = int(parts[0])
        cols = int(parts[1])
    except ValueError:
        raise ValueError("Строка 1: R и C должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: R и C должны быть положительными")

    # Ожидаем ровно rows строк данных
    data_lines = lines[1:]
    # Убираем пустые хвостовые строки
    while data_lines and data_lines[-1] == "":
        data_lines.pop()

    if len(data_lines) != rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, получено {len(data_lines)}"
        )

    matrix = []
    for index, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(
                f"Строка {index}: ожидалось {cols} чисел, получено {len(parts)}"
            )
        try:
            row = [int(p) for p in parts]
        except ValueError:
            raise ValueError(f"Строка {index}: все ячейки должны быть целыми числами")
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    """Вариант 1: сумма положительных элементов."""
    total = 0
    for row in matrix:
        for value in row:
            if value > 0:
                total += value
    return total


def export_csv(matrix, path):
    """Дополнительно: экспорт таблицы в CSV стандартным модулем csv."""
    import csv

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)


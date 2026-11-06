from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix, selected_sum


def expect_value_error(text, description):
    try:
        read_matrix_from_text(text)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Ошибка не обнаружена: {description}")


def read_matrix_from_text(text):
    with TemporaryDirectory() as directory:
        path = Path(directory) / "matrix.txt"
        path.write_text(text, encoding="utf-8")
        return read_matrix(path)


# 1. Базовая проверка
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

# 2. Матрица 1x1 со значением 0
assert read_matrix_from_text("1 1\n0\n") == [[0]]

# 3. Пустой файл → ValueError
expect_value_error("", "пустой файл")

# 4. Заголовок 0 3 → ValueError
expect_value_error("0 3\n", "нулевое число строк")

# 5. Заголовок 1 2, одна ячейка → ValueError со ссылкой на строку 2
try:
    read_matrix_from_text("1 2\n1\n")
except ValueError as e:
    assert "Строка 2" in str(e)
else:
    raise AssertionError("Ошибка не обнаружена: неверное число ячеек")

# 6. Нечисловая ячейка → ValueError со ссылкой на строку 2
try:
    read_matrix_from_text("1 2\n1 x\n")
except ValueError as e:
    assert "Строка 2" in str(e)
else:
    raise AssertionError("Ошибка не обнаружена: нечисловая ячейка")

# 7. Лишняя строка данных → ValueError
expect_value_error("1 1\n0\n1\n", "лишняя строка данных")

# 8. Отсутствующий путь → FileNotFoundError
try:
    read_matrix(Path("/nonexistent/matrix.txt"))
except FileNotFoundError:
    pass
else:
    raise AssertionError("FileNotFoundError не возник")

# 9. Вариант 1: сумма положительных
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 8
assert selected_sum([[0, 0], [0, 0]]) == 0
assert selected_sum([]) == 0

print("Все проверки пройдены")

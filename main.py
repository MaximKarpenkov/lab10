import sys
from pathlib import Path

from files_lab import read_matrix, selected_sum, export_csv
from table import row_sums, column_sums


def read_positive_integer():
    """Повторяет ввод до получения положительного целого."""
    while True:
        raw = input("Введите положительное целое: ")
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: не целое число")
            continue
        if value <= 0:
            print("Ошибка: должно быть больше нуля")
            continue
        return value


def main():
    folder = Path(__file__).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"

    # Обязательное задание 1: надёжный ввод размера (демонстрация)
    size = read_positive_integer()
    print(f"Принято положительное целое: {size}")

    # Чтение таблицы с обработкой ошибок
    try:
        matrix = read_matrix(matrix_path)
    except FileNotFoundError:
        print(f"Ошибка: файл {matrix_path.name} не найден")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return
    except UnicodeError:
        print("Ошибка: файл не в кодировке UTF-8")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    # Все данные корректны — теперь можно писать отчёт
    rs = row_sums(matrix)
    cs = column_sums(matrix)
    variant_result = selected_sum(matrix)

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write("Суммы строк: " + " ".join(map(str, rs)) + "\n")
            file.write("Суммы столбцов: " + " ".join(map(str, cs)) + "\n")
            file.write(f"Результат варианта: {variant_result}\n")
    except OSError as error:
        print(f"Не удалось записать отчёт: {error}")
        return

    print(f"Отчёт записан в {report_path.name}")

    # Дополнительно: экспорт в CSV
    try:
        csv_path = folder / "matrix_export.csv"
        export_csv(matrix, csv_path)
        print(f"CSV-экспорт: {csv_path.name}")
    except OSError as error:
        print(f"Не удалось записать CSV: {error}")


if __name__ == "__main__":
    main()


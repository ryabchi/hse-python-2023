from pathlib import Path
from typing import Dict, Any, List, Optional
import re
import csv


def count_words(text: str) -> Dict[str, int]:
    """
    Функция для подсчета слов в тексте.

    При подсчете слов - все знаки препинания игнорируются.
    Словом считается непрерывная последовательность длиной больше одного
    символа, состоящая из букв в диапазоне A-Z и a-z.
    Если в последовательности присутствует цифра - это не слово.

    Hello - слово
    Hello7 - не слово

    При подсчете слов регистр букв не имеет значения.

    Результат выполнения функции словарь, в котором:
    ключ - слово в нижнем регистре
    значение - количество вхождений слов в текст

    :param text: текст, для подсчета символов
    :return: словарь, в котором:
             ключ - слово в нижнем регистре
             значение - количество вхождений слов в текст
    """

    # пиши свой код здесь
    words = {}

    text = text.strip().split()

    for word in text:
        word = re.sub(r'[,.:!?-]', "", word)
        if re.match(r'^[a-zA-Z]+$', word):
            if (word.lower() in words):
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1

    return words


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exp

    return numbers


def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    """
    Функция для расчета кешбека по операциям.
    За покупки в обычных категориях возвращается 1% от стоимости покупки
    За покупки в special_category начисляют 5% от стоимости покупки

    :param operations: список словарей, содержащих поля
           amount - сумма операции
           category - категория покупки
    :param special_category: список категорий повышенного кешбека
    :return: размер кешбека
    """
    result = 0
    default_cashback = 0.01
    special_cashback = 0.05

    for i in range(len(operations)):
        total = 0
        d = operations[i]
        if d["category"] in special_category:
            total = d["amount"] * special_cashback
        else:
            total = d["amount"] * default_cashback
        result += total

    result = float("{:.2f}".format(result))
    return result


def get_path_to_file() -> Optional[Path]:
    """
    Находит корректный путь до тестового файла.

    Если запускать тесты из pycharm - начальная папка - tests
    Если запускать файлы через make tests - начальная папка - корень проекта

    :return: путь до тестового файла tasks.csv
    """
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'


def csv_reader(header: str) -> int:
    """
    Функция считывает csv файл и подсчитывает количество
    уникальных элементов в столбце.
    Столбец выбирается на основе имени заголовка,
    переданного в переменной header.

    Обратите внимание на структуру файла!
    Первая строка - строка с заголовками.
    Остальные строки - строки с данными.

    Файл для анализа: tasks.csv
    Для того чтобы файл корректно открывался в тестах:
    для получения пути до файла - используйте функцию get_path_to_file
    которая определена перед функцией.

    CSV анализируем с помощью встроенной библиотеки csv

    :param header: название заголовка
    :return: количество уникальных элементов в столбце
    """
    elements = []

    # пиши свой код здесь
    with open(get_path_to_file()) as file:
        csv_reader = csv.reader(file, delimiter=",")
        column_id = 0
        count = 0
        for row in csv_reader:
            if count == 0:
                column_id = row.index(header)
                count += 1
            else:
                x = row[column_id]
                if (str(x) not in elements):
                    elements.append(str(x))

    result = len(elements)

    return result

from pathlib import Path
from typing import Dict, Any, List, Optional


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
    import re
    text = text.lower()
    delimiters = "!| |;|,|:|\\.|\\|"
    text = re.split(delimiters, text)
    dict = {}
    for i in range(len(text)):
        b = 1
        for j in range(len(text[i])):
            if (text[i][j].isalpha() == False):
                b = 0
        if (b == 1 and text[i] != ''):
            if (text[i] in dict):
                dict[text[i]] += 1
            else:
                dict[text[i]] = 1

    return dict


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь

    for i in range(len(numbers)):
        numbers[i] = pow(numbers[i], exp)

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

    sum = 0
    for i in range(len(operations)):
        if (operations[i]['category'] in special_category):
            sum += operations[i]['amount'] * 0.05
        else:
            sum += operations[i]['amount'] * 0.01
    return sum


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

    # пиши свой код здесь

    s1 = []
    ss = []
    import csv
    sk1 = {}
    with open(get_path_to_file(), encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                for i in range(len(row)):
                    s1.append(row[i])

            else:
                s2 = []
                for i in range(len(row)):
                    s2.append(row[i])
                ss.append(s2)
            count += 1
    for i in range(len(s1)):
        sd = []
        for j in range(len(ss)):
            sd.append(ss[j][i])
        sk1[s1[i]] = len(set(sd))

    return sk1[header]

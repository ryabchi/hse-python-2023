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

    import string
    text = text.lower()
    text = text.translate(str.maketrans({key: None for key in string.punctuation}))
    print(text)
    text = text.split()
    uniq_text = text
    uniq_text = sorted(set(uniq_text), key=lambda d: uniq_text.index(d))
    result = {}
    for i in uniq_text:
        count = 0
        m = [s for s in i if s in '123456789']
        if not m:
            for j in text:
                if i == j:
                    count += 1
            result[i] = count
    return result


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**exp
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
    result = 0.00
    for i in range(len(operations)):
        percent = 0.01
        for j in special_category:
            if j == operations[i].get('category'):
                percent = 0.05
        result += float(operations[i].get("amount"))*percent
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
    import csv
    full_mat = []
    mas = []
    a = get_path_to_file()
    with open(a) as f:
        reader = csv.reader(f)
        for row in reader:
            full_mat.append(row)
    for i in range(len(full_mat)):
        if i == 0:
            for j in range(len(full_mat[i])):
                if full_mat[i][j] == header:
                    need = j
        else:
            mas.append(full_mat[i][need])
    result = len(set(mas))
    # пиши свой код здесь
    return result


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
    def is_word(word):
        for simbol in word:
            if 'A' <= simbol <= 'Z' or 'a' <= simbol <= 'z':
                continue
            else:
                return False
        return True

    def ad_dic(dic, w):
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    non_simb = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    diction = {}
    ch_ind = 0
    while ch_ind <len(text):
        k = 0
        while ch_ind + k < len(text) and ('A' <= text[ch_ind + k] <= 'Z' or 'a' <= text[ch_ind + k] <= 'z'):
            k += 1
        if k > 1:
            if ch_ind == 0:
                if text[ch_ind + k] not in non_simb:
                    ad_dic(diction, text[ch_ind:ch_ind+k].lower())
            elif ch_ind + k == len(text):
                if text[ch_ind - 1] not in non_simb:
                    ad_dic(diction, text[ch_ind:ch_ind+k].lower())
            else:
                if text[ch_ind-1] not in non_simb and text[ch_ind+k] not in non_simb:
                    ad_dic(diction, text[ch_ind:ch_ind+k].lower())
            ch_ind += k
        ch_ind += 1
    return diction


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь

    return [x ** exp for x in numbers]


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
    for dict in operations:
        per = 0.01
        if dict["category"] in special_category:
            per = 0.05
        result += per * dict["amount"]
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

    # пиши свой код здесь
    import csv
    stolb = set()
    with open(get_path_to_file(), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stolb.add(row[header])
    return len(stolb)

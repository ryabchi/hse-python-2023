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
    ind = -1
    dic = []
    while ind < len(text) - 1:
        ind += 1
        if (ord(text[ind]) > 64 and ord(text[ind]) < 91) or (ord(text[ind]) > 96 and ord(text[ind]) < 123):
            st = str()
            for i in range(ind, len(text)):
                if (ord(text[i]) > 64 and ord(text[i]) < 91) or (ord(text[i]) > 96 and ord(text[i]) < 123):
                    st = st + text[i]
                elif ((ord(text[i]) <= 64 or ord(text[i]) >= 91) or (ord(text[i]) <= 96 or ord(text[i]) >= 123)):
                    if (ord(text[i]) >= 48 and ord(text[i]) <= 57):
                        for k in range(i, len(text)):
                            if ((ord(text[k]) <= 64 or (ord(text[k]) >= 91 and ord(text[k]) <= 96) or ord(text[k]) >= 123)):
                                if ord(text[k]) < 48 or ord(text[k]) > 57:
                                    ind = k
                                    break
                        break
                    else:
                        ind = i
                        dic.append(st.lower())
                        break
                if len(text) - 1 == i:
                    ind = i
                    dic.append(st.lower())
                    break
        i = ind
        if (ord(text[i]) >= 48 and ord(text[i]) <= 57):
            for k in range(i, len(text)):
                if ((ord(text[k]) <= 64 or (ord(text[k]) >= 91 and ord(text[k]) <= 96) or ord(text[k]) >= 123)):
                    if ord(text[k]) < 48 or ord(text[k]) > 57:
                        ind = k
                        break
    dic1 = []
    count = []
    ans = []
    for i in range(len(dic)):
        if dic[i] not in dic1:
            dic1.append(dic[i])
            c = 0
            for g in range(i, len(dic)):
                if dic[g] == dic1[len(dic1) - 1]:
                    c += 1
            count.append(c)
            ans.append([dic1[len(dic1) - 1], c])
    d = dict(ans)



    return d


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    ans=[]
    for i in numbers:
        ans.append(pow(i, exp))
    return ans


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
    result=float(0)
    for i in operations:
        if i['category'] in special_category:
            result=result+int(i['amount'])*0.05
        else:
            result = result + int(i['amount']) * 0.01

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
    with open(f'{get_path_to_file()}', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        c=0
        ind=0
        arr=[]
        for row in spamreader:
            if c==0:
                for i in range(len(row)):
                    if row[i]==header:
                        ind=i
                        break
                c=1
            else:
                if row[ind] not in arr:
                    arr.append(row[ind])

    return len(arr)

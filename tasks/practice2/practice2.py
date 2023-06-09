from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
    return "Hello "+name


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    # пиши код здесь
    import random
    return round(random.uniform(100, 1000000), 2)


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    b = 1
    for i in range(1, len(phone_number)):
        if (phone_number[i] > '9' or phone_number[i] < '0'):
            b = 0
    if (len(phone_number) == 12 and phone_number.startswith("+7") and b == 1):
        result = True
    else:
        result = False
    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    # пиши код здесь
    if (current_amount >= float(transfer_amount)):
        result = True
    else:
        result = False
    return result


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    # пиши код здесь
    import re
    text2 = text.strip()
    text = text.strip()
    text = text.lower()
    delimiters = "!|,|\"| |'|,|-|\\.|\\|"
    text = re.split(delimiters, text)
    s = ""
    delim = []
    while ('' in text):
        text.remove('')
    for i in range(len(text2)):
        if (text2[i] == ' ' or text2[i] == '\'' or text2[i] == '\" ' or text2[i] == '-' or text2[i] == '!'):
            delim.append(text2[i])
    for i in range(len(text)):

        if (text[i] in uncultured_words):
            text[i] = len(text[i]) * "#"
        s += text[i]
        if (i < len(delim) and delim[i] != '\'' and delim[i] != '\"'):
            s += delim[i]
    s = s.capitalize()
    return s


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:
    
    Иванов,Петр,Сергеевич,01.01.1991,10000
    
    Что должны вернуть на ее основе:
    
    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000
    
    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    # пиши код здесь
    user_info = user_info.split(',')
    surname = user_info[0]
    name = user_info[1]
    patronymic = user_info[2]
    date = user_info[3]
    sum = user_info[4]
    s = 'Фамилия: ' + surname + "\n" + 'Имя: ' + name + "\n" + 'Отчество: ' + patronymic + '\n' + 'Дата рождения: ' + date + '\n' + 'Запрошенная сумма: ' + sum
    return s

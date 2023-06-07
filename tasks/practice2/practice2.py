import random
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
    greeting = f'Hello, {name}!'
    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """
    amount = float("%.2f" % random.randint(100, 1000000))
    # пиши код здесь
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    result = False
    if phone_number.startswith("+7"):
        for i in range(2, len(phone_number)):
            if not phone_number[i].isdigit():
                return result
        return True
    else:
        return result

    # пиши код здесь


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
    result = True
    if current_amount >= float(transfer_amount):
        return result
    else:
        return False

    # пиши код здесь



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
    text = text.split()
    for i in range(len(text)):
        if i == 0:
            text[i] = text[i][0].upper() + text[i][1:].lower()
        else:
            text[i] = text[i].lower()
        for j in uncultured_words:
            if j in text[i]:
                text[i] = text[i].replace(j, "#"*len(j))
        if '"' in text[i]:
            text[i] = text[i].replace('"', '', 1)
        elif "'" in text[i]:
            text[i] = text[i].replace("'", '', 1)
        elif "\'" in text[i]:
            text[i] = text[i].replace("\'", '', 1)
    result = ""
    for i in range(len(text)):
        if i != len(text) - 1:
            result = result + text[i] + " "
        else:
            result = result + text[i]
    return result


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
    data = user_info.split(",")
    result = f'Фамилия: {data[0]}\nИмя: {data[1]}\nОтчество: {data[2]}\nДата рождения: {data[3]}\nЗапрошенная сумма: {data[4]}'
    # пиши код здесь
    return result

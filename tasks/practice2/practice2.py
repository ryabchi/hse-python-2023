import random
import re
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
    return "Hello," + name + "!"


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
    return float(f"{random.uniform(100, 1000000):.{2}f}")


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    if re.search(r"\+7\d{10}", phone_number):
        return True
    return False


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
    if current_amount >= float(transfer_amount):
        return True
    return False


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
    text = text.replace("'", '')
    text = text.replace('"', '')
    for i in uncultured_words:
        text = text.replace(i, '#' * len(i))
    text = text.split()
    text = ' '.join(text)
    text = text.capitalize()
    return text


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
    data = user_info.split(',')
    data[0] = "Фамилия: " + data[0]
    data[1] = "Имя: " + data[1]
    data[2] = "Отчество: " + data[2]
    data[3] = "Дата рождения: " + data[3]
    data[4] = "Запрошенная сумма: " + data[4]
    return "\n".join(data)

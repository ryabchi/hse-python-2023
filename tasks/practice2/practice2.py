from typing import Iterable, List

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: Username
    :type name: str
    :return: greeting
    """

    greeting: str = f"Hello, {name}!"
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
    from random import uniform

    RANGE: List[int, int] = [100, 1_000_000]
    DIGITS_COUNT: int = 2

    return round(uniform(*RANGE), DIGITS_COUNT)


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :type phone_number: str
    :return: булевское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    from re import fullmatch

    return bool(fullmatch(r'\+7\d{10}', phone_number))


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:

    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :type current_amount: float
    :param transfer_amount: сумма перевода
    :type transfer_amount: str
    :return: булевское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    return current_amount >= float(transfer_amount)


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствуют лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :type text: str
    :param uncultured_words: список запрещенных слов
    :type uncultured_words: Iterable[str]
    :return: текст, соответсвующий правилам
    """

    from re import sub

    result: str = ' '.join(text.split()).capitalize()
    result: str = sub(r'[\"\']', "", result)

    for word in uncultured_words:
        result: str = result.replace(word, len(word) * '#')

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
    :type user_info: str
    :return: текст кредитной заявки
    """
    from dataclasses import dataclass

    @dataclass
    class User:
        surname: str
        name: str
        patronymic: str
        birth_date: str
        loan_sum: str

        def format_str(self) -> str:
            return f'Фамилия: {self.surname}\n' \
                   f'Имя: {self.name}\n' \
                   f'Отчество: {self.patronymic}\n' \
                   f'Дата рождения: {self.birth_date}\n' \
                   f'Запрошенная сумма: {self.loan_sum}'


    return User(*user_info.split(',')).format_str()

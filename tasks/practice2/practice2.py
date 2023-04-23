import datetime
import random
import re
from string import Template
from typing import Iterable, Final
from dataclasses import dataclass

UNCULTURED_WORDS = ("kotleta", "pirog")


common_greeting = Template("Привет, друг, $name")
credit_order = Template(
    "Фамилия: $surname\n"
    "Имя: $name\n"
    "Отчество: $patronymic\n"
    "Дата рождения: $birthday\n"
    "Запрошенная сумма: $amount"
)


min_amount_number: Final = 100
max_amount_number: Final = 1000000

ru_phone_number_validator = re.compile("\\+7\\d{10}")


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """
    greeting = common_greeting.substitute(name=name)
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

    amount = round(random.uniform(min_amount_number, max_amount_number), 2)

    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """
    result = (
        True if ru_phone_number_validator.match(phone_number) is not None else False
    )
    # пиши код здесь
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

    return current_amount >= float(transfer_amount)


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
    result = text.strip().lower().capitalize().replace("'", "").replace('"', "")

    for word in uncultured_words:
        result = result.replace(word, "#" * len(word))

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

    order = parse_pure_order_string(user_info)
    result = order.to_text()

    return result


@dataclass
class CreditOrder:
    name: str
    surname: str
    patronymic: str
    birthday: datetime.datetime
    credit_amount: int

    def to_text(self):
        return credit_order.substitute(
            name=self.name,
            surname=self.surname,
            patronymic=self.patronymic,
            birthday=self.birthday.strftime("%d.%m.%Y"),
            amount=str(self.credit_amount),
        )


def parse_pure_order_string(user_info: str) -> CreditOrder:
    parsed = user_info.split(",")

    return CreditOrder(
        name=parsed[1],
        surname=parsed[0],
        patronymic=parsed[2],
        birthday=datetime.datetime.strptime(parsed[3], "%d.%m.%Y"),
        credit_amount=int(parsed[4]),
    )

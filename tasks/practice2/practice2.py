from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = f"Hello, {name}" # пиши код здесь
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
    import random as r
    amount = r.uniform(100, 1000000)
    amount = float("{0:.2f}".format(amount))
    print(amount)
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

    result = True
    sh = 0
    if len(phone_number) != 12:
        result = False
        return result
    if phone_number[1] != "7":
        result = False
        return result
    for i in phone_number:
        sh += 1
        try:
            if i != "+":
                if 0 <= int(i) <= 9:
                    continue
                else:
                    result = False
                    break
            else:
                continue
        except:
            result = False
            break
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

    t = float(transfer_amount)
    if current_amount >= t:
        result = True
    else:
        result = False
    # пиши код здесь
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
    
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.split()
    text = " ".join(text)
    text = text[:1].upper() + text[1:].lower()
    t = text.split()
    for j in range(len(t)):
        for i in uncultured_words:
            if i in t[j]:
                another = ""
                for m in range(len(t[j])):
                    if t[j][m].isalpha():
                        another += "#"
                    else:
                        another += t[j][m]
                t[j] = another
    result = " ".join(t)
    # пиши код здесь
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

    user_info = user_info.split(",")
    result = (f"Фамилия: {user_info[0]}\n"
              f"Имя: {user_info[1]}\n"
              f"Отчество: {user_info[2]}\n"
              f"Дата рождения: {user_info[3]}\n"
              f"Запрошенная сумма: {user_info[4]}")
    # пиши код здесь
    return result

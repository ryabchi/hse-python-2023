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
    greeting=f'Привет, {name}!'
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

    # пиши код здесь
    import random
    amount=random.uniform(100, 1000000)
    amount=float("%.2f" % amount)
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    result = True
    numberss=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(phone_number)):
        if i==0 and phone_number[i]!='+':
            result = False
            break
        if i==1 and phone_number[i]!='7':
            result = False
            break
        elif i>0 and phone_number[i] not in numberss:
            result = False
            break
    if len(phone_number)!=len('+7xxxxxxxxxx'):
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
    if current_amount>=float(transfer_amount):
        result=True
    else:
        result=False
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
    text=text.split()
    ans = str
    newtext = []
    for i in range(len(text)):
        if i == 0:
            ans = (text[i])[0].upper()
            ans = ans + (text[i])[1:].lower()
            newtext.append(ans)
        else:
            newtext.append(text[i].lower())
    ans = ''
    for i in newtext:
        if i[:len(i) - 1] in uncultured_words:
            for k in uncultured_words:
                if i[:len(i) - 1] == k:
                    for h in range(len(k)):
                        ans += '#'
                    ans += i[len(i) - 1]
            ans += ' '
        elif i not in uncultured_words:
            for g in range(len(i)):
                if ord(i[g]) != 34 and ord(i[g]) != 39 and ord(i[g]) != 92:
                    ans += i[g]
            ans += ' '
        else:
            for k in uncultured_words:
                if i == k:
                    for h in range(len(k)):
                        ans += '#'
            ans += ' '

    result=ans[:len(ans) - 1]
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

    # пиши код здесь
    st=user_info.split(',')
    result=(f'Фамилия: {st[0]}\nИмя: {st[1]}\nОтчество: {st[2]}\nДата рождения: {st[3]}\nЗапрошенная сумма: {st[4]}')
    return result

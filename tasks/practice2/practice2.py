from typing import Iterable
import random

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:

    return "Привет, {}!".format(name)


def get_amount() -> float:

    return round(random.uniform(100,1000001),2)


def is_phone_correct(phone_number: str) -> bool:

    return phone_number[:2]=="+7" and phone_number[2:].isdigit()


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:

    return current_amount >= float(transfer_amount)


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:

    text=text.lower()

    text=' '.join(text.split())

    text=text.replace('"','').replace("'",'')

    for word in uncultured_words:
        text=text.replace(word,'#'*len(word))

    text=text.capitalize()

    return text


def create_request_for_loan(user_info: str) -> str:

    user_info=user_info.split(",")

    result='Фамилия: {}\n'.format(user_info[0])
    result+='Имя: {}\n'.format(user_info[1])
    result+='Отчество: {}\n'.format(user_info[2])
    result+='Дата рождения: {}\n'.format(user_info[3])
    result+='Запрошенная сумма: {}'.format(user_info[4])
    


    return result

from typing import Any, Optional

def list_(l: Any, name: str) -> Optional[str]:
    for el in l:
        if isinstance(el, list):
            result = list_(el, name)
            if not (result is None):
                return result
        elif isinstance(el, dict):
            result = dict_(el, name)
            if not (result is None):
                return result
    return None


def dict_(d: Any, name: str) -> Optional[str]:
    if 'name' in d.keys() and 'phone' in d.keys():
        if d['name'] == name:
            return d['phone']
    else:
        result = list_(d.values(), name)
        if not (result is None):
            return result
    return None

def search_phone(content: Any, name: str) -> Optional[str]:
    """
    Функция поиска номера телефона пользователя в структуре данных.

    Алгоритм работы следующий:
    1) принимаем на вход структуру content, состоящую из словарей,
    списков и строковых ключей в списке
    2) внутри структуры может быть запись следующего формата:
    {
        'name': 'user_name',
        'phone': 'user_phone',
    }

    3) необходимо пройтись по всей структуре
    4) если встречаем словарь, в котором ключ name совпадает с
    аргументом функции name - берем из этого словаря поле phone
    и возвращаем этот телефон из функции
    5) если поле name с таким значением не найдено - возвращаем из
    функции None

    Может пригодиться:

    1) Чтобы проверить, является ли объект списком используйте функцию:
    isinstance(some_object, list)
    если some_object список - результат будет True
    если some_object не список - False

    2) Чтобы проверить, является ли объект словарем используйте функцию:
    isinstance(some_object, dict)


    :param content: словарь или список, внутрь которого вложены объекты. Внутри
                      может скрываться номер телефона пользователя
    :param name: имя пользователя, у которого будем искать номер телефона
    :return: номер телефона пользователя или None
    """

    result = None
    if isinstance(content, dict):
        result = dict_(content, name)
    elif isinstance(content, list):
        result = list_(content, name)

    return result

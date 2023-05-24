from typing import Any, Optional


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

    # пиши свой код здесь

    return find_by_recursion(content, name)


def find_by_recursion(structure: Any, name: str):
    if isinstance(structure, dict):
        try:
            if structure['name'] == name:
                return structure['phone']
            else:
                pass
        except KeyError:
            pass

        for key, value in structure.items():
            returned = find_by_recursion(value, name)
            if returned is not None:
                return returned

    elif structure is not None:
        for elem in structure:
            if isinstance(elem, dict) or isinstance(elem, tuple) or isinstance(elem, list):
                returned = find_by_recursion(elem, name)
                if returned is not None:
                    return returned

    return None


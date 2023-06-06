from typing import Any, Optional

res: Any
def find_in_dict(dct:dict, name:str):
    is_name_find=False
    for key in dct:
        if (key == 'name' and dct['name'] == name):
            is_name_find = True
        if (is_name_find and key == 'phone'):
            res = dct['phone']
            return res
        if (isinstance(dct[key], list)):
            res = find_in_list(dct[key], name)
            if (res!=None):
                return res
        if (isinstance(dct[key], dict)):
            res = find_in_dict(dct[key], name)
            if (res!=None):
                return res
    return None
def find_in_list(lst:list, name:str):
    for obj in lst:
        if (isinstance(obj, dict)):
            res = find_in_dict(obj, name)
            if (res!=None):
                return res
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

    if (isinstance(content, list)):
        return find_in_list(content, name)
    if (isinstance(content, dict)):
        return find_in_dict(content, name)
    return None

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
    
    print(content)
    temp = None
    phonenumber = None
    for i in content:
        if isinstance(i, list):
            ph = search_phone(i,name)
        if isinstance(content, dict):
            temp = content.get('name') == name
            if temp:
                phonenumber = content.get('phone')
            if isinstance(content[i], dict):
                temp = content[i].get('name')
                if temp:
                    phonenumber = content[i].get('phone')
            if isinstance(content[i], list):
                phonenumber = search_phone(content[i], name)
        if isinstance(i, dict):
            temp = i.get('name') == name
            if temp:
                phonenumber = i.get('phone')
            else:
                phonenumber = search_phone(i, name)

    return phonenumber

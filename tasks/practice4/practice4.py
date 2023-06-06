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
    def iterate_nested_struct(nested_struct, type):
        if type == dict:
            for key in nested_struct:
                if key == "name" and "phone" in nested_struct and nested_struct[key] == name:
                    return nested_struct["phone"]
                if isinstance(nested_struct[key], dict) or isinstance(nested_struct[key], list):
                    result = iterate_nested_struct(nested_struct[key], dict if isinstance(nested_struct[key], dict) else list)
                    if result is not None:
                        return result

        elif type == list:
            for item in nested_struct:
                if isinstance(item, dict) or isinstance(item, list):
                    result = iterate_nested_struct(item, dict if isinstance(item, dict) else list)
                    if result is not None:
                        return result

        return None


    return iterate_nested_struct(content, dict if isinstance(content, dict) else list)
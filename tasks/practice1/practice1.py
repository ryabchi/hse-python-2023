def concatenate_strings(a: str, b: str) -> str:
    """
    Функция для сложения двух строк.
    Результат сложения запишите в переменную result.
    :param a: первая строка
    :param b: вторая строка
    :return: результат сложения
    """
    result = a + b
    return result


def calculate_salary(total_compensation: int) -> float:
    """
    Функция расчета зарплаты, которую сотрудник получит после
    вычета налогов. Ставка налогообложения равна 13%.
    :param total_compensation: сумма зарплаты до вычета налога
    :return: сумма заплаты после вычета налога
    """
    tax_rate = 0.13  # ставка налога
    tax_amount = total_compensation * tax_rate  # сумма налога
    salary = total_compensation - tax_amount  # зарплата после вычета налога
    return salary
    # пиши свой код здесь

    return result

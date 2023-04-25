def concatenate_strings(a: str, b: str) -> str:

    """
    Функция для сложения двух строк.
    Результат сложения запишите в переменную result.

    :param a: String
    :type a: str
    :param b: String
    :type b: str

    :return: concatenation result
    """

    result: str = a + b
    return result


def calculate_salary(total_compensation: int) -> float:

    """
    Функция расчета зарплаты, которую сотрудник получит после
    вычета налогов. Ставка налогообложения равна 13%.

    :param total_compensation: salary before tax
    :type total_compensation: int
    :return: salary after tax
    """

    TAX: float = 0.13
    return total_compensation * (1 - TAX)

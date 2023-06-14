{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ba14f46",
   "metadata": {},
   "outputs": [],
   "source": [
    "def concatenate_strings(a: str, b: str) -> str:\n",
    "    \"\"\"\n",
    "    Функция для сложения двух строк.\n",
    "    Результат сложения запишите в переменную result.\n",
    "\n",
    "    :param a: строка\n",
    "    :param b: строка\n",
    "    :return: результат сложения\n",
    "    \"\"\"\n",
    "\n",
    "    result = a + b\n",
    "    return result\n",
    "\n",
    "\n",
    "def calculate_salary(total_compensation: int) -> float:\n",
    "    \"\"\"\n",
    "    Функция расчета зарплаты, которую сотрудник получит после\n",
    "    вычета налогов. Ставка налогообложения равна 13%.\n",
    "\n",
    "    :param total_compensation: сумма зарплаты до вычета налога\n",
    "    :return: сумма заплаты после вычета налога\n",
    "    \"\"\"\n",
    "\n",
    "    result = total_compensation * (1 - 0.13)\n",
    "    return result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

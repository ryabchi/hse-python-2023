{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6f77414",
   "metadata": {},
   "outputs": [],
   "source": [
    "from typing import Any, Optional\n",
    "\n",
    "\n",
    "def search_phone(content: Any, name: str) -> Optional[str]:\n",
    "    \"\"\"\n",
    "    Функция поиска номера телефона пользователя в структуре данных.\n",
    "\n",
    "    Алгоритм работы следующий:\n",
    "    1) принимаем на вход структуру content, состоящую из словарей,\n",
    "    списков и строковых ключей в списке\n",
    "    2) внутри структуры может быть запись следующего формата:\n",
    "    {\n",
    "        'name': 'user_name',\n",
    "        'phone': 'user_phone',\n",
    "    }\n",
    "\n",
    "    3) необходимо пройтись по всей структуре\n",
    "    4) если встречаем словарь, в котором ключ name совпадает с\n",
    "    аргументом функции name - берем из этого словаря поле phone\n",
    "    и возвращаем этот телефон из функции\n",
    "    5) если поле name с таким значением не найдено - возвращаем из\n",
    "    функции None\n",
    "\n",
    "    Может пригодиться:\n",
    "\n",
    "    1) Чтобы проверить, является ли объект списком используйте функцию:\n",
    "    isinstance(some_object, list)\n",
    "    если some_object список - результат будет True\n",
    "    если some_object не список - False\n",
    "\n",
    "    2) Чтобы проверить, является ли объект словарем используйте функцию:\n",
    "    isinstance(some_object, dict)\n",
    "\n",
    "\n",
    "    :param content: словарь или список, внутрь которого вложены объекты. Внутри\n",
    "                      может скрываться номер телефона пользователя\n",
    "    :param name: имя пользователя, у которого будем искать номер телефона\n",
    "    :return: номер телефона пользователя или None\n",
    "    \"\"\"\n",
    "\n",
    "    if isinstance(content, dict):\n",
    "        if 'name' in content and content['name'] == name and 'phone' in content:\n",
    "            return content['phone']\n",
    "        else:\n",
    "            for value in content.values():\n",
    "                result = search_phone(value, name)\n",
    "                if result:\n",
    "                    return result\n",
    "    elif isinstance(content, list):\n",
    "        for item in content:\n",
    "            result = search_phone(item, name)\n",
    "            if result:\n",
    "                return result\n",
    "\n",
    "    return None"
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

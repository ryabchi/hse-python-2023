from typing import Set
from .employee import Employee, Manager
from .exception import NoSuchMemberError
import copy

class Team:
    """
    Класс - команда.
    У каждой команды есть менеджер, название и участники.

    Возможности:
    - добавление участников
    - удаление участника из команды
    - просмотр базовой информации об участниках
    - получение списка участников
    """

    name: str
    manager: Manager
    __members: Set[Employee]

    def __init__(self, name: str, manager: Manager):
        """
        Задача:
        Реализовать конструктор класса.
        Конструктор должен присвоить значения публичным атрибутам
        и инициализировать контейнер `__members`
        """

        # пиши свой код здесь
        self.name = name
        self.manager = manager
        self.__members = set()

    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        Пример вывода: 'name: Ivan position manager'
        """

        # пиши свой код здесь
        return "team: {team_name} manager: {manager_name} number of members: {members_count}".format(team_name = self.name, manager_name = self.manager.name, members_count = len(self.get_members()))

    def add_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод добавления участника в команду.
        Добавить можно только работника.
        """
        if not isinstance(member, Employee):
            raise TypeError

        # пиши свой код здесь
        if not isinstance(member, Employee):
            raise TypeError

        self.__members.add(member)

    def remove_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод удаления участника из команды.
        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`
        """

        # пиши свой код здесь
        if not isinstance(member, Employee):
            raise TypeError

        try:
            self.__members.remove(member)
        except KeyError:
            raise NoSuchMemberError(self.name, member)

    def get_members(self) -> Set[Employee]:
        """
        Задача: реализовать метод возвращения списка участков команды та,
        чтобы из вне нельзя было поменять список участников внутри класса
        """

        # пиши свой код здесь
        return copy.copy(self.__members)

    def show(self) -> None:
        """
        DO NOT EDIT!
        Данный метод нельзя редактировать!

        Метод показывает информацию о команде в формате:
        `'team: {team_name} manager: {manager_name} number of members: {members_count)}'`

        Задача: доработать класс таким образом, чтобы метод выполнял свою функцию, не меняя содержимое
        этого метода
        """
        print(self)

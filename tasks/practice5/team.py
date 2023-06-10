from typing import Set
from .employee import Employee, Manager
from .exception import NoSuchMemberError


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
        acceptable_init = isinstance(name, str) and isinstance(manager, Manager)
        if acceptable_init:
            self.name, self.manager, self.__members = name, manager, set()
        else: raise TypeError

        # пиши свой код здесь

    def add_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод добавления участника в команду.
        Добавить можно только работника.
        """
        acceptable_init = isinstance(member,Employee)
        if acceptable_init:
            self.__members.add(member)
        else: raise TypeError
        # пиши свой код здесь

    def remove_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод удаления участника из команды.
        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`
        """
        acceptable_init = isinstance(member, Employee)
        if acceptable_init:
            try:
                self.__members.remove(member)
            except KeyError:
                raise NoSuchMemberError(self.name, member)
        else: raise TypeError

    def get_members(self) -> Set[Employee]:
        """
        Задача: реализовать метод возвращения списка участков команды та,
        чтобы из вне нельзя было поменять список участников внутри класса
        """

        return set(self.__members)

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

    def __str__(self):
        return f'team: {self.name} manager: {self.manager.name} number of members: {len(self.__members)}'

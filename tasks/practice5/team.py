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

        self.name = name
        self.manager = manager
        self.__members=set()


    def add_member(self, member: Employee) -> None:

        if type(member) != Employee and not issubclass(type(member),Employee):
            raise TypeError()

        self.__members.add(member)

    def remove_member(self, member: Employee) -> None:

        if type(member) != Employee and not issubclass(type(member),Employee):
            raise TypeError()

        if member in self.__members:
            self.__members.remove(member)
        else:
            raise NoSuchMemberError(self.name, member)

    def get_members(self) -> Set[Employee]:
        return self.__members.copy()

    def __str__(self):
        return f"team: {self.name} manager: {self.manager.name} number of members: {len(self.__members)}"

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

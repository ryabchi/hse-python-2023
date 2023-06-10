from typing import Dict
from .exception import NoSuchPositionError

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}


def get_position_level(position_name: str) -> int:
    try:
        return POSITIONS[position_name]
    except KeyError:
        raise NoSuchPositionError(position_name)


class Employee:
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        if type(name) is not str:
            raise ValueError()
        if type(position) is not str:
            raise ValueError()
        if type(salary) is not int:
            raise ValueError()
        self.name = name
        self.position = position
        self._salary = salary

    def get_salary(self) -> int:
        return self._salary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            raise TypeError()
        try:
            return get_position_level(self.position) == get_position_level(other.position)
        except NoSuchPositionError as e:
            raise ValueError(f"position ${e.position} does not exist")

    def __str__(self):
        return f'name: {self.name} position: {self.position}'

    def __hash__(self):
        return id(self)


class Developer(Employee):
    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        super().__init__(name, self.position, salary)
        self.language = language


class Manager(Employee):
    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        super().__init__(name, self.position, salary)

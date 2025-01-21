import itertools
from enum import Enum

DEFAULT_STUDENTS = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
)


class Plant(Enum):
    GRASS = "G"
    CLOVER = "C"
    RADISHES = "R"
    VIOLETS = "V"


class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagram = diagram
        self.students = students

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        self._students = sorted(students)

    def plants(self, students):
        student_index = self.students.index(students)
        return [
            Plant(symbol).name.capitalize()
            for symbol in itertools.chain.from_iterable(
                row[2 * student_index : 2 * student_index + 2]
                for row in self.diagram.split("\n")
            )
        ]

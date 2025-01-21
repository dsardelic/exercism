import itertools
from collections import defaultdict


class School:
    def __init__(self):
        self._names_per_grade = defaultdict(set)
        self._added = []

    def add_student(self, name, grade):
        if name in self.roster():
            self._added.append(False)
        else:
            self._names_per_grade[grade].add(name)
            self._added.append(True)

    def roster(self):
        return list(
            itertools.chain.from_iterable(
                self.grade(grade) for grade in sorted(self._names_per_grade)
            )
        )

    def grade(self, grade_number):
        return sorted(self._names_per_grade[grade_number])

    def added(self):
        return list(self._added)

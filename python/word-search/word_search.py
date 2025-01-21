from dataclasses import dataclass


class Vector(tuple):
    def multiply_by(self, scalar):
        return Vector(self[i] * scalar for i in range(len(self)))


@dataclass
class Point:
    x: int
    y: int

    def translate(self, vector):
        return self.__class__(self.x + vector[0], self.y + vector[1])

    def reverse(self):
        return self.__class__(self.y, self.x)


class WordSearch:
    vectors = (
        Vector((-1, -1)),
        Vector((-1, 0)),
        Vector((-1, 1)),
        Vector((0, -1)),
        Vector((0, 1)),
        Vector((1, -1)),
        Vector((1, 0)),
        Vector((1, 1)),
    )

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        try:
            return next(
                (
                    Point(x, y).reverse(),
                    Point(x, y).translate(vector.multiply_by(len(word) - 1)).reverse(),
                )
                for x in range(len(self.puzzle))
                for y in range(len(self.puzzle[0]))
                for vector in self.vectors
                if self.puzzle_slice(Point(x, y), vector, len(word)) == word
            )
        except StopIteration:
            return None

    def puzzle_slice(self, point, vector, length):
        return "".join(
            self.puzzle_element_at(slice_point)
            for i in range(length)
            if (slice_point := point.translate(vector.multiply_by(i)))
            and self.within_puzzle(slice_point)
        )

    def puzzle_element_at(self, point):
        return self.puzzle[point.x][point.y]

    def within_puzzle(self, point):
        return 0 <= point.x < len(self.puzzle) and 0 <= point.y < len(self.puzzle[0])

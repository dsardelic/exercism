import itertools


def spiral_matrix(size):
    def is_available(x, y):
        return 0 <= x < size and 0 <= y < size and not matrix[x][y]

    if not size:
        return []
    matrix = [[None] * size for _ in range(size)]
    offsets = itertools.cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    number = 1
    x, y = 0, 0
    offset_x, offset_y = next(offsets)
    while True:
        matrix[x][y] = number
        number += 1
        if is_available(x + offset_x, y + offset_y):
            x, y = x + offset_x, y + offset_y
        else:
            offset_x, offset_y = next(offsets)
            if is_available(x + offset_x, y + offset_y):
                x, y = x + offset_x, y + offset_y
            else:
                return matrix

import itertools


def rectangles(strings):
    return sum(
        is_valid_rectangle(
            top_left_x, top_left_y, bottom_right_x, bottom_right_y, strings
        )
        for (
            (top_left_x, top_left_y),
            (bottom_right_x, bottom_right_y),
        ) in itertools.combinations(coordinates_of("+", strings), 2)
    )


def coordinates_of(char, strings):
    return [
        (x, y)
        for x, row in enumerate(strings)
        for y, string_char in enumerate(row)
        if string_char == char
    ]


def horizontal_side(x, y_from, y_to, strings):
    return strings[x][y_from : y_to + 1]


def vertical_side(y, x_from, x_to, strings):
    return [row[y] for row in strings[x_from : x_to + 1]]


def is_valid_horizontal_side(side):
    return all(char in {"+", "-"} for char in side)


def is_valid_vertical_side(side):
    return all(char in {"+", "|"} for char in side)


def is_valid_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, strings):
    if top_left_x >= bottom_right_x or top_left_y >= bottom_right_y:
        return False
    return all(
        is_valid_horizontal_side(side)
        for side in (
            horizontal_side(top_left_x, top_left_y, bottom_right_y, strings),
            horizontal_side(bottom_right_x, top_left_y, bottom_right_y, strings),
        )
    ) and all(
        is_valid_vertical_side(side)
        for side in (
            vertical_side(top_left_y, top_left_x, bottom_right_x, strings),
            vertical_side(bottom_right_y, top_left_x, bottom_right_x, strings),
        )
    )

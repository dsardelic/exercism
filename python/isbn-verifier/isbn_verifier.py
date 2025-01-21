import re


def is_valid(isbn):
    if not (
        isinstance(isbn, str) and isbn and re.fullmatch(r"^[0-9][0-9X\-]{9,}$", isbn)
    ):
        return False
    if len(isbn := isbn.replace("-", "")) > 10:
        return False
    if "X" in isbn[: len(isbn) - 1]:
        return False
    return (
        not sum(
            (10 if digit == "X" else int(digit)) * multiplier
            for digit, multiplier in zip(isbn, range(10, 0, -1))
        )
        % 11
    )

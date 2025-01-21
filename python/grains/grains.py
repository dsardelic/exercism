from functools import lru_cache


@lru_cache(maxsize=64)
def square(number):
    if not isinstance(number, int) or (not 1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)


def total():
    return sum(square(i) for i in range(1, 65))

import itertools
import math


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors = set(
        itertools.chain.from_iterable(
            (
                (x, number // x)
                for x in range(1, math.isqrt(number) + 1)
                if not number % x
            )
        )
    ) - {number}

    sum_of_factors = sum(factors)

    if number < sum_of_factors:
        return "abundant"

    if number > sum_of_factors:
        return "deficient"

    return "perfect"

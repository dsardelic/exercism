import math


def largest(*, min_factor=0, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    max_product = -float("inf")
    factors = []
    j_stop_value = min_factor - 1
    for j in range(max_factor, min_factor - 1, -1):
        if j <= j_stop_value:
            break
        for i in range(j, min_factor - 1, -1):
            if max_product != -float("inf") and i < max_product / j:
                break
            product = i * j
            if is_palindrome(product) and product >= max_product:
                if product == max_product:
                    factors.append([i, j])
                else:
                    factors = [[i, j]]
                max_product = max(max_product, product)
                j_stop_value = math.isqrt(product) - 1
    return (max_product if max_product > -float("inf") else None), factors


def smallest(*, min_factor=0, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    min_product = float("inf")
    factors = []
    i_stop_value = max_factor + 1
    for i in range(min_factor, max_factor + 1):
        if i >= i_stop_value:
            break
        for j in range(i, max_factor + 1):
            if min_product != float("inf") and j > min_product / i:
                break
            product = i * j
            if is_palindrome(product) and product <= min_product:
                if product == min_product:
                    factors.append([i, j])
                else:
                    factors = [[i, j]]
                min_product = min(min_product, product)
                i_stop_value = math.isqrt(product) + 1
    return (min_product if min_product < float("inf") else None), factors


def is_palindrome(number):
    number_str = str(number)
    return all(
        number_str[i] == number_str[-(i + 1)] for i in range(len(number_str) // 2)
    )

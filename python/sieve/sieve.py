import math


def primes(limit):
    A = [False, False] + [True] * (limit - 1)
    for i in range(2, math.isqrt(limit) + 1):
        if A[i]:
            n = 0
            while (j := i**2 + n * i) <= limit:
                A[j] = False
                n += 1
    return [i for i, is_prime in enumerate(A) if is_prime]

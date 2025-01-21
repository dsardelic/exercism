def triplets_with_sum(number):
    return [
        [a, b, number - (a + b)]
        for a in range(1, number // 3 + 1)
        for b in range(a, (number - a) // 2 + 1)
        if a**2 + b**2 == (number - (a + b)) ** 2
    ]

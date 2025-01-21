def fact(number):
    if number <= 1:
        return 1
    return number * fact(number - 1)


def bin_coef(m, k):  # m choose k
    numerator = 1
    for factor in range(0, k):
        numerator = numerator * (m - factor)
    denominator = fact(k)
    coef = numerator / denominator
    return coef


def taylor(num):
    exp = len(str(num))
    x = (num / (10**exp)) - 1
    sum_ = 0
    for term in range(100):
        sum_ += bin_coef(1 / 2, term) * (x**term)
    result = (
        sum_ * 3.16227766017 * (10 ** ((exp - 1) / 2))
        if exp % 2
        else sum_ * (10 ** (exp / 2))
    )
    return round(result, 3)


def square_root(number):
    return taylor(number)


print(taylor(81))

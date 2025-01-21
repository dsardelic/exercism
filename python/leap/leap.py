def divisible_by(year, number):
    return not year % number


def leap_year(year):
    match divisible_by(year, 4), divisible_by(year, 100), divisible_by(year, 400):
        case _, _, True:
            return True
        case _, True, False:
            return False
        case True, _, _:
            return True
        case False, _, _:
            return False

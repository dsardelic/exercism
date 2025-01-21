def is_armstrong_number(number):
    if not number:
        return True
    return number == sum(pow(int(digit), len(str(number))) for digit in str(number))

SINGLE_DIGITS = (
    "",  # 'zero' will be printed as a standalone number only
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)

FIRST_TWENTY_NUMBERS = SINGLE_DIGITS + (
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
)

MULTIPLES_OF_TEN = (
    "",  # won't be used
    "ten",  # won't be used either
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
)

POWERS_OF_1000 = tuple(1000**power for power in range(4))
POWERS_OF_1000_NAMES = ("", "thousand", "million", "billion")
assert len(POWERS_OF_1000_NAMES) >= len(POWERS_OF_1000)


def say(number):
    def say_power_and_multiplier(number, power, name_accumulator):
        if power < 0:
            return name_accumulator.strip()
        multiplier_name = say_number_below_1000(
            number % (1000 ** (power + 1)) // (1000**power)
        )
        name_accumulator += (
            " " + (multiplier_name + " " + POWERS_OF_1000_NAMES[power]).strip()
            if multiplier_name
            else ""
        )
        return say_power_and_multiplier(number, power - 1, name_accumulator)

    if not isinstance(number, int):
        raise ValueError("expected int, received " + type(number))
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")
    if not number:
        return "zero"
    return say_power_and_multiplier(number, len(POWERS_OF_1000), "")


def say_number_below_1000(number):
    assert 0 <= number < 1000
    return (
        f"{(SINGLE_DIGITS[number // 100] + ' hundred ') if number // 100 else ''}"
        f"{say_number_below_100(number % 100)}"
    ).strip()


def say_number_below_100(number):
    assert 0 <= number < 100
    if number < 21:
        return FIRST_TWENTY_NUMBERS[number]
    return "-".join((MULTIPLES_OF_TEN[number // 10], SINGLE_DIGITS[number % 10])).strip(
        "-"
    )

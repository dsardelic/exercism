import re
import string


class PhoneNumber:
    def __init__(self, number):
        self.number = self.validated_number(self.sanitize_number(number))

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    def sanitize_number(self, number):
        return re.sub(
            r"|".join([r" ", r"\+", r"\-", r"\(", r"\)", r"\."]), "", number.strip()
        )

    def validated_number(self, number):
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(number) == 11:
            if number[0] == "1":
                number = number[1:]
            else:
                raise ValueError("11 digits must start with 1")

        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        if number[0] == "0":
            raise ValueError("area code cannot start with zero")

        if number[0] == "1":
            raise ValueError("area code cannot start with one")

        if any(char in number for char in string.punctuation):
            raise ValueError("punctuations not permitted")

        if any(char in string.ascii_lowercase for char in number.lower()):
            raise ValueError("letters not permitted")

        return number

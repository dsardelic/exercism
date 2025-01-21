import re


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        despaced_card_num = self.card_num.replace(" ", "")
        if not re.fullmatch(r"[0-9 ]{2,}", despaced_card_num):
            return False
        return not (
            sum(
                self.double(char) if i % 2 else int(char)
                for i, char in enumerate(reversed(despaced_card_num))
            )
            % 10
        )

    @staticmethod
    def double(char):
        return doubled if (doubled := int(char) * 2) < 10 else doubled - 9

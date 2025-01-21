import itertools
import random
import string


class Cipher:
    def __init__(self, key=None):
        self.key = key if key else self.generate_key()

    def encode(self, text):
        return "".join(
            string.ascii_lowercase[
                (
                    string.ascii_lowercase.index(text_char)
                    + string.ascii_lowercase.index(key_char)
                )
                % len(string.ascii_lowercase)
            ]
            for text_char, key_char in zip(text, itertools.cycle(self.key))
        )

    def decode(self, text):
        return "".join(
            string.ascii_lowercase[
                string.ascii_lowercase.index(text_char)
                - string.ascii_lowercase.index(key_char)
            ]
            for text_char, key_char in zip(text, itertools.cycle(self.key))
        )

    @staticmethod
    def generate_key():
        random.seed()
        return "".join(random.choice(string.ascii_lowercase) for _ in range(100))

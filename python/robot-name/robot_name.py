import random


class Robot:
    def __init__(self):
        self.name = self.generate_name()

    @staticmethod
    def generate_name():
        random.seed()
        return "".join(
            (
                *(chr(random.randint(ord("A"), ord("Z"))) for _ in range(2)),
                *(chr(random.randint(ord("0"), ord("9"))) for _ in range(3)),
            )
        )

    def reset(self):
        self.name = self.generate_name()

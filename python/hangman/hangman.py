STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.previous_guesses = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if char not in self.word or char in self.previous_guesses:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:  # huh??? negative remaining guesses?
                self.status = STATUS_LOSE
                return
        self.previous_guesses.add(char)
        if self.previous_guesses.issuperset(set(self.word)):
            self.status = STATUS_WIN

    def get_masked_word(self):
        return "".join(
            (char if char in self.previous_guesses else "_") for char in self.word
        )

    def get_status(self):
        return self.status

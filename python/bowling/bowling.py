class Frame:
    def __init__(self, rank):
        self.rank = rank
        self.rolls = None
        self.score = None

    def set_rolls(self, rolls):
        self.rolls = rolls
        for roll in rolls:
            roll.frames.append(self)

    def calculate_score(self):
        match [roll.pins for roll in self.rolls]:
            # frames 1-8, turkey
            case 10, None, 10, None, 10:
                self.score = 30

            # frames 1-8, double
            case 10, None, 10, None, pins5 if pins5 is not None:
                self.score = 20 + pins5

            # frames 1-8, strike
            case 10, None, pins3, pins4, _ if all(
                item is not None for item in (pins3, pins4)
            ):
                self.score = 10 + pins3 + pins4

            # frames 1-8, spare
            case pins1, pins2, pins3, _, _ if all(
                item is not None for item in (pins1, pins2, pins3)
            ) and pins1 + pins2 == 10:
                self.score = 10 + pins3

            # frames 1-8, open frame
            case pins1, pins2, _, _, _ if all(
                item is not None for item in (pins1, pins2)
            ):
                if (score := pins1 + pins2) > 10:
                    raise ValueError("More than 10 points in 2 consecutive frame rolls")
                self.score = pins1 + pins2

            # frame 9, strike
            case 10, None, pins_9_1, pins_9_2 if all(
                item is not None for item in (pins_9_1, pins_9_2)
            ):
                self.score = 10 + pins_9_1 + pins_9_2

            # frame 9, spare
            case pins_9_1, pins_9_2, pins_10_1, _ if all(
                item is not None for item in (pins_9_1, pins_9_2, pins_10_1)
            ) and pins_9_1 + pins_9_2 == 10:
                self.score = 10 + pins_10_1

            # frame 9, open frame
            case pins_9_1, pins_9_2, _, _ if all(
                item is not None for item in (pins_9_1, pins_9_2)
            ):
                if (score := pins_9_1 + pins_9_2) > 10:
                    raise ValueError("More than 10 points in 2 consecutive frame rolls")
                self.score = score

            # frame 10, no strike in 1st roll nor spare in first 2 rolls
            case pins_10_1, pins_10_2, None if all(
                item is not None for item in (pins_10_1, pins_10_2)
            ) and pins_10_1 < 10:
                if (score := pins_10_1 + pins_10_2) > 10:
                    raise ValueError("More than 10 points in 2 consecutive frame rolls")
                if score < 10:
                    self.score = score

            # frame 10, strike in 1st roll
            case 10, pins_10_2, pins_10_3 if all(
                item is not None for item in (pins_10_2, pins_10_3)
            ):
                if pins_10_2 == 10:
                    self.score = 20 + pins_10_3
                else:
                    if pins_10_2 + pins_10_3 > 10:
                        raise ValueError(
                            "More than 10 points in 2 consecutive frame rolls"
                        )
                    self.score = 10 + pins_10_2 + pins_10_3

            # frame 10, spare in first 2 rolls
            case pins_10_1, pins_10_2, pins_10_3 if all(
                item is not None for item in (pins_10_1, pins_10_2, pins_10_3)
            ) and pins_10_1 + pins_10_2 == 10:
                self.score = pins_10_1 + pins_10_2 + pins_10_3


class Roll:
    def __init__(self):
        self.frames = []
        self.pins = None

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == "pins":
            for frame in self.frames:
                frame.calculate_score()


class BowlingGame:
    def __init__(self):
        self.frames = [Frame(i + 1) for i in range(10)]
        self.rolls = self.init_rolls()
        self._roll_idx = 0

    def init_rolls(self):
        rolls = [Roll() for i in range(21)]
        for frame in self.frames:
            frame.set_rolls(rolls[(frame.rank - 1) * 2 : (frame.rank - 1) * 2 + 5])
        # the final bonus roll of the final frame does not impact the penultimate frame
        rolls[-1].frames.remove(self.frames[8])
        self.frames[8].rolls.remove(rolls[-1])
        return rolls

    def roll(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError(f"Invalid pin count: {pins}")
        if self.game_over:
            raise ValueError("Rolling after game over")
        self.rolls[self._roll_idx].pins = pins
        self._roll_idx += 1
        # skip other frame roll after strike, but not in the final frame
        if pins == 10 and self._roll_idx < 18:
            self._roll_idx += 1

    def score(self):
        if not self.game_over:
            raise ValueError("Game not over, additional roll(s) expected")
        return sum(frame.score for frame in self.frames)

    @property
    def game_over(self):
        return all(frame.score is not None for frame in self.frames)

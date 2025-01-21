class BowlingScorer:
    def __init__(self, frames):
        self.frames = frames
        self._points_per_frame = [None] * len(frames)

    @property
    def points_per_frame(self):
        while any(frame_score is None for frame_score in self._points_per_frame):
            self.score_frame(self._points_per_frame.index(None))
        return self._points_per_frame

    def score_frame(self, frame_idx):
        if frame_idx == 9:
            self.score_last_frame(frame_idx)
        elif sum(self.frames[frame_idx]) == 10:
            if len(self.frames[frame_idx]) == 1:
                strikes_in_a_row_count = self.consecutive_strikes_count(frame_idx)
                if strikes_in_a_row_count == 1:
                    self.score_strike(frame_idx)
                elif strikes_in_a_row_count == 2:
                    self.score_double(frame_idx)
                else:
                    self.score_n_strikes_in_a_row(frame_idx, strikes_in_a_row_count)
            elif len(self.frames[frame_idx]) == 2:
                self.score_spare(frame_idx)
        else:
            self.score_open_frame(frame_idx)

    def score_last_frame(self, frame_idx):
        self._points_per_frame[frame_idx] = sum(self.frames[frame_idx])

    def score_open_frame(self, frame_idx):
        self._points_per_frame[frame_idx] = sum(self.frames[frame_idx])

    def score_spare(self, frame_idx):
        self._points_per_frame[frame_idx] = 10 + self.frames[frame_idx + 1][0]

    def score_strike(self, frame_idx):
        self._points_per_frame[frame_idx] = 10 + sum(self.frames[frame_idx + 1][:2])

    def score_double(self, frame_idx):
        self._points_per_frame[frame_idx] = 20 + self.frames[frame_idx + 2][0]
        self.score_strike(frame_idx + 1)

    def score_n_strikes_in_a_row(self, frame_idx, n):
        if n == 2:
            self.score_double(frame_idx)
        else:
            self._points_per_frame[frame_idx] = 30
            self.score_n_strikes_in_a_row(frame_idx + 1, n - 1)

    def consecutive_strikes_count(self, frame_idx):
        # not counting the last frame
        count = 1
        frame_idx += 1
        while frame_idx < 9 and self.frames[frame_idx] == [10]:
            count += 1
            frame_idx += 1
        return count


class BowlingGame:
    def __init__(self):
        self.frames = [[] for _ in range(10)]
        self._frame_idx = 0
        self._fill_ball = False
        self._game_over = False

    def valid_pins(self, pins):
        def more_than_10_points_in_a_non_final_frame():
            return (
                self._frame_idx < 9
                and self.frames[self._frame_idx]
                and self.frames[self._frame_idx][0] + pins > 10
            )

        def more_than_10_points_in_the_final_frame_without_fill_ball():
            return (
                self._frame_idx == 9
                and len(self.frames[self._frame_idx]) == 1
                and self.frames[self._frame_idx][0]
                < 10
                < self.frames[self._frame_idx][0] + pins
            )

        def more_than_10_points_in_the_final_frame_with_fill_ball():
            return (
                self._frame_idx == 9
                and len(self.frames[self._frame_idx]) == 2
                and self.frames[self._frame_idx][0] == 10
                and self.frames[self._frame_idx][1]
                < 10
                < self.frames[self._frame_idx][1] + pins
            )

        if not 0 <= pins <= 10:
            raise ValueError(f"Invalid pin count: {pins}")
        if self._game_over:
            raise ValueError("Rolling after game over")
        if (
            more_than_10_points_in_a_non_final_frame()
            or more_than_10_points_in_the_final_frame_without_fill_ball()
            or more_than_10_points_in_the_final_frame_with_fill_ball()
        ):
            raise ValueError(
                "Invalid pin count: "
                "score of more than 10 points in 2 consecutive frame rolls"
            )
        return pins

    def roll(self, pins):
        pins = self.valid_pins(pins)
        self.frames[self._frame_idx].append(pins)
        if self._frame_idx == 9:
            if len(self.frames[self._frame_idx]) == 3:
                self._game_over = True
            if sum(self.frames[self._frame_idx]) == 10:
                self._fill_ball = True
            if len(self.frames[self._frame_idx]) == 2 and not self._fill_ball:
                self._game_over = True
        elif len(self.frames[self._frame_idx]) == 2 or pins == 10:
            self._frame_idx += 1

    def score(self):
        if not self._game_over:
            raise ValueError("Game not over, additional roll(s) expected")
        return sum(BowlingScorer(self.frames).points_per_frame)


if __name__ == "__main__":
    # sample_pins = [10, 9, 1, 5, 5, 7, 2, 10, 10, 10, 9, 0, 8, 2, 9, 1, 10]
    sample_pins = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = BowlingGame()
    for roll in sample_pins:
        game.roll(roll)
    print(game.frames)
    print(BowlingScorer(game.frames).points_per_frame)
    print(game.score())

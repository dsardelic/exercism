import itertools


class Scale:
    chromatic_a_sharp = [
        "A",
        "A#",
        "B",
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
    ]

    chromatic_a_flat = [
        "A",
        "Bb",
        "B",
        "C",
        "Db",
        "D",
        "Eb",
        "E",
        "F",
        "Gb",
        "G",
        "Ab",
    ]

    sharp_tonics = {
        "C",
        "a",
        "G",
        "D",
        "A",
        "E",
        "B",
        "F#",
        "e",
        "b",
        "f#",
        "c#",
        "g#",
        "d#",
    }

    flat_tonics = {
        "F",
        "Bb",
        "Eb",
        "Ab",
        "Db",
        "Gb",
        "d",
        "g",
        "c",
        "f",
        "bb",
        "eb",
    }

    interval_halfstep_mapping = {"m": 1, "M": 2, "A": 3}

    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        chromatic_a_scale = (
            self.chromatic_a_sharp
            if self.tonic in self.sharp_tonics
            else self.chromatic_a_flat
        )
        start_index = chromatic_a_scale.index(self.tonic.capitalize())
        return (chromatic_a_scale * 2)[start_index : start_index + 12]

    def interval(self, intervals):
        return [self.tonic.capitalize()] + [
            (self.chromatic() + [self.tonic.capitalize()])[offset]
            for offset in itertools.accumulate(
                self.interval_halfstep_mapping[interval] for interval in intervals
            )
        ]

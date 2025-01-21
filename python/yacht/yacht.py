import collections

# Score categories.
# Change the values as you see fit.
YACHT = object()
ONES = object()
TWOS = object()
THREES = object()
FOURS = object()
FIVES = object()
SIXES = object()
FULL_HOUSE = object()
FOUR_OF_A_KIND = object()
LITTLE_STRAIGHT = object()
BIG_STRAIGHT = object()
CHOICE = object()


def score(dice, category):
    counter = collections.Counter(dice)
    return {
        YACHT: 50 if 5 in counter.values() else 0,
        ONES: 1 * counter[1],
        TWOS: 2 * counter[2],
        THREES: 3 * counter[3],
        FOURS: 4 * counter[4],
        FIVES: 5 * counter[5],
        SIXES: 6 * counter[6],
        FULL_HOUSE: (
            sum(count * number for number, count in counter.items())
            if sorted(counter.values()) == [2, 3]
            else 0
        ),
        FOUR_OF_A_KIND: (
            sum(
                4 * number if count in {4, 5} else 0
                for number, count in counter.items()
            )
            if 4 in counter.values() or 5 in counter.values()
            else 0
        ),
        LITTLE_STRAIGHT: (
            30 if max(counter.values()) == 1 and 6 not in counter.keys() else 0
        ),
        BIG_STRAIGHT: (
            30 if max(counter.values()) == 1 and 1 not in counter.keys() else 0
        ),
        CHOICE: sum(dice),
    }[category]

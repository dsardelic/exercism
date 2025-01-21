import itertools


def solve(puzzle):
    addends, sum_ = puzzle.replace(" ", "").split("==")
    addends = addends.split("+")
    letters = sorted(set(puzzle) - set("+= "))
    for combination in itertools.combinations(list(range(10)), len(letters)):
        for digits in itertools.permutations(combination):
            translation = {
                ord(letter): str(digits[i]) for i, letter in enumerate(letters)
            }
            translated_addends = [addend.translate(translation) for addend in addends]
            translated_sum = sum_.translate(translation)
            if sum(int(addend) for addend in translated_addends) == int(
                translated_sum
            ) and all(
                number[0] != "0" for number in translated_addends + [translated_sum]
            ):
                return {letter: digits[i] for i, letter in enumerate(letters)}
    return None

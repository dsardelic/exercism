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
            translate(None, None, clear_cache=True)()
            # translated_addends = [addend.translate(translation) for addend in addends]
            translated_addends = [
                translate(addend, translation)() for addend in addends
            ]
            # translated_sum = sum_.translate(translation)
            translated_sum = translate(sum_, translation)()
            if sum(int(addend) for addend in translated_addends) == int(
                translated_sum
            ) and all(
                number[0] != "0" for number in translated_addends + [translated_sum]
            ):
                print(puzzle.translate(translation))
                return {letter: digits[i] for i, letter in enumerate(letters)}
    return None


def translate(word, translation, clear_cache=None):
    m = {}

    def memoiziraj():
        if clear_cache:
            m.clear()
            return
        if word not in m:
            m[word] = word.translate(translation)
        else:
            pass
        return m[word]

    return memoiziraj


if __name__ == "__main__":
    # solve("A + A + A + A + A + A + A + A + A + A + A + B == BCC")
    # solve("NO + NO + TOO == LATE")
    # solve("SEND + MORE == MONEY")
    solve("AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE")

import itertools


def combinations(target, size, exclude):
    return [
        list(combination)
        for combination in itertools.combinations(
            [n for n in range(1, 10) if n not in exclude], size
        )
        if sum(combination) == target
    ]

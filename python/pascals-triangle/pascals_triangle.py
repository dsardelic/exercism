# import functools
import itertools


def rows(row_count):
    # @functools.lru_cache
    def row(row_count):
        if not row_count:
            return [1]
        return [1, *(sum(pair) for pair in itertools.pairwise(row(row_count - 1))), 1]

    if row_count < 0:
        raise ValueError("number of rows is negative")
    return [row(row_count) for row_count in range(row_count)]

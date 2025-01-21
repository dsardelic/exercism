import functools
import itertools


def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    if not lists:
        return []
    return list(itertools.chain.from_iterable(lists))


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    return functools.reduce(function, list, initial)


def foldr(function, list, initial):
    return functools.reduce(function, reversed(list), initial)


def reverse(list):
    return list[::-1]

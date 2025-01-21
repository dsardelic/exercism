"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def element_indexes(element, some_list):
    return (i for i, elt in enumerate(some_list) if elt == element)


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if (not list_one) or (
        len(list_one) < len(list_two)
        and any(
            list_two[i : i + len(list_one)] == list_one
            for i in element_indexes(list_one[0], list_two)
        )
    ):
        return SUBLIST

    if (not list_two) or (
        len(list_one) > len(list_two)
        and any(
            list_one[i : i + len(list_two)] == list_two
            for i in element_indexes(list_two[0], list_one)
        )
    ):
        return SUPERLIST

    return UNEQUAL

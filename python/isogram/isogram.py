import collections
import string


def is_isogram(input_string):
    counter = collections.Counter(input_string.lower())
    return all(counter[char] <= 1 for char in counter if char in string.ascii_lowercase)

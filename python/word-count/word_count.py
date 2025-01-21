import collections
import re


def count_words(sentence):
    return collections.Counter(
        token.strip("'")
        for token in re.split(r"[^'\w]|_", sentence.lower())
        if token.strip("'")
    )

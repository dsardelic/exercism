import itertools
import re


def decode(string):
    return "".join(
        match[1] * (int(match[0]) if match[0] else 1)
        for match in re.findall(r"(\d*)([ A-Za-z])", string)
    )


def encode(string):
    return "".join(
        itertools.chain.from_iterable(
            (str(grouper_len) if (grouper_len := len(tuple(grouper))) > 1 else "", key)
            for key, grouper in itertools.groupby(string)
        )
    )

import itertools

FILL_VALUE = "\0"


def transpose(lines):
    return "\n".join(
        "".join(row).rstrip(FILL_VALUE).replace(FILL_VALUE, " ")
        for row in itertools.zip_longest(
            *(tuple(row) for row in lines.split("\n")),
            fillvalue=FILL_VALUE,
        )
    )

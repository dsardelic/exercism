from string import Template

NUMBERS = (
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
)

STANZA_TEMPLATE = Template(
    "$qty green bottle$plural hanging on the wall,\n"
    "$qty green bottle$plural hanging on the wall,\n"
    "And if one green bottle should accidentally fall,\n"
    "There'll be $new_qty green bottle$new_plural hanging on the wall.\n"
)


def recite(start, take=1):
    accumulator = []
    for qty in range(start, start - take, -1):
        plural = "" if qty == 1 else "s"
        new_plural = "" if qty == 2 else "s"
        accumulator = accumulator + STANZA_TEMPLATE.substitute(
            qty=NUMBERS[qty].capitalize(),
            new_qty=NUMBERS[qty - 1],
            plural=plural,
            new_plural=new_plural,
        ).split("\n")

    return accumulator[:-1]

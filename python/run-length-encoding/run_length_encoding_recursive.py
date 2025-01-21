import re


def decode(string):
    return "".join(
        match[1] * (int(match[0]) if match[0] else 1)
        for match in re.findall(r"(\d*)([ A-Za-z])", string)
    )


def encode(string):
    def accumulate(string, last, count, accumulator):
        if not string:
            return "".join(accumulator + [str(count) if count > 1 else "", last])
        head, *tail = string
        if head == last:
            return accumulate(tail, last, count + 1, accumulator)
        return accumulate(
            tail, head, 1, accumulator + [str(count) if count > 1 else "", last]
        )

    if not string:
        return ""
    if len(string) == 1:
        return string
    return accumulate(string[1:], string[0], 1, [])

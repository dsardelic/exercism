import math
import string


def cipher_text(plain_text):
    if not (plain_text and (normalized := normalize(plain_text))):
        return ""
    return " ".join("".join(word) for word in zip(*rectanglize(normalized)))


def normalize(text):
    return "".join(
        char for char in text.lower() if char not in string.punctuation + " "
    )


def rectanglize(text):
    r = math.isqrt(len(text))
    c = r if r * r >= len(text) else r + 1
    r = r if r * c >= len(text) else r + 1
    padded_text = text.ljust(r * c, " ")
    return [padded_text[i : i + c] for i in range(0, r * c, c)]

import math
import string


def encode(plain_text, a, b):
    m = len(string.ascii_lowercase)
    if math.gcd(a, m) > 1:
        raise ValueError("a and m must be coprime.")
    encoded_text = "".join(
        string.ascii_lowercase[(a * string.ascii_lowercase.index(char) + b) % m]
        if char in string.ascii_lowercase
        else char
        for char in "".join(
            char.lower()
            for char in plain_text.replace(" ", "")
            if char not in string.punctuation
        )
    )
    return " ".join(encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5))


def decode(ciphered_text, a, b):
    m = len(string.ascii_lowercase)
    if math.gcd(a, m) > 1:
        raise ValueError("a and m must be coprime.")
    for mmi in range(m):
        if mmi * a % m == 1:
            break
    return "".join(
        string.ascii_lowercase[mmi * (string.ascii_lowercase.index(char) - b) % m]
        if char in string.ascii_lowercase
        else char
        for char in ciphered_text.replace(" ", "")
    )

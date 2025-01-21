import string

# assume key <= 26

LOWER_CHARS = string.ascii_lowercase * 2
UPPER_CHARS = string.ascii_uppercase * 2


def rotate_char(char, key):
    if char in LOWER_CHARS:
        return LOWER_CHARS[LOWER_CHARS.index(char) + key]
    if char in UPPER_CHARS:
        return UPPER_CHARS[UPPER_CHARS.index(char) + key]
    return char


def rotate(text, key):
    return "".join(rotate_char(char, key) for char in text)

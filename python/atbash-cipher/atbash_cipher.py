import string

ATBASH_WORD_SIZE = 5


def encode(plain_text):
    encoded_text = decode(plain_text)
    return " ".join(
        encoded_text[i : i + ATBASH_WORD_SIZE]
        for i in range(0, len(encoded_text), ATBASH_WORD_SIZE)
    )


def decode(ciphered_text):
    return "".join(
        string.ascii_lowercase[
            len(string.ascii_lowercase) - 1 - string.ascii_lowercase.index(letter)
        ]
        if letter in string.ascii_lowercase
        else letter
        for letter in ciphered_text.lower()
        if letter not in (string.punctuation + " ")
    )

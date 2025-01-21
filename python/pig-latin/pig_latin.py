import itertools
import string

VOWELS = tuple("aeiou")
CONSONANTS = tuple(char for char in string.ascii_lowercase if char not in VOWELS)


def translate(text):
    def translate_word(word):
        if word[0] in VOWELS or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"
        if word.startswith("qu"):
            return word[2:] + "qu" + "ay"
        if any(word.startswith(char + "qu") for char in CONSONANTS):
            consonant, _, _, *rest = word
            return "".join(rest) + consonant + "qu" + "ay"
        if len(word) == 2 and word[-1] == "y":
            return word[::-1] + "ay"
        if word[0] == "y":
            return word[1:] + "y" + "ay"
        if "y" in word and all(char in CONSONANTS for char in word[: word.index("y")]):
            return word[word.index("y") :] + word[: word.index("y")] + "ay"
        if word[0] in CONSONANTS:
            prefix = "".join(itertools.takewhile(lambda char: char not in VOWELS, word))
            return word.removeprefix(prefix) + prefix + "ay"
        raise RuntimeError("no rules applied")

    return " ".join(translate_word(word) for word in text.split())

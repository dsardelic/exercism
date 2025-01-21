def is_pangram(sentence):
    return {char.upper() for char in sentence}.issuperset(
        {chr(letter_code) for letter_code in range(ord("A"), ord("Z") + 1)}
    )

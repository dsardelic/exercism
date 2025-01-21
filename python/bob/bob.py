def response(hey_bob):
    if not (hey_bob := hey_bob.strip()):
        return "Fine. Be that way!"
    if any(char.isalpha() for char in hey_bob) and all(
        char.upper() == char for char in hey_bob
    ):
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."

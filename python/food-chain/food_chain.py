def recite(start_verse, end_verse):
    foods = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    comments = [
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "It wriggled and jiggled and tickled inside her.",
        "How absurd to swallow a bird!",
        "Imagine that, to swallow a cat!",
        "What a hog, to swallow a dog!",
        "Just opened her throat and swallowed a goat!",
        "I don't know how she swallowed a cow!",
        "She's dead, of course!",
    ]

    def prey(verse_no):
        return (
            foods[verse_no - 1]
            if verse_no != 2
            else "spider that wriggled and jiggled and tickled inside her"
        )

    def generate_verse(verse_no):
        verse = [f"I know an old lady who swallowed a {foods[verse_no-1]}."]
        verse.append(comments[verse_no - 1])
        if verse_no not in {1, 8}:
            for i in range(verse_no, 1, -1):
                verse.append(
                    f"She swallowed the {foods[i-1]} to catch the {prey(i-1)}."
                )
            verse.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        return verse

    recital = []
    for i in range(start_verse, end_verse + 1):
        recital.extend(generate_verse(i))
        recital.append("")
    recital.pop()
    return recital

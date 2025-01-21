import functools


def recite(start_verse, end_verse):
    gifts = (
        "Partridge in a Pear Tree",
        "Turtle Doves",
        "French Hens",
        "Calling Birds",
        "Gold Rings",
        "Geese-a-Laying",
        "Swans-a-Swimming",
        "Maids-a-Milking",
        "Ladies Dancing",
        "Lords-a-Leaping",
        "Pipers Piping",
        "Drummers Drumming",
    )
    quantities = (
        "a",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
    )
    ordinals = (
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    )

    @functools.lru_cache
    def gifts_on_day(day, print_and_for_the_first_day=False):
        maybe_and = "and " if not day and print_and_for_the_first_day else ""
        curr_gifts = f"{maybe_and}{quantities[day]} {gifts[day]}"
        return curr_gifts if not day else f"{curr_gifts}, {gifts_on_day(day - 1, True)}"

    return [
        f"On the {ordinals[verse - 1]} day of Christmas my true love gave to me: "
        f"{gifts_on_day(verse - 1)}."
        for verse in range(start_verse, end_verse + 1)
    ]

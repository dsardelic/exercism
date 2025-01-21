import itertools


def proverb(*args, qualifier=None):
    if not args:
        return []
    return [
        f"For want of a {arg} the {next_arg} was lost."
        for arg, next_arg in itertools.pairwise(args)
    ] + [f"And all for the want of a {qualifier + ' ' if qualifier else ''}{args[0]}."]

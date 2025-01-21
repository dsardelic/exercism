def value(colors):
    color_catalog = (
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    )
    return int("".join(str(color_catalog.index(color)) for color in colors[:2]))

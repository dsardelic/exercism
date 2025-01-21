def label(colors):
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

    metric_prefixes = {
        "": 1,
        "kilo": 1_000,
        "mega": 1_000_000,
        "giga": 1_000_000_000,
    }

    ohm_value = int(
        "".join(str(color_catalog.index(color)) for color in colors[:2])
        + "0" * color_catalog.index(colors[2])
    )

    for prefix, multiplier in metric_prefixes.items():
        if (prefixed_ohm_value := ohm_value // multiplier) < 1000:
            return f"{prefixed_ohm_value} {prefix}ohms"

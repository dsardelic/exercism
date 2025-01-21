RESISTOR_COLORS = (
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

RESISTOR_TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors):
    if len(colors) < 4:
        return format_resistor_label(parse_number(colors))
    *value_colors, multiplier_color, tolerance_color = colors
    return format_resistor_label(
        *scaled(
            parse_number(value_colors)
            * pow(10, RESISTOR_COLORS.index(multiplier_color))
        ),
        RESISTOR_TOLERANCES[tolerance_color],
    )


def parse_number(colors):
    return sum(
        RESISTOR_COLORS.index(colors[i]) * pow(10, len(colors) - 1 - i)
        for i in range(len(colors))
    )


def scaled(number):
    scale = ""
    scales = iter(["kilo", "mega", "giga"])
    while number > 1000:
        number /= 1000
        scale = next(scales)
    return (int(number) if int(number) == number else number), scale


def format_resistor_label(number, scale="", tolerance=None):
    return f"{number} {scale}ohms{(' ±' + str(tolerance) + '%') if tolerance else ''}"

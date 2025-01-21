ROMAN_LITERALS = "IVXLCDM"


def roman(number: int) -> str:
    return "".join(
        [
            convert(digit, *ROMAN_LITERALS[2 * power : 2 * power + 3])
            for power, digit in enumerate(reversed(str(number)))
        ][::-1]
    )


def convert(digit: str, regular: str, higher: str = None, highest: str = None) -> str:
    match digit:
        case "0":
            ret_val = ""
        case "1" | "2" | "3":
            ret_val = regular * int(digit)
        case "4":
            ret_val = regular + higher
        case "5":
            ret_val = higher
        case "6" | "7" | "8":
            ret_val = higher + (int(digit) - 5) * regular
        case "9":
            ret_val = regular + highest
    return ret_val

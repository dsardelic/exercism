def from_input_base_to_base_10(input_base, digits):
    return sum(
        digit * input_base**power for power, digit in enumerate(reversed(digits))
    )


def from_base_10_to_output_base(number, output_base):
    if not number:
        return [0]
    digits = []
    while number:
        digits = [number % output_base, *digits]
        number //= output_base
    return digits


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    return from_base_10_to_output_base(
        from_input_base_to_base_10(input_base, digits), output_base
    )

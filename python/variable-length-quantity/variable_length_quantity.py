def encode(numbers):
    def encode_number(number):
        number, rest = divmod(number, 128)
        encoded = [rest]
        while number:
            encoded.insert(0, (number % 128) | (1 << 7))
            number //= 128
        return encoded

    return sum((encode_number(number) for number in numbers), start=[])


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = 128 * number + (byte % 128)
        if byte >= 0x80:
            can_terminate = False
        else:
            numbers.append(number)
            number = 0
            can_terminate = True
    if can_terminate:
        return numbers
    raise ValueError("incomplete sequence")

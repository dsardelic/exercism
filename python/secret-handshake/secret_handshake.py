def commands(binary_str):
    actions = ("jump", "close your eyes", "double blink", "wink")
    maybe_handshake = [
        action for digit, action in zip(binary_str[1:], actions) if digit == "1"
    ]
    return maybe_handshake if binary_str[0] == "1" else maybe_handshake[::-1]

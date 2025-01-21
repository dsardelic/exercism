import itertools


def encode(message, rails_count):
    rails = [[] for _ in range(rails_count)]
    rail_indices = itertools.cycle(
        itertools.chain(range(0, rails_count), range(rails_count - 2, 0, -1))
    )
    for rail_index, char in zip(rail_indices, message):
        rails[rail_index].append(char)
    return "".join("".join(rail) for rail in rails)


def decode(encoded_message, rails_count):
    rail_indices = itertools.cycle(
        itertools.chain(range(0, rails_count), range(rails_count - 2, 0, -1))
    )
    decoded_message = [next(rail_indices) for _ in range(len(encoded_message))]
    encoded_message_chars = iter(encoded_message)
    for rail_index in range(rails_count):
        while rail_index in decoded_message:
            decoded_message[decoded_message.index(rail_index)] = next(
                encoded_message_chars
            )
    return "".join(decoded_message)

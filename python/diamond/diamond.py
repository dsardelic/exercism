def rows(letter):
    r_val = []
    row_length = (ord(letter) - ord("A")) * 2 + 1

    def do_letter(curr_letter):
        row_chars = [" "] * row_length
        offset = ord(curr_letter) - ord("A")
        row_chars[row_length // 2 - offset] = curr_letter
        row_chars[row_length // 2 + offset] = curr_letter
        row = "".join(row_chars)
        r_val.append(row)
        if curr_letter != letter:
            do_letter(chr(ord(curr_letter) + 1))
            r_val.append(row)

    do_letter("A")
    return r_val

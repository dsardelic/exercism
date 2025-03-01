def is_paired(input_string):
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in input_string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    if stack:
        return False
    return True

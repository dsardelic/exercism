import operator


def parse_number(token):
    try:
        return int(token)
    except ValueError as err:
        raise ValueError("syntax error") from err


def parse_operation(token):
    operations = {
        "plus": operator.add,
        "minus": operator.sub,
        "multiplied by": operator.mul,
        "divided by": operator.floordiv,
    }
    try:
        return operations[token]
    except KeyError as k_err:
        # is token actually a number?
        try:
            _ = int(token)
        except ValueError as v_err:
            # no, token is not a number
            raise ValueError("unknown operation") from v_err
        # yes, token is a number
        raise ValueError("syntax error") from k_err


def answer(question):
    if not question.startswith("What"):
        raise ValueError("unknown operation")
    if not question.startswith("What is "):
        raise ValueError("syntax error")
    tokens = question.removeprefix("What is ").removesuffix("?").split()
    result = 0
    operation = operator.add
    expected_token_type_is_numerical = True
    i = 0
    while i < len(tokens):
        if expected_token_type_is_numerical:
            result = operation(result, parse_number(tokens[i]))
            expected_token_type_is_numerical = False
        else:
            if tokens[i] in ("multiplied", "divided"):
                operation = parse_operation(f"{tokens[i]} {tokens[i+1]}")
                i += 1
            else:
                operation = parse_operation(tokens[i])
            expected_token_type_is_numerical = True
        i += 1
    if expected_token_type_is_numerical:
        raise ValueError("syntax error")
    return result

import re

DEFAULT_WORDS = ("+", "-", "*", "/", "dup", "drop", "swap", "over")


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.

    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


def evaluate(input_data):  # pylint: disable=too-complex
    user_defined_words = {}

    def execute_operation(word, statement_tokens, stack):
        if word_definition := user_defined_words.get(word, None):
            for token in reversed(word_definition):
                statement_tokens.append(token)
            return

        match word:
            case "+":
                stack.append(pop_operand(stack) + pop_operand(stack))
            case "-":
                subtrahend = pop_operand(stack)
                minuend = pop_operand(stack)
                stack.append(minuend - subtrahend)
            case "*":
                stack.append(pop_operand(stack) * pop_operand(stack))
            case "/":
                if not (divisor := pop_operand(stack)):
                    raise ZeroDivisionError("divide by zero")
                dividend = pop_operand(stack)
                stack.append(dividend // divisor)
            case "dup":
                item = pop_operand(stack)
                stack.append(item)
                stack.append(item)
            case "drop":
                _ = pop_operand(stack)
            case "swap":
                head = pop_operand(stack)
                tail = pop_operand(stack)
                stack.append(head)
                stack.append(tail)
            case "over":
                head = pop_operand(stack)
                tail = pop_operand(stack)
                stack.append(tail)
                stack.append(head)
                stack.append(tail)
            case _:
                raise ValueError("undefined operation")

    def ultimate_definition_tokens(token):
        if token in user_defined_words:
            return [
                ultimate_definition_tokens(subtoken)
                for subtoken in user_defined_words[token]
            ]
        if token in DEFAULT_WORDS or is_a_number(token):
            return [token]
        raise ValueError("illegal operation")

    stack = []
    for statement in input_data:
        if match := re.fullmatch(r"\: ([ -~]+?) ([ -~]+) ;", statement.lower()):
            # user-defined word
            word = match.group(1).lower()
            if is_a_number(word):
                raise ValueError("illegal operation")
            user_defined_words[word] = flatten(
                ultimate_definition_tokens(definition_token)
                for definition_token in match.group(2).lower().split()
            )
        else:
            statement_tokens = statement.lower().split()[::-1]
            while statement_tokens:
                statement_token = statement_tokens.pop()
                if is_a_number(statement_token):
                    stack.append(int(statement_token))
                else:
                    execute_operation(statement_token, statement_tokens, stack)

    return stack


def pop_operand(stack):
    if not stack:
        raise StackUnderflowError("Insufficient number of items in stack")
    return stack.pop()


def is_a_number(token):
    return bool(re.fullmatch(r"-?\d+", token))


def flatten(iterable):
    def flatten_items():
        for item in iterable:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    return list(flatten_items())

def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    step_number = 0
    while True:
        step_number += 1
        if (number := (3 * number + 1 if number % 2 else number // 2)) == 1:
            return step_number

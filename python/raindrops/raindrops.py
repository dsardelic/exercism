def convert(number):
    if not all((number % 3, number % 5, number % 7)):
        return (
            f"{'' if number % 3 else 'Pling'}"
            f"{'' if number % 5 else 'Plang'}"
            f"{'' if number % 7 else 'Plong'}"
        )
    return str(number)

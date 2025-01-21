def sum_of_multiples(limit, multiples):
    return sum(
        set().union(
            *(
                set(range(multiple, limit, multiple) if multiple else {0})
                for multiple in multiples
            )
        )
    )

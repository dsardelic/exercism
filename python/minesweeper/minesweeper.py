def annotate(minefield):
    def mine_count_at(x, y):
        return sum(
            minefield[i][j] == "*"
            for i in range(max(x - 1, 0), min(x + 1 + 1, len(minefield)))
            for j in range(max(y - 1, 0), min(y + 1 + 1, len(minefield[0])))
            if not (i == x and j == y)
        )

    if len(set(len(row) for row in minefield)) > 1:
        raise ValueError("The board is invalid with current input.")

    if set(field for row in minefield for field in row) > set("* "):
        raise ValueError("The board is invalid with current input.")

    return [
        "".join(
            field
            if field == "*" or not mine_count_at(i, j)
            else str(mine_count_at(i, j))
            for j, field in enumerate(row)
        )
        for i, row in enumerate(minefield)
    ]

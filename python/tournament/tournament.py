from collections import defaultdict


def tally(rows):
    teams = defaultdict(list)
    for row in rows:
        team1, team2, outcome = row.split(";")
        if outcome == "win":
            teams[team1].append(3)
            teams[team2].append(0)
        if outcome == "draw":
            teams[team1].append(1)
            teams[team2].append(1)
        if outcome == "loss":
            teams[team1].append(0)
            teams[team2].append(3)
    table_header = ["Team                           | MP |  W |  D |  L |  P"]
    table_rows = [
        " | ".join(
            (
                f"{item[0]:<30}",
                f"{len(item[1]):>2}",
                f"{item[1].count(3):>2}",
                f"{item[1].count(1):>2}",
                f"{item[1].count(0):>2}",
                f"{sum(item[1]):>2}",
            )
        )
        for item in sorted(teams.items(), key=lambda x: (-sum(x[1]), x[0]))
    ]
    return table_header + table_rows

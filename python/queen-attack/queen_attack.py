class Queen:
    def __init__(self, row, column):
        self.validate_position(row, column)
        self.row = row
        self.column = column

    @classmethod
    def validate_position(cls, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row)
            == abs(self.column - another_queen.column)
        )

import gleam/int

pub type Position {
  Position(row: Int, column: Int)
}

pub type Error {
  RowTooSmall
  RowTooLarge
  ColumnTooSmall
  ColumnTooLarge
}

pub fn create(queen: Position) -> Result(Nil, Error) {
  case queen {
    Position(x, _y) if x < 0 -> Error(RowTooSmall)
    Position(x, _y) if x > 7 -> Error(RowTooLarge)
    Position(_x, y) if y < 0 -> Error(ColumnTooSmall)
    Position(_x, y) if y > 7 -> Error(ColumnTooLarge)
    _ -> Ok(Nil)
  }
}

pub fn can_attack(
  black_queen black_queen: Position,
  white_queen white_queen: Position,
) -> Bool {
  white_queen.row == black_queen.row
  || white_queen.column == black_queen.column
  || {
    int.absolute_value(white_queen.row - black_queen.row)
    == int.absolute_value(white_queen.column - black_queen.column)
  }
}

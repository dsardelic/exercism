import gleam/int
import gleam/list
import gleam/set

pub type Position {
  Position(row: Int, column: Int)
}

pub fn saddle_points(matrix: List(List(Int))) -> List(Position) {
  let in_rows = do_rows(matrix)
  let in_cols = do_cols_as_rows(list.transpose(matrix))
  set.to_list(set.intersection(set.from_list(in_rows), set.from_list(in_cols)))
}

fn do_rows(matrix) {
  let maxs = matrix |> list.filter_map(list.reduce(_, int.max))

  matrix
  |> list.zip(maxs)
  |> list.index_map(fn(item, x) {
    let #(row, row_max) = item
    positions_for_rows(row, x, row_max, 0, [])
  })
  |> list.flatten
}

fn positions_for_rows(row, x, row_max, j, acc) {
  case row {
    [first, ..rest] if first == row_max ->
      positions_for_rows(rest, x, row_max, j + 1, [
        Position(x + 1, j + 1),
        ..acc
      ])
    [_, ..rest] -> positions_for_rows(rest, x, row_max, j + 1, acc)
    [] -> acc
  }
}

fn do_cols_as_rows(matrix) {
  let mins = matrix |> list.filter_map(list.reduce(_, int.min))

  matrix
  |> list.zip(mins)
  |> list.index_map(fn(item, x) {
    let #(row, row_min) = item
    positions_for_cols_as_rows(row, x, row_min, 0, [])
  })
  |> list.flatten
}

fn positions_for_cols_as_rows(row, x, row_min, j, acc) {
  case row {
    [first, ..rest] if first == row_min ->
      positions_for_cols_as_rows(rest, x, row_min, j + 1, [
        Position(j + 1, x + 1),
        ..acc
      ])
    [_, ..rest] -> positions_for_cols_as_rows(rest, x, row_min, j + 1, acc)
    [] -> acc
  }
}

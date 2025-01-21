import gleam/dict.{type Dict}
import gleam/list
import gleam/order
import gleam/string

type Point {
  Point(x: Int, y: Int)
}

type Grid =
  Dict(Point, String)

pub fn rectangles(input: String) -> Int {
  let grid: Grid = input |> to_grid

  grid
  |> to_list_of_vertices
  |> list.combination_pairs
  |> rectangle_count(grid)
}

fn to_grid(input: String) -> Grid {
  use grid, row, x <- list.index_fold(string.split(input, "\n"), dict.new())
  use grid, char, y <- list.index_fold(string.to_graphemes(row), grid)

  dict.insert(grid, Point(x, y), char)
}

fn to_list_of_vertices(grid: Grid) -> List(Point) {
  use vertices, grid_item <- list.fold(dict.to_list(grid), [])

  case grid_item {
    #(point, "+") -> [point, ..vertices]
    _ -> vertices
  }
}

fn rectangle_count(
  vertex_combinations: List(#(Point, Point)),
  grid: Grid,
) -> Int {
  use count, vertex_point_pair <- list.fold(vertex_combinations, 0)
  let #(vertex1, vertex2) = vertex_point_pair
  let assert [upper_left_vertex, lower_right_vertex] =
    list.sort([vertex1, vertex2], point_compare)

  case upper_left_vertex, lower_right_vertex {
    Point(v1_x, v1_y), Point(v2_x, v2_y) if v2_x > v1_x && v2_y > v1_y -> {
      case
        list.all(
          [
            is_valid_horizontal_edge(v1_x, v1_y, v2_y, grid),
            is_valid_horizontal_edge(v2_x, v1_y, v2_y, grid),
            is_valid_vertical_edge(v1_y, v1_x, v2_x, grid),
            is_valid_vertical_edge(v2_y, v1_x, v2_x, grid),
          ],
          fn(is_valid) { is_valid },
        )
      {
        True -> 1 + count
        False -> count
      }
    }
    _, _ -> count
  }
}

fn point_compare(left: Point, right: Point) -> order.Order {
  case left, right {
    Point(x_left, _), Point(x_right, _) if x_left < x_right -> order.Lt
    Point(x_left, _), Point(x_right, _) if x_left > x_right -> order.Gt
    Point(_, y_left), Point(_, y_right) if y_left < y_right -> order.Lt
    Point(_, y_left), Point(_, y_right) if y_left > y_right -> order.Gt
    _, _ -> order.Eq
  }
}

fn is_valid_horizontal_edge(x: Int, y_from: Int, y_to, grid: Grid) -> Bool {
  list.range(y_from, y_to)
  |> list.map(fn(y) { Point(x, y) })
  |> list.all(fn(point) {
    case dict.get(grid, point) {
      Ok("+") | Ok("-") -> True
      Ok(_) -> False
      Error(_) -> panic as "Coordinates out of bounds"
    }
  })
}

fn is_valid_vertical_edge(y: Int, x_from: Int, x_to, grid: Grid) -> Bool {
  list.range(x_from, x_to)
  |> list.map(fn(x) { Point(x, y) })
  |> list.all(fn(point) {
    case dict.get(grid, point) {
      Ok("+") | Ok("|") -> True
      Ok(_) -> False
      Error(_) -> panic as "Coordinates out of bounds"
    }
  })
}

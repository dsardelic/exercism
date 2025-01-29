import gleam/int
import gleam/string

pub fn is_valid(isbn: String) -> Bool {
  let dehyphenated = isbn |> string.replace("-", "")
  case dehyphenated |> string.length == 10 {
    False -> False
    True -> apply_isbn_formula(dehyphenated |> string.to_graphemes, 10, 0)
  }
}

fn apply_isbn_formula(digits: List(String), multiplier: Int, acc: Int) {
  case digits {
    [] -> acc % 11 == 0
    ["X"] -> apply_isbn_formula([], multiplier - 1, acc + 10 * multiplier)
    [first, ..rest] ->
      case first |> int.base_parse(10) {
        Ok(digit) ->
          apply_isbn_formula(rest, multiplier - 1, acc + digit * multiplier)
        Error(_) -> False
      }
  }
}

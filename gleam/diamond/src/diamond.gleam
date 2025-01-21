import gleam/list
import gleam/string

pub fn build(letter: String) -> String {
  let matrix: List(List(String)) =
    matrix_row(letter) |> list.repeat({ ord(letter) - ord("A") } * 2 + 1)

  let keep_indices_only = fn(tuple: #(String, List(String))) -> List(String) {
    let #(to_remain, chars) = tuple
    list.map(chars, fn(char) {
      case char == to_remain {
        True -> char
        False -> " "
      }
    })
  }

  letter
  |> indices
  |> list.zip(matrix)
  |> list.map(keep_indices_only)
  |> list.map(string.join(_, with: ""))
  |> string.join(with: "\n")
}

fn ord(char: String) -> Int {
  let assert [codepoint, ..] = char |> string.to_utf_codepoints
  codepoint |> string.utf_codepoint_to_int
}

fn chr(int: Int) -> String {
  let assert Ok(codepoint) = int |> string.utf_codepoint
  [codepoint] |> string.from_utf_codepoints
}

fn matrix_row(letter: String) -> List(String) {
  case letter {
    "A" -> ["A"]
    _ -> {
      list.flatten([[letter], matrix_row(chr(ord(letter) - 1)), [letter]])
    }
  }
}

fn indices(letter: String) -> List(String) {
  indices_loop("A", letter)
}

fn indices_loop(from: String, until: String) -> List(String) {
  case from == until {
    True -> [until]
    False ->
      list.flatten([[from], indices_loop(chr(ord(from) + 1), until), [from]])
  }
}

import gleam/list
import gleam/string

pub fn rotate(shift_key: Int, text: String) -> String {
  text
  |> string.to_graphemes
  |> list.map(rotate_char(_, shift_key))
  |> string.concat
}

fn rotate_char(char: String, shift_key: Int) {
  let uppercase = ord(char) >= ord("A") && ord(char) <= ord("Z")
  let lowercase = ord(char) >= ord("a") && ord(char) <= ord("z")
  case uppercase, lowercase {
    True, _ -> chr({ ord(char) - ord("A") + shift_key } % 26 + ord("A"))
    _, True -> chr({ ord(char) - ord("a") + shift_key } % 26 + ord("a"))
    _, _ -> char
  }
}

fn ord(char: String) -> Int {
  let assert [codepoint, ..] = char |> string.to_utf_codepoints
  codepoint |> string.utf_codepoint_to_int
}

fn chr(int: Int) -> String {
  let assert Ok(codepoint) = int |> string.utf_codepoint
  [codepoint] |> string.from_utf_codepoints
}

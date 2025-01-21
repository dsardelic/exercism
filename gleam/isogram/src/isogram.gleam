import gleam/list
import gleam/string

pub fn is_isogram(phrase phrase: String) -> Bool {
  let chars =
    phrase
    |> string.replace(" ", "")
    |> string.replace("-", "")
    |> string.lowercase()
    |> string.to_graphemes()

  chars == list.unique(chars)
}

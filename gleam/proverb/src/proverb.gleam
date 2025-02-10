import gleam/list
import gleam/string

pub fn recite(inputs: List(String)) -> String {
  case inputs {
    [] -> ""
    [first] -> "And all for the want of a " <> first <> "."
    [first, ..] ->
      inputs
      |> list.window_by_2
      |> list.map(fn(pair) {
        "For want of a " <> pair.0 <> " the " <> pair.1 <> " was lost."
      })
      |> string.join("\n")
      <> "\nAnd all for the want of a "
      <> first
      <> "."
  }
}

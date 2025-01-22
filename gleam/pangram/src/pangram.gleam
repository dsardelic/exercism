import gleam/list
import gleam/set
import gleam/string

pub fn is_pangram(sentence: String) -> Bool {
  list.range(65, 90)
  |> list.filter_map(string.utf_codepoint)
  |> set.from_list
  |> set.difference(
    sentence |> string.uppercase |> string.to_utf_codepoints |> set.from_list,
  )
  |> set.is_empty
}

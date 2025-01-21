import gleam/bool
import gleam/dict.{type Dict}
import gleam/list
import gleam/option.{None, Some}
import gleam/regex
import gleam/string

pub fn count_words(input: String) -> Dict(String, Int) {
  let assert Ok(delimiters) = regex.from_string("[^'\\w]|_")

  input
  |> string.lowercase
  |> regex.split(content: _, with: delimiters)
  |> list.map(trim(_, "'"))
  |> list.filter(fn(word) { word |> string.is_empty |> bool.negate })
  |> to_counter
}

fn trim(str: String, char: String) -> String {
  str |> trim_left(char) |> trim_right(char)
}

fn trim_left(str: String, char: String) -> String {
  case str |> string.starts_with(char) {
    True -> trim_left(string.slice(str, 1, string.length(str) - 1), char)
    False -> str
  }
}

fn trim_right(str: String, char: String) -> String {
  case string.ends_with(str, char) {
    True -> trim_right(string.slice(str, 0, string.length(str) - 1), char)
    False -> str
  }
}

fn to_counter(words: List(String)) -> Dict(String, Int) {
  list.fold(words, dict.new(), fn(counter, key) {
    dict.upsert(counter, key, fn(value) {
      case value {
        Some(n) -> n + 1
        None -> 1
      }
    })
  })
}

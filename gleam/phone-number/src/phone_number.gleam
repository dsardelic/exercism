import gleam/list
import gleam/regex
import gleam/result
import gleam/string

pub fn clean(input: String) -> Result(String, String) {
  input
  |> sanitize
  |> validate
}

fn sanitize(str: String) -> String {
  let assert Ok(pattern) = regex.from_string(" |\\+|\\-|\\(|\\)|\\.")
  regex.replace(pattern, str, "")
}

fn validate(digit_string: String) -> Result(String, String) {
  digit_string
  |> check_length
  |> result.try(remove_country_code)
  |> result.try(check_area_code)
  |> result.try(check_exchange_code)
  |> result.try(check_for_punctuation)
  |> result.try(check_for_letters)
}

fn check_length(str: String) -> Result(String, String) {
  case string.length(str) {
    length if length < 10 -> Error("must not be fewer than 10 digits")
    length if length > 11 -> Error("must not be greater than 11 digits")
    _ -> Ok(str)
  }
}

fn remove_country_code(str: String) -> Result(String, String) {
  case string.length(str), string.first(str) {
    11, Ok("1") -> Ok(string.slice(str, 1, string.length(str) - 1))
    11, _ -> Error("11 digits must start with 1")
    10, _ -> Ok(str)
    _, _ -> panic as "10- or 11-char string expected"
  }
}

fn check_area_code(string_10: String) -> Result(String, String) {
  let assert Ok(char) = string.first(string_10)
  case char {
    "0" -> Error("area code cannot start with zero")
    "1" -> Error("area code cannot start with one")
    _ -> Ok(string_10)
  }
}

fn check_exchange_code(string_10: String) -> Result(String, String) {
  case string.slice(string_10, 3, 1) {
    "0" -> Error("exchange code cannot start with zero")
    "1" -> Error("exchange code cannot start with one")
    _ -> Ok(string_10)
  }
}

fn check_for_punctuation(string_10: String) -> Result(String, String) {
  let punctuation = "@:!" |> string.to_graphemes()
  case
    string_10
    |> string.to_graphemes
    |> list.filter(list.contains(punctuation, _))
    |> list.length
  {
    0 -> Ok(string_10)
    _ -> Error("punctuations not permitted")
  }
}

fn check_for_letters(string_10: String) -> Result(String, String) {
  let uppercase_letters = list.range(ord("A"), ord("Z")) |> list.map(chr)
  case
    string_10
    |> string.uppercase
    |> string.to_graphemes
    |> list.filter(list.contains(uppercase_letters, _))
    |> list.length
  {
    0 -> Ok(string_10)
    _ -> Error("letters not permitted")
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

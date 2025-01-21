import gleam/string

pub fn message(log_line: String) -> String {
  case string.split_once(log_line, ": ") {
    Ok(#(_, message)) -> string.trim(message)
    Error(_) -> panic as "Unknown what to do in this case"
  }
}

pub fn log_level(log_line: String) -> String {
  case string.split_once(log_line, ": ") {
    Ok(#(level, _)) -> trim_brackets(string.lowercase(level))
    Error(_) -> panic as "Unknown what to do in this case"
  }
}

pub fn reformat(log_line: String) -> String {
  case string.split_once(log_line, ": ") {
    Ok(#(level, message)) ->
      string.trim(message)
      <> " ("
      <> trim_brackets(string.lowercase(level))
      <> ")"
    Error(_) -> panic as "Unknown what to do in this case"
  }
}

fn trim_leading_char(str: String, char: String) -> String {
  case string.first(str) {
    Ok(ch) if ch == char ->
      trim_leading_char(string.slice(str, 1, string.length(str) - 1), char)
    _ -> str
  }
}

fn trim_trailing_char(str: String, char: String) -> String {
  case string.last(str) {
    Ok(ch) if ch == char ->
      trim_trailing_char(string.slice(str, 0, string.length(str) - 1), char)
    _ -> str
  }
}

fn trim_char(str: String, char: String) -> String {
  str |> trim_leading_char(char) |> trim_trailing_char(char)
}

fn trim_brackets(str: String) {
  str |> trim_char("[") |> trim_char("]")
}

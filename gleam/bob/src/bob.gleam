import gleam/string

pub fn hey(remark: String) -> String {
  let remark = string.trim(remark)
  case remark {
    "" -> "Fine. Be that way!"
    _ -> {
      let is_question = remark |> string.ends_with("?")
      let all_letters_are_caps =
        remark == string.uppercase(remark) && remark != string.lowercase(remark)
      case is_question, all_letters_are_caps {
        True, True -> "Calm down, I know what I'm doing!"
        True, False -> "Sure."
        False, True -> "Whoa, chill out!"
        False, False -> "Whatever."
      }
    }
  }
}

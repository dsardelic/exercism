import gleam/option.{type Option, None, Some}

pub fn two_fer(name: Option(String)) -> String {
  let recipient: String = case name {
    Some(name) -> name
    None -> "you"
  }
  "One for " <> recipient <> ", one for me."
}

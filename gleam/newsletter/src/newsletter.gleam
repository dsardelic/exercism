import gleam/result
import gleam/string
import simplifile

pub fn read_emails(path: String) -> Result(List(String), Nil) {
  case path |> simplifile.read {
    Ok(content) -> Ok(content |> string.trim |> string.split("\n"))
    Error(_) -> Error(Nil)
  }
}

pub fn create_log_file(path: String) -> Result(Nil, Nil) {
  path |> simplifile.create_file |> result.replace_error(Nil)
}

pub fn log_sent_email(path: String, email: String) -> Result(Nil, Nil) {
  path |> simplifile.append(email <> "\n") |> result.replace_error(Nil)
}

pub fn send_newsletter(
  emails_path: String,
  log_path: String,
  send_email: fn(String) -> Result(Nil, Nil),
) -> Result(Nil, Nil) {
  case read_emails(emails_path) {
    Ok(emails) -> {
      let _ = create_log_file(log_path)
      send_newsletter_loop(emails, log_path, send_email)
    }
    Error(_) -> Error(Nil)
  }
}

fn send_newsletter_loop(
  emails: List(String),
  log_path: String,
  send_email: fn(String) -> Result(Nil, Nil),
) -> Result(Nil, Nil) {
  case emails {
    [] -> Ok(Nil)
    [first, ..rest] ->
      case send_email(first) {
        Ok(_) -> {
          let _ = log_sent_email(log_path, first)
          send_newsletter_loop(rest, log_path, send_email)
        }
        Error(_) -> {
          send_newsletter_loop(rest, log_path, send_email)
        }
      }
  }
}

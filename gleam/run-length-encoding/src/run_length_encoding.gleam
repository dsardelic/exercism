import gleam/int
import gleam/list
import gleam/string

pub fn encode(plaintext: String) -> String {
  let compress_and_concat = fn(acc, segment) {
    case segment, list.length(segment) {
      [first, ..], 1 -> acc <> first
      [first, ..], n -> acc <> int.to_string(n) <> first
      _, _ -> acc
    }
  }

  plaintext
  |> string.to_graphemes
  |> segmentalize
  |> list.fold("", compress_and_concat)
}

pub fn decode(ciphertext: String) -> String {
  ciphertext
  |> string.to_graphemes
  |> group_into_digits_and_data
  |> list.map(string.concat)
  |> decompress
}

fn segmentalize(lst) {
  case lst {
    [] -> []
    [first, ..] -> {
      let #(segment, unsegmentalized) =
        list.split_while(lst, fn(x) { x == first })
      [segment, ..segmentalize(unsegmentalized)]
    }
  }
}

fn group_into_digits_and_data(lst) {
  case lst {
    [] -> []
    [first, ..rest] -> {
      let #(digits, ungrouped) =
        list.split_while(lst, string.contains("0123456789", _))
      case digits {
        [] -> [[first], ..group_into_digits_and_data(rest)]
        [_, ..] -> [digits, ..group_into_digits_and_data(ungrouped)]
      }
    }
  }
}

fn decompress(lst) {
  case lst {
    [] -> ""
    [first] -> first
    [first, second, ..rest] ->
      case int.base_parse(first, 10) {
        Ok(n) -> string.repeat(second, n) <> decompress(rest)
        Error(_) -> first <> decompress([second, ..rest])
      }
  }
}

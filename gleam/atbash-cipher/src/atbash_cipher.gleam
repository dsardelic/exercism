import gleam/bit_array
import gleam/list
import gleam/string

pub fn encode(phrase: String) -> String {
  phrase
  |> string.lowercase
  |> string.to_graphemes
  |> list.filter_map(atbash_replace)
  |> list.sized_chunk(5)
  |> list.map(string.concat)
  |> string.join(" ")
}

pub fn decode(phrase: String) -> String {
  phrase
  |> string.to_graphemes
  |> list.filter_map(atbash_replace)
  |> string.concat
}

fn atbash_replace(char: String) {
  case <<char:utf8>> {
    <<ord>> if ord >= 97 && ord <= 122 ->
      bit_array.to_string(<<{ 122 - { ord - 97 } }>>)
    <<ord>> if ord >= 48 && ord <= 57 -> Ok(char)
    _ -> Error(Nil)
  }
}

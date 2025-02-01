import gleam/bit_array
import gleam/int
import gleam/list
import gleam/string

type TranscodeType {
  Encode
  Decode
}

pub fn encode(plaintext plaintext: String, key key: String) -> String {
  transcode(plaintext, key, Encode)
}

pub fn decode(ciphertext ciphertext: String, key key: String) -> String {
  transcode(ciphertext, key, Decode)
}

fn transcode(plaintext, key, transcode_type) {
  plaintext
  |> string.to_graphemes
  |> list.sized_chunk(string.length(key))
  |> list.flat_map(list.zip(_, string.to_graphemes(key)))
  |> list.filter_map(transcode_char(_, transcode_type))
  |> string.concat
}

fn transcode_char(
  pair: #(String, String),
  transcode_type: TranscodeType,
) -> Result(String, Nil) {
  let assert <<ord_char>> = <<pair.0:utf8>>
  let assert <<ord_key_char>> = <<pair.1:utf8>>
  let assert <<ord_a>> = <<"a">>

  case transcode_type {
    Encode ->
      bit_array.to_string(<<
        { ord_a + { ord_char - ord_a + { ord_key_char - ord_a } } % 26 },
      >>)
    Decode ->
      bit_array.to_string(<<
        { ord_a + { ord_char - ord_a - { ord_key_char - ord_a } + 26 } % 26 },
      >>)
  }
}

pub fn generate_key() -> String {
  let random_replace = fn(char) {
    let assert <<ord_char>> = <<char:utf8>>
    bit_array.to_string(<<{ ord_char + int.random(25) }>>)
  }

  string.repeat("a", 100)
  |> string.to_graphemes
  |> list.filter_map(random_replace)
  |> string.concat
}

import gleam/bool
import gleam/list
import gleam/result
import gleam/string

pub type Error {
  KeyNotCoprime(Int, Int)
}

const alphabet = "abcdefghijklmnopqrstuvwxyz"

const m = 26

pub fn encode(
  plaintext plaintext: String,
  a a: Int,
  b b: Int,
) -> Result(String, Error) {
  use <- bool.guard(!are_coprime(a, m), Error(KeyNotCoprime(a, m)))

  plaintext
  |> string.lowercase
  |> string.to_graphemes
  |> list.filter_map(encode_letter(_, a, b))
  |> list.sized_chunk(5)
  |> list.map(string.concat)
  |> string.join(" ")
  |> Ok
}

pub fn decode(
  ciphertext ciphertext: String,
  a a: Int,
  b b: Int,
) -> Result(String, Error) {
  use <- bool.guard(!are_coprime(a, m), Error(KeyNotCoprime(a, m)))

  ciphertext
  |> string.replace(" ", "")
  |> string.to_graphemes
  |> list.filter_map(decode_letter(_, mmi(a), b))
  |> string.concat
  |> Ok
}

fn encode_letter(letter, a, b) {
  let is_lowercase_letter = string.contains(alphabet, letter)
  let is_digit = string.contains("0123456789", letter)

  case is_lowercase_letter, is_digit {
    True, _ -> {
      use i <- result.try(index_of(letter))
      alphabet_letter({ a * i + b } % m)
    }
    _, True -> Ok(letter)
    _, _ -> Error(Nil)
  }
}

fn decode_letter(letter, mmi, b) {
  case string.contains("0123456789", letter) {
    True -> Ok(letter)
    False -> {
      use i <- result.try(index_of(letter))
      alphabet_letter(mmi * { i - b } % m)
    }
  }
}

fn are_coprime(x, y) {
  case x {
    _ if x > y -> are_coprime_loop(x, y, 2)
    _ if x < y -> are_coprime_loop(y, x, 2)
    _ -> False
  }
}

fn are_coprime_loop(x, y, divisor) {
  case x % divisor == 0 && y % divisor == 0 {
    True -> False
    False ->
      case divisor == y {
        True -> True
        False -> are_coprime_loop(x, y, divisor + 1)
      }
  }
}

fn index_of(letter) {
  alphabet
  |> string.to_graphemes
  |> list.zip(list.range(0, m - 1))
  |> list.key_find(letter)
}

fn alphabet_letter(index) {
  let index = case index >= 0 {
    True -> index
    False -> { index + { -index / m + 1 } * m } % m
  }

  list.range(0, m - 1)
  |> list.zip(alphabet |> string.to_graphemes)
  |> list.key_find(index)
}

fn mmi(a) {
  mmi_loop(a, 0)
}

fn mmi_loop(a, i) {
  case i * a % m == 1 {
    True -> i
    False ->
      case i == m {
        False -> mmi_loop(a, i + 1)
        True -> panic as "Infinite loop ahead"
      }
  }
}

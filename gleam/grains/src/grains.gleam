import gleam/int
import gleam/list
import gleam/result

pub type Error {
  InvalidSquare
}

pub fn square(square: Int) -> Result(Int, Error) {
  case square {
    square if square < 1 || square > 64 -> Error(InvalidSquare)
    _ -> Ok(int_pow(2, square - 1, 1))
  }
}

pub fn total() -> Int {
  list.range(1, 64)
  |> list.map(square)
  |> result.values
  |> int.sum
}

fn int_pow(base: Int, power: Int, acc: Int) {
  case power {
    0 -> acc
    _ -> int_pow(base, power - 1, acc * base)
  }
}

import gleam/int
import gleam/string

pub fn is_armstrong_number(number: Int) -> Bool {
  armstrong_formula(0, number, number |> int.to_string |> string.length)
  == number
}

fn armstrong_formula(acc: Int, number: Int, power: Int) -> Int {
  case number {
    0 -> acc
    _ ->
      armstrong_formula(acc + int_power(number % 10, power), number / 10, power)
  }
}

fn int_power(n: Int, power: Int) {
  case power {
    0 -> 1
    _ -> n * int_power(n, power - 1)
  }
}

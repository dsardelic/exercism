import gleam/list
import gleam/result

pub type Error {
  InvalidBase(Int)
  InvalidDigit(Int)
}

pub fn rebase(
  digits digits: List(Int),
  input_base input_base: Int,
  output_base output_base: Int,
) -> Result(List(Int), Error) {
  use input_base <- result.try(validate_base(input_base))
  use output_base <- result.try(validate_base(output_base))
  use digits <- result.try(validate_digits(digits, digits, input_base))
  case digits |> to_base_10(input_base) |> from_base_10(output_base) {
    [] -> Ok([0])
    lst -> Ok(lst)
  }
}

fn validate_base(base) {
  case base {
    base if base < 2 -> Error(InvalidBase(base))
    _ -> Ok(base)
  }
}

fn validate_digits(all, unvalidated, base) {
  case unvalidated {
    [] -> Ok(all)
    [first, ..] if first < 0 || first >= base -> Error(InvalidDigit(first))
    [_, ..rest] -> validate_digits(all, rest, base)
  }
}

fn to_base_10(digits, base) {
  do_to_base_10(list.reverse(digits), base, 0, 0)
}

fn do_to_base_10(digits, base, power, acc) {
  case digits {
    [] -> acc
    [first, ..rest] ->
      do_to_base_10(rest, base, power + 1, acc + first * int_pow(base, power))
  }
}

fn from_base_10(number, base) {
  do_from_base_10(number, base, 0, [])
}

fn do_from_base_10(number, base, power, acc) {
  case int_pow(base, power) > number {
    True -> acc
    False -> {
      let digit = number % int_pow(base, power + 1) / int_pow(base, power)
      do_from_base_10(number, base, power + 1, [digit, ..acc])
    }
  }
}

fn int_pow(base, power) {
  case power {
    0 -> 1
    1 -> base
    _ -> base * int_pow(base, power - 1)
  }
}

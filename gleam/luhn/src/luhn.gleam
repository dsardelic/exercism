import gleam/bool
import gleam/int
import gleam/list
import gleam/regex
import gleam/string

pub fn valid(value: String) -> Bool {
  let assert Ok(reg_exp) = regex.from_string("^[0-9]{2,}$")
  use <- bool.guard(
    !regex.check(reg_exp, string.replace(value, " ", "")),
    False,
  )

  let double_odd_digits = fn(digit, i) {
    case int.is_odd(i) {
      True ->
        case 2 * digit > 9 {
          True -> 2 * digit - 9
          False -> 2 * digit
        }
      False -> digit
    }
  }

  value
  |> string.replace(" ", "")
  |> string.to_graphemes
  |> list.reverse
  |> list.filter_map(int.base_parse(_, 10))
  |> list.index_map(double_odd_digits)
  |> int.sum
  |> int.modulo(10)
  == Ok(0)
}

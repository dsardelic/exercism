import gleam/list

pub fn factors(value: Int) -> List(Int) {
  list.reverse(do_factors(value, 2, []))
}

fn do_factors(value, divisor, acc) {
  case value {
    1 -> acc
    value if value > 1 ->
      case value % divisor == 0 {
        True -> do_factors(value / divisor, divisor, [divisor, ..acc])
        False -> do_factors(value, divisor + 1, acc)
      }
    _ -> panic as "Invalid value"
  }
}

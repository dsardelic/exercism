pub fn convert(number: Int) -> String {
  let roman_digit_groups = [
    ["I", "V", "X"],
    ["X", "L", "C"],
    ["C", "D", "M"],
    ["M", "", ""],
  ]
  convert_place_value("", number, 1, roman_digit_groups)
}

fn convert_place_value(
  acc: String,
  number: Int,
  place_value: Int,
  roman_digit_groups: List(List(String)),
) {
  case roman_digit_groups {
    [[lo, mid, hi], ..rest] -> {
      let roman_digit = case number % { place_value * 10 } / place_value {
        1 -> lo
        2 -> lo <> lo
        3 -> lo <> lo <> lo
        4 -> lo <> mid
        5 -> mid
        6 -> mid <> lo
        7 -> mid <> lo <> lo
        8 -> mid <> lo <> lo <> lo
        9 -> lo <> hi
        _ -> ""
      }
      convert_place_value(roman_digit <> acc, number, place_value * 10, rest)
    }
    _ -> acc
  }
}

import gleam/bool
import gleam/list
import gleam/string

pub type Error {
  OutOfRange
}

const first_twenty_numbers = [
  "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
  "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
  "seventeen", "eighteen", "nineteen", "twenty",
]

const multiples_of_ten = [
  "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
  "ninety",
]

const powers_of_1000_names = ["billion", "million", "thousand", ""]

pub fn say(number: Int) -> Result(String, Error) {
  use <- bool.guard(number < 0, Error(OutOfRange))
  use <- bool.guard(
    number >= int_pow(1000, list.length(powers_of_1000_names)),
    Error(OutOfRange),
  )
  use <- bool.guard(number == 0, Ok("zero"))

  number
  |> to_multipliers_of_powers_list(list.length(powers_of_1000_names))
  |> list.zip(powers_of_1000_names)
  |> list.map(say_multiplier_and_power)
  |> list.map(string.trim)
  |> string.join(" ")
  |> string.trim
  |> Ok
}

fn to_multipliers_of_powers_list(number, power) {
  case power {
    0 -> []
    _ -> [
      number % int_pow(1000, power) / int_pow(1000, power - 1),
      ..to_multipliers_of_powers_list(number, power - 1)
    ]
  }
}

fn say_multiplier_and_power(number_and_power: #(Int, String)) {
  let #(number, power) = number_and_power
  case say_number_below_1000(number) {
    "" -> ""
    text -> text <> " " <> power
  }
}

fn say_number_below_1000(number) {
  case number / 100 {
    0 -> say_number_below_100(number % 100)
    _ -> {
      list_element_at(first_twenty_numbers, number / 100)
      <> " hundred "
      <> say_number_below_100(number % 100)
    }
  }
}

fn say_number_below_100(number) {
  case number < 21 {
    True -> list_element_at(first_twenty_numbers, number)
    False -> {
      let tens = list_element_at(multiples_of_ten, number / 10)
      let ones = list_element_at(first_twenty_numbers, number % 10)
      case ones {
        "" -> tens
        _ -> tens <> "-" <> ones
      }
    }
  }
}

fn list_element_at(lst, index) {
  let assert [first, ..rest] = lst
  case index {
    0 -> first
    _ if index > 0 -> list_element_at(rest, index - 1)
    _ -> panic as "Invalid index"
  }
}

fn int_pow(base, power) {
  case power {
    0 -> 1
    1 -> base
    _ if power > 1 -> base * int_pow(base, power - 1)
    _ -> panic as "Invalid power"
  }
}

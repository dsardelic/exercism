pub type Error {
  NonPositiveNumber
}

pub fn steps(number: Int) -> Result(Int, Error) {
  case number > 0 {
    True -> Ok(steps_for_positive(0, number))
    False -> Error(NonPositiveNumber)
  }
}

fn steps_for_positive(acc: Int, number: Int) -> Int {
  case number {
    1 -> acc
    _ if number % 2 == 1 -> steps_for_positive(1 + acc, 3 * number + 1)
    _ -> steps_for_positive(1 + acc, number / 2)
  }
}

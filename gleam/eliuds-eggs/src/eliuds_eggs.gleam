pub fn egg_count(number: Int) -> Int {
  egg_count_accumulator(number, 0)
}

fn egg_count_accumulator(number: Int, acc: Int) -> Int {
  case number {
    0 -> acc
    _ if number % 2 == 1 -> egg_count_accumulator(number / 2, acc + 1)
    _ -> egg_count_accumulator(number / 2, acc)
  }
}

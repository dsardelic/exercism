import gleam/list
import gleam/string

pub fn recite(
  start_bottles start_bottles: Int,
  take_down take_down: Int,
) -> String {
  start_bottles
  |> list.range(start_bottles - take_down + 1)
  |> list.map(stanza)
  |> string.join("\n\n")
}

fn number_to_text(number: Int) -> String {
  case number {
    0 -> "no"
    1 -> "one"
    2 -> "two"
    3 -> "three"
    4 -> "four"
    5 -> "five"
    6 -> "six"
    7 -> "seven"
    8 -> "eight"
    9 -> "nine"
    10 -> "ten"
    _ -> panic as "Beyond scope"
  }
}

fn line1(start_bottles: Int) -> String {
  start_bottles |> number_to_text |> string.capitalise
  <> " green bottle"
  <> case start_bottles {
    1 -> ""
    _ -> "s"
  }
  <> " hanging on the wall,"
}

fn line2(start_bottles: Int) -> String {
  line1(start_bottles)
}

fn line3(_start_bottles: Int) -> String {
  "And if one green bottle should accidentally fall,"
}

fn line4(start_bottles: Int) -> String {
  let remaining_bottles = number_to_text(start_bottles - 1)
  case start_bottles {
    2 -> "There'll be one green bottle hanging on the wall."
    _ ->
      "There'll be "
      <> remaining_bottles
      <> " green bottles hanging on the wall."
  }
}

fn stanza(start_bottles: Int) -> String {
  string.join(
    [
      line1(start_bottles),
      line2(start_bottles),
      line3(start_bottles),
      line4(start_bottles),
    ],
    "\n",
  )
}

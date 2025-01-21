import gleam/int

pub fn convert(number: Int) -> String {
  let sound =
    ""
    |> add_sound(number, 3, "Pling")
    |> add_sound(number, 5, "Plang")
    |> add_sound(number, 7, "Plong")
  case sound {
    "" -> int.to_string(number)
    _ -> sound
  }
}

fn add_sound(acc: String, number: Int, divisor: Int, sound: String) -> String {
  case number % divisor {
    0 -> acc <> sound
    _ -> acc
  }
}

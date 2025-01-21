import gleam/float
import gleam/int
import gleam/list
import gleam/result

pub type Resistance {
  Resistance(unit: String, value: Int)
}

pub fn label(colors: List(String)) -> Result(Resistance, String) {
  colors
  |> colors_to_resistance
  |> apply_metric_prefixes(["", "kilo", "mega", "giga"])
}

fn color_to_value(color: String) -> Result(Int, String) {
  case color {
    "black" -> Ok(0)
    "brown" -> Ok(1)
    "red" -> Ok(2)
    "orange" -> Ok(3)
    "yellow" -> Ok(4)
    "green" -> Ok(5)
    "blue" -> Ok(6)
    "violet" -> Ok(7)
    "grey" -> Ok(8)
    "white" -> Ok(9)
    _ -> Error("Invalid color")
  }
}

fn colors_to_resistance(colors: List(String)) -> Result(Resistance, String) {
  use values <- result.try(
    colors
    |> list.take(3)
    |> list.try_map(color_to_value),
  )
  case values {
    [] | [_] | [_, _] -> Error("Not enough colors")
    [value1, value2, value3, ..] -> {
      use power <- result.try(
        value3
        |> int.to_float
        |> int.power(10, _)
        |> result.try_recover(fn(_) { Error("int.power() failed") }),
      )
      Ok(Resistance("ohms", { value1 * 10 + value2 } * float.truncate(power)))
    }
  }
}

fn apply_metric_prefixes(
  resistance: Result(Resistance, String),
  prefixes: List(String),
) -> Result(Resistance, String) {
  case resistance, prefixes {
    Error(message), _ -> Error(message)
    Ok(_), [] -> Error("Not enough metric prefixes")
    Ok(Resistance(unit, value)), [prefix, ..rest] -> {
      case value >= 1000 {
        True -> apply_metric_prefixes(Ok(Resistance(unit, value / 1000)), rest)
        False -> Ok(Resistance(prefix <> unit, value))
      }
    }
  }
}

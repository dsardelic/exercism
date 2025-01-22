import gleam/float
import gleam/int
import gleam/list

pub type Classification {
  Perfect
  Abundant
  Deficient
}

pub type Error {
  NonPositiveInt
}

pub fn classify(number: Int) -> Result(Classification, Error) {
  case number > 0 {
    False -> Error(NonPositiveInt)
    True ->
      case aliquot_sum(number) {
        sum if sum < number -> Ok(Deficient)
        sum if sum > number -> Ok(Abundant)
        _ -> Ok(Perfect)
      }
  }
}

fn aliquot_sum(number: Int) {
  let mapper = fn(divisor) {
    case number % divisor == 0 {
      True if number / divisor == divisor -> [divisor]
      True if number / divisor != divisor -> [divisor, number / divisor]
      _ -> []
    }
  }

  let assert Ok(square_root) = float.square_root(int.to_float(number))

  list.range(1, square_root |> float.truncate)
  |> list.flat_map(mapper)
  |> int.sum()
  |> int.subtract(number)
}

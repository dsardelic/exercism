import gleam/list
import gleam/string

pub fn slices(input: String, size: Int) -> Result(List(String), Error) {
  case string.length(input) {
    0 -> Error(EmptySeries)
    _ if size < 0 -> Error(SliceLengthNegative)
    _ if size == 0 -> Error(SliceLengthZero)
    length if size > length -> Error(SliceLengthTooLarge)
    length if size == length -> Ok([input])
    _ ->
      Ok(
        input
        |> string.to_graphemes
        |> list.window(size)
        |> list.map(string.concat),
      )
  }
}

pub type Error {
  SliceLengthTooLarge
  SliceLengthZero
  SliceLengthNegative
  EmptySeries
}

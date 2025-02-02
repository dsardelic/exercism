import gleam/float
import gleam/int

pub fn square_root(radicand: Int) -> Int {
  let assert Ok(root) = radicand |> int.to_float |> float.square_root
  float.truncate(root)
}

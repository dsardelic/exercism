import gleam/float
import gleam/int
import gleam/list
import gleam/result

pub fn square_of_sum(n: Int) -> Int {
  let sum: Result(Float, Nil) =
    list.range(1, n)
    |> int.sum
    |> int.power(2.0)

  case sum {
    Ok(sum) -> float.truncate(sum)
    Error(_) -> panic as "Unknown what needs to be done here"
  }
}

pub fn sum_of_squares(n: Int) -> Int {
  let squares =
    list.range(1, n)
    |> list.map(int.power(_, 2.0))
    |> result.all

  case squares {
    Ok(l) -> float.truncate(float.sum(l))
    Error(_) -> panic as "Unknown what needs to be done here"
  }
}

pub fn difference(n: Int) -> Int {
  square_of_sum(n) - sum_of_squares(n)
}

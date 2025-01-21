import gleam/int
import gleam/list
import gleam/result
import gleam/set

pub fn sum(factors factors: List(Int), limit limit: Int) -> Int {
  factors
  |> list.map(multiples(_, limit))
  |> list.reduce(set.union)
  |> result.unwrap(set.new())
  |> set.fold(0, int.add)
}

fn multiples(factor: Int, limit: Int) -> set.Set(Int) {
  case factor >= limit {
    True -> set.new()
    False ->
      list.range(1, { limit - 1 } / factor)
      |> list.map(int.multiply(_, factor))
      |> set.from_list
  }
}

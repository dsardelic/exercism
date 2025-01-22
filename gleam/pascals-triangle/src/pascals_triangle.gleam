import gleam/list
import gleam/result

pub fn rows(n: Int) -> List(List(Int)) {
  case n {
    0 -> []
    _ -> unfold([[1]], 1, n)
  }
}

fn unfold(acc, from, to) {
  case from == to {
    True -> acc
    False -> {
      unfold(
        list.append(acc, [next_row(acc |> list.last |> result.unwrap([]))]),
        from + 1,
        to,
      )
    }
  }
}

fn next_row(row) {
  [1, ..inner_sums(row) |> list.append([1])]
}

fn inner_sums(row) {
  row
  |> list.window_by_2
  |> list.map(fn(tuple) { tuple.0 + tuple.1 })
}

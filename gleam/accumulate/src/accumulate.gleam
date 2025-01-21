import gleam/list

pub fn accumulate(list: List(a), fun: fn(a) -> b) -> List(b) {
  do_accumulate([], list, fun)
}

fn do_accumulate(acc: List(b), list: List(a), fun: fn(a) -> b) -> List(b) {
  case list {
    [] -> acc |> list.reverse
    [first, ..rest] -> do_accumulate([fun(first), ..acc], rest, fun)
  }
}

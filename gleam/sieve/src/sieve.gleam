import gleam/dict.{type Dict}
import gleam/list
import gleam/result

pub fn primes_up_to(upper_bound: Int) -> List(Int) {
  case upper_bound < 2 {
    True -> []
    False -> {
      let candidates = list.range(2, upper_bound)
      let number_to_marked =
        dict.from_list(candidates |> list.map(fn(n) { #(n, False) }))
      let number_to_marked = mark(candidates, number_to_marked, upper_bound)

      candidates
      |> list.filter(fn(n) {
        number_to_marked |> dict.get(n) |> result.unwrap(True) == False
      })
    }
  }
}

fn mark(
  candidates: List(Int),
  number_to_marked: Dict(Int, Bool),
  upper_bound: Int,
) -> Dict(Int, Bool) {
  case candidates {
    [] -> number_to_marked
    [first, ..rest] -> {
      let assert Ok(marked) = number_to_marked |> dict.get(first)
      case marked {
        True -> mark(rest, number_to_marked, upper_bound)
        False ->
          mark(
            rest,
            mark_multiple(
              in: number_to_marked,
              multiple: first + first,
              of: first,
              if_not_greater_than: upper_bound,
            ),
            upper_bound,
          )
      }
    }
  }
}

fn mark_multiple(
  in number_to_marked: Dict(Int, Bool),
  multiple multiple: Int,
  of prime: Int,
  if_not_greater_than upper_bound: Int,
) {
  case multiple > upper_bound {
    True -> number_to_marked
    False ->
      mark_multiple(
        dict.insert(number_to_marked, multiple, True),
        multiple + prime,
        prime,
        upper_bound,
      )
  }
}

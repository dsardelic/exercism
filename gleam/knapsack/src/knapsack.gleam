import gleam/bool
import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/result

pub type Item {
  Item(value: Int, weight: Int)
}

pub fn maximum_value(items: List(Item), maximum_weight: Int) -> Int {
  // for each weight remember local max value and list of used items
  let max_data: Dict(Int, #(Int, List(Item))) =
    list.fold(items, dict.new(), fn(acc, item) {
      case dict.get(acc, item.weight) {
        Ok(#(value, _)) if item.value <= value -> acc
        _ -> dict.insert(acc, item.weight, #(item.value, [item]))
      }
    })

  // local max value might not be the biggest max value along the way
  run(from: 0, until: maximum_weight, with: items, using_acc: max_data)
  |> dict.filter(fn(weight, _v) { weight <= maximum_weight })
  |> dict.fold([], fn(acc, _k, v) { [v.0, ..acc] })
  |> list.reduce(int.max)
  |> result.unwrap(0)
}

fn run(from weight, until max_weight, with all_items, using_acc max_data) {
  use <- bool.guard(weight == max_weight, max_data)

  case dict.get(max_data, weight) {
    Ok(#(value, used_items)) -> {
      let maybe_update = fn(max_data, unused_item: Item) {
        let new_weight = weight + unused_item.weight
        use <- bool.guard(new_weight > max_weight, max_data)
        let new_value = value + unused_item.value
        case dict.get(max_data, new_weight) {
          Ok(#(max_value, _)) if new_value <= max_value -> max_data
          _ ->
            dict.insert(
              max_data,
              new_weight,
              #(new_value, [unused_item, ..used_items]),
            )
        }
      }

      run(
        weight + 1,
        max_weight,
        all_items,
        list.fold(list_diff(all_items, used_items), max_data, maybe_update),
      )
    }
    Error(_) -> run(weight + 1, max_weight, all_items, max_data)
  }
}

fn list_diff(lst1: List(a), lst2: List(a)) {
  case lst2 {
    [] -> lst1
    [first, ..lst2_rest] -> {
      case list.pop(lst1, fn(item) { item == first }) {
        Ok(#(_, lst1_rest)) -> list_diff(lst1_rest, lst2_rest)
        Error(_) -> list_diff(lst1, lst2_rest)
      }
    }
  }
}

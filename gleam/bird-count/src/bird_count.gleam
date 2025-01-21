import gleam/int
import gleam/list
import gleam/result

pub fn today(days: List(Int)) -> Int {
  result.unwrap(list.first(days), 0)
}

pub fn increment_day_count(days: List(Int)) -> List(Int) {
  case days {
    [] -> [1]
    [first, ..rest] -> [first + 1, ..rest]
  }
}

pub fn has_day_without_birds(days: List(Int)) -> Bool {
  list.any(days, fn(x) { x == 0 })
}

pub fn total(days: List(Int)) -> Int {
  int.sum(days)
}

pub fn busy_days(days: List(Int)) -> Int {
  list.fold(days, 0, fn(acc, x) {
    case x >= 5 {
      True -> acc + 1
      False -> acc
    }
  })
}

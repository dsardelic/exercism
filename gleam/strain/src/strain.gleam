import gleam/list

pub fn keep(list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  do_keep([], list, predicate)
}

pub fn discard(list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  do_discard([], list, predicate)
}

fn do_keep(acc: List(t), list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  case list {
    [] -> list.reverse(acc)
    [first, ..rest] -> {
      case predicate(first) {
        True -> do_keep([first, ..acc], rest, predicate)
        False -> do_keep(acc, rest, predicate)
      }
    }
  }
}

fn do_discard(acc: List(t), list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  case list {
    [] -> list.reverse(acc)
    [first, ..rest] -> {
      case predicate(first) {
        False -> do_discard([first, ..acc], rest, predicate)
        True -> do_discard(acc, rest, predicate)
      }
    }
  }
}

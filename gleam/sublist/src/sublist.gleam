import gleam/list

pub type Comparison {
  Equal
  Unequal
  Sublist
  Superlist
}

pub fn sublist(compare list_a: List(a), to list_b: List(a)) -> Comparison {
  case list.length(list_a), list.length(list_b) {
    _, _ if list_a == list_b -> Equal
    0, _ -> Sublist
    _, 0 -> Superlist
    len_a, len_b if len_a < len_b ->
      case list_contains_sublist(list_b, list_a) {
        True -> Sublist
        False -> Unequal
      }
    len_a, len_b if len_a > len_b ->
      case list_contains_sublist(list_a, list_b) {
        True -> Superlist
        False -> Unequal
      }
    _, _ -> Unequal
  }
}

fn list_contains_sublist(superlist, sublist) {
  case superlist, sublist {
    _, [] -> True
    [], [_, ..] -> False
    [superlist_first, ..superlist_rest], [sublist_first, ..sublist_rest] ->
      case
        superlist_first == sublist_first
        && list_starts_with(superlist_rest, sublist_rest)
      {
        True -> True
        False -> list_contains_sublist(superlist_rest, sublist)
      }
  }
}

fn list_starts_with(superlist, sublist) {
  case superlist, sublist {
    _, [] -> True
    [], [_, ..] -> False
    [superlist_first, ..superlist_rest], [sublist_first, ..sublist_rest] ->
      case superlist_first == sublist_first {
        True -> list_starts_with(superlist_rest, sublist_rest)
        False -> False
      }
  }
}

pub fn append(first first: List(a), second second: List(a)) -> List(a) {
  case first {
    [] -> second
    [first, ..rest] -> [first, ..append(rest, second)]
  }
}

pub fn concat(lists: List(List(a))) -> List(a) {
  case lists {
    [] -> []
    [first, ..rest] -> append(first, concat(rest))
  }
}

pub fn filter(list: List(a), function: fn(a) -> Bool) -> List(a) {
  case list {
    [] -> []
    [first, ..rest] ->
      case function(first) {
        True -> [first, ..filter(rest, function)]
        False -> filter(rest, function)
      }
  }
}

pub fn length(list: List(a)) -> Int {
  case list {
    [] -> 0
    [_, ..rest] -> 1 + length(rest)
  }
}

pub fn map(list: List(a), function: fn(a) -> b) -> List(b) {
  case list {
    [] -> []
    [first, ..rest] -> [function(first), ..map(rest, function)]
  }
}

pub fn foldl(
  over list: List(a),
  from initial: b,
  with function: fn(b, a) -> b,
) -> b {
  case list {
    [] -> initial
    [first, ..rest] -> foldl(rest, function(initial, first), function)
  }
}

pub fn foldr(
  over list: List(a),
  from initial: b,
  with function: fn(b, a) -> b,
) -> b {
  foldl(reverse(list), initial, function)
}

pub fn reverse(list: List(a)) -> List(a) {
  case list {
    [] -> []
    [first, ..rest] -> append(reverse(rest), [first])
  }
}

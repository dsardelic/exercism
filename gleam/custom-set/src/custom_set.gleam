import gleam/list

pub opaque type Set(t) {
  Set(contents: List(t))
}

pub fn new(members: List(t)) -> Set(t) {
  Set(members |> list.unique)
}

pub fn is_empty(set: Set(t)) -> Bool {
  set.contents |> list.is_empty
}

pub fn contains(in set: Set(t), this member: t) -> Bool {
  set.contents |> list.contains(member)
}

pub fn is_subset(first: Set(t), of second: Set(t)) -> Bool {
  list.all(first.contents, fn(member) { contains(second, member) })
}

pub fn disjoint(first: Set(t), second: Set(t)) -> Bool {
  first |> intersection(second) |> is_empty
}

pub fn is_equal(first: Set(t), to second: Set(t)) -> Bool {
  is_subset(first, second) && is_subset(second, first)
}

pub fn add(to set: Set(t), this member: t) -> Set(t) {
  case set.contents |> list.contains(member) {
    True -> set
    False -> Set(set.contents |> list.prepend(member))
  }
}

pub fn intersection(of first: Set(t), and second: Set(t)) -> Set(t) {
  Set(first.contents |> list.filter(list.contains(second.contents, _)))
}

pub fn difference(between first: Set(t), and second: Set(t)) -> Set(t) {
  Set(
    first.contents
    |> list.filter(fn(member) { !list.contains(second.contents, member) }),
  )
}

pub fn union(of first: Set(t), and second: Set(t)) -> Set(t) {
  new(first.contents |> list.append(second.contents))
}

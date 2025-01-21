import gleam/list

pub type Tree {
  Nil
  Node(data: Int, left: Tree, right: Tree)
}

pub fn to_tree(data: List(Int)) -> Tree {
  data |> list.fold(Nil, insert)
}

fn insert(tree: Tree, value: Int) -> Tree {
  case tree {
    Nil -> Node(value, Nil, Nil)
    Node(data, left, right) ->
      case value <= data {
        True -> Node(data, insert(left, value), right)
        False -> Node(data, left, insert(right, value))
      }
  }
}

pub fn sorted_data(data: List(Int)) -> List(Int) {
  inorder(to_tree(data))
}

fn inorder(tree: Tree) -> List(Int) {
  case tree {
    Nil -> []
    Node(data, left, right) ->
      inorder(left)
      |> list.append([data])
      |> list.append(inorder(right))
  }
}

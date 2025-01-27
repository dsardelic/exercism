import gleam/list
import gleam/result

pub type Tree(a) {
  Tree(label: a, children: List(Tree(a)))
}

pub fn from_pov(tree: Tree(a), from: a) -> Result(Tree(a), Nil) {
  case tree.label == from {
    True -> Ok(tree)
    False ->
      case path_from_ancestor_to_descendant(tree, from) {
        Ok([_root, ..rest]) -> from_pov_loop(tree, from, rest)
        Ok([]) -> Error(Nil)
        Error(_) -> Error(Nil)
      }
  }
}

fn from_pov_loop(
  tree: Tree(a),
  from: a,
  label_path: List(a),
) -> Result(Tree(a), Nil) {
  case label_path {
    [] -> Ok(tree)
    [label, ..rest_of_labels] -> {
      use child <- result.try(
        list.find(tree.children, fn(child) { child.label == label }),
      )
      let updated_tree =
        Tree(
          tree.label,
          list.filter(tree.children, fn(child) { child.label != label }),
        )
      let updated_child = Tree(child.label, [updated_tree, ..child.children])
      from_pov_loop(updated_child, from, rest_of_labels)
    }
  }
}

pub fn path_to(
  tree tree: Tree(a),
  from from: a,
  to to: a,
) -> Result(List(a), Nil) {
  case path_to_loop(tree, from, to, tree.children) {
    Ok(path) -> Ok(path)
    Error(Nil) -> {
      case
        path_from_descendant_to_ancestor(tree, from),
        path_from_ancestor_to_descendant(tree, to)
      {
        Ok(path_from), Ok(path_to) -> {
          Ok(
            list_remove_if_exists_last(path_from)
            |> list.append([tree.label])
            |> list.append(list_remove_if_exists_first(path_to)),
          )
        }
        _, _ -> Error(Nil)
      }
    }
  }
}

pub fn path_to_loop(
  tree: Tree(a),
  from: a,
  to: a,
  children: List(Tree(a)),
) -> Result(List(a), Nil) {
  case children {
    [] -> Error(Nil)
    [first, ..rest] -> {
      case path_to(first, from, to) {
        Ok(path) -> Ok(path)
        Error(Nil) -> path_to_loop(tree, from, to, rest)
      }
    }
  }
}

fn path_from_descendant_to_ancestor(
  tree: Tree(a),
  from: a,
) -> Result(List(a), Nil) {
  case tree.label == from {
    True -> Ok([from])
    False -> path_from_descendant_to_ancestor_loop(tree, from, tree.children)
  }
}

fn path_from_descendant_to_ancestor_loop(
  tree: Tree(a),
  from: a,
  children: List(Tree(a)),
) -> Result(List(a), Nil) {
  case children {
    [] -> Error(Nil)
    [first, ..rest] -> {
      case path_from_descendant_to_ancestor(first, from) {
        Ok(path) -> Ok(list.append(path, [tree.label]))
        Error(Nil) -> path_from_descendant_to_ancestor_loop(tree, from, rest)
      }
    }
  }
}

fn path_from_ancestor_to_descendant(
  tree: Tree(a),
  to: a,
) -> Result(List(a), Nil) {
  case tree.label == to {
    True -> Ok([to])
    False -> path_from_ancestor_to_descendant_loop(tree, to, tree.children)
  }
}

fn path_from_ancestor_to_descendant_loop(
  tree: Tree(a),
  to: a,
  children: List(Tree(a)),
) -> Result(List(a), Nil) {
  case children {
    [] -> Error(Nil)
    [first, ..rest] -> {
      case path_from_ancestor_to_descendant(first, to) {
        Ok(path) -> Ok([tree.label, ..path])
        Error(Nil) -> path_from_ancestor_to_descendant_loop(tree, to, rest)
      }
    }
  }
}

fn list_remove_if_exists_first(list: List(a)) -> List(a) {
  case list {
    [] -> []
    [_, ..rest] -> rest
  }
}

fn list_remove_if_exists_last(list: List(a)) -> List(a) {
  case list {
    [] -> []
    [_] -> []
    [first, ..rest] -> [first, ..list_remove_if_exists_last(rest)]
  }
}

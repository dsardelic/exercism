import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub fn row(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> to_list_of_lists_of_int
  |> result.try(list_at(_, index - 1))
}

pub fn column(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> to_list_of_lists_of_int
  |> result.map(list.transpose(_))
  |> result.try(list_at(_, index - 1))
}

fn to_list_of_lists_of_int(str) {
  str
  |> string.split("\n")
  |> list.map(string.split(_, " "))
  |> list.map(to_list_of_ints(_))
  |> list.map(result.all)
  |> result.all
}

fn to_list_of_ints(lst_of_strs) {
  case lst_of_strs {
    [] -> []
    [first, ..rest] -> [int.base_parse(first, 10), ..to_list_of_ints(rest)]
  }
}

fn list_at(lst, idx) {
  case lst, idx {
    _, idx if idx < 0 -> Error(Nil)
    _, 0 -> list.first(lst)
    [], _ -> Error(Nil)
    [_first, ..rest], idx -> list_at(rest, idx - 1)
  }
}

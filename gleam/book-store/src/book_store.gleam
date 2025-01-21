import gleam/dict
import gleam/float
import gleam/int
import gleam/list
import gleam/option.{None, Some}
import gleam/result

pub type BookQtyPerType =
  dict.Dict(Int, Int)

pub type BookSetQtyPerSize =
  dict.Dict(Int, Int)

pub fn lowest_price(books: List(Int)) -> Float {
  books
  |> count_book_types
  |> count_book_sets
  |> optimize_book_sets
  |> calculate_price
}

fn count_book_types(book_types: List(Int)) -> BookQtyPerType {
  list.fold(book_types, dict.new(), fn(acc, book_type) {
    dict.upsert(acc, book_type, fn(value) {
      case value {
        Some(value) -> value + 1
        None -> 1
      }
    })
  })
}

fn count_book_sets(book_qty_per_type: BookQtyPerType) -> BookSetQtyPerSize {
  count_book_sets_loop(dict.new(), dict.values(book_qty_per_type))
}

fn count_book_sets_loop(acc: BookSetQtyPerSize, book_qtys: List(Int)) {
  case book_qtys {
    [] -> acc
    _ -> {
      let book_set_qty = book_qtys |> list.reduce(int.min) |> result.unwrap(0)
      let book_set_size = list.length(book_qtys)
      let acc =
        dict.upsert(acc, book_set_size, fn(value) {
          case value {
            Some(value) -> value + book_set_qty
            None -> book_set_qty
          }
        })
      let book_qtys =
        book_qtys
        |> list.map(fn(x) { x - book_set_qty })
        |> list.filter(fn(x) { x > 0 })

      count_book_sets_loop(acc, book_qtys)
    }
  }
}

fn optimize_book_sets(
  book_set_qty_per_size: BookSetQtyPerSize,
) -> BookSetQtyPerSize {
  let can_form_a_better_book_set =
    dict.has_key(book_set_qty_per_size, 5)
    && dict.has_key(book_set_qty_per_size, 3)
  case can_form_a_better_book_set {
    False -> book_set_qty_per_size
    True -> {
      let remove_one_set_of_size = fn(
        book_set_qty_per_size: BookSetQtyPerSize,
        size: Int,
      ) {
        dict.map_values(book_set_qty_per_size, fn(key, value) {
          case key {
            _ if key == size -> value - 1
            _ -> value
          }
        })
      }

      let add_two_sets_of_size_4 = fn(book_set_qty_per_size: BookSetQtyPerSize) {
        dict.upsert(book_set_qty_per_size, 4, fn(value) {
          case value {
            Some(value) -> value + 2
            None -> 2
          }
        })
      }

      let remove_empty = fn(book_set_qty_per_size: BookSetQtyPerSize) {
        dict.filter(book_set_qty_per_size, fn(_key, value) { value != 0 })
      }

      optimize_book_sets(
        book_set_qty_per_size
        |> remove_one_set_of_size(5)
        |> remove_one_set_of_size(3)
        |> add_two_sets_of_size_4
        |> remove_empty,
      )
    }
  }
}

fn calculate_price(book_set_qty_per_size: BookSetQtyPerSize) -> Float {
  let single_book_price = 800.0
  let discount_pct_per_book_set_size =
    dict.from_list([#(2, 5.0), #(3, 10.0), #(4, 20.0), #(5, 25.0)])
  let discount_pct = fn(book_set_size: Int) -> Float {
    book_set_size
    |> dict.get(discount_pct_per_book_set_size, _)
    |> result.unwrap(0.0)
  }
  let discounted_book_set_price = fn(book_set_size) {
    int.to_float(book_set_size)
    *. single_book_price
    *. { 1.0 -. discount_pct(book_set_size) /. 100.0 }
  }

  dict.fold(book_set_qty_per_size, 0.0, fn(acc, book_set_size, book_set_qty) {
    float.add(
      acc,
      discounted_book_set_price(book_set_size) *. int.to_float(book_set_qty),
    )
  })
}

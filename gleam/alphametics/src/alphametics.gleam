import gleam/bool
import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub fn solve(puzzle: String) -> Result(Dict(String, Int), Nil) {
  let assert [addends, sum] =
    puzzle
    |> string.replace(" ", "")
    |> string.split("==")

  let addends = string.split(addends, "+")
  let addends = case addends {
    [_, _, ..] -> Ok(addends)
    _ -> Error(Nil)
  }
  use addends <- result.try(addends)

  let non_zero_letters =
    [sum, ..addends]
    |> list.filter(fn(word) { string.length(word) >= 2 })
    |> list.map(string.first)
    |> result.values

  let max_length =
    [sum, ..addends]
    |> list.map(string.length)
    |> list.reduce(int.max)
    |> result.unwrap(0)

  let words =
    [sum, ..addends]
    |> list.map(string.pad_left(_, max_length, "0"))
    |> list.map(string.reverse)
    |> list.map(string.to_graphemes)
  let assert [sum, ..addends] = words

  process_next_addend_digit(addends, 0, sum, [], non_zero_letters, dict.new())
}

fn process_next_addend_digit(
  addends,
  column_sum,
  sum,
  later_addends,
  non_zero_letters,
  mappings,
) {
  case addends {
    [] -> {
      process_next_sum_digit(
        sum,
        column_sum,
        later_addends,
        non_zero_letters,
        mappings,
      )
    }
    [addends_first, ..addends_rest] -> {
      case addends_first {
        [] -> {
          // check for carry from previous column
          case column_sum > 0 {
            True -> Error(Nil)
            False -> validate_solution(mappings, non_zero_letters)
          }
        }
        ["0", ..addend_rest] ->
          process_next_addend_digit(
            addends_rest,
            column_sum,
            sum,
            [addend_rest, ..later_addends],
            non_zero_letters,
            mappings,
          )
        [addend_first, ..addend_rest] -> {
          case dict.get(mappings, addend_first) {
            Ok(digit) -> {
              process_next_addend_digit(
                addends_rest,
                column_sum + digit,
                sum,
                [addend_rest, ..later_addends],
                non_zero_letters,
                mappings,
              )
            }
            Error(_) ->
              try_addend_digit_candidate(
                available_digits(mappings),
                addend_first,
                addend_rest,
                addends_rest,
                column_sum,
                sum,
                later_addends,
                non_zero_letters,
                mappings,
              )
          }
        }
      }
    }
  }
}

fn try_addend_digit_candidate(
  possible_digits,
  addend_first,
  addend_rest,
  addends_rest,
  column_sum,
  sum,
  later_addends,
  non_zero_letters,
  mappings,
) {
  case possible_digits, list.contains(non_zero_letters, addend_first) {
    [], _ -> Error(Nil)
    [0, ..digits_rest], True ->
      try_addend_digit_candidate(
        digits_rest,
        addend_first,
        addend_rest,
        addends_rest,
        column_sum,
        sum,
        later_addends,
        non_zero_letters,
        mappings,
      )
    [digit, ..digits_rest], _ -> {
      case
        process_next_addend_digit(
          addends_rest,
          column_sum + digit,
          sum,
          [addend_rest, ..later_addends],
          non_zero_letters,
          mappings |> dict.insert(addend_first, digit),
        )
      {
        Ok(solution) -> Ok(solution)
        Error(Nil) ->
          try_addend_digit_candidate(
            digits_rest,
            addend_first,
            addend_rest,
            addends_rest,
            column_sum,
            sum,
            later_addends,
            non_zero_letters,
            mappings,
          )
      }
    }
  }
}

fn available_digits(mappings) {
  list.range(0, 9)
  |> list.filter(fn(digit) {
    mappings
    |> dict.values()
    |> list.contains(digit)
    |> bool.negate
  })
}

fn process_next_sum_digit(
  sum,
  column_sum,
  later_addends,
  non_zero_letters,
  mappings,
) {
  let assert [sum_first, ..sum_rest] = sum
  case dict.get(mappings, sum_first) {
    Ok(digit) ->
      case column_sum % 10 == digit {
        False -> Error(Nil)
        True ->
          process_next_addend_digit(
            later_addends,
            column_sum / 10,
            sum_rest,
            [],
            non_zero_letters,
            mappings,
          )
      }
    Error(_) -> {
      case mappings |> dict.values |> list.contains(column_sum % 10) {
        True -> Error(Nil)
        False ->
          process_next_addend_digit(
            later_addends,
            column_sum / 10,
            sum_rest,
            [],
            non_zero_letters,
            mappings |> dict.insert(sum_first, column_sum % 10),
          )
      }
    }
  }
}

fn validate_solution(mappings, non_zero_letters) {
  case
    non_zero_letters
    |> list.any(fn(letter) { dict.get(mappings, letter) == Ok(0) })
  {
    True -> Error(Nil)
    False -> Ok(mappings)
  }
}

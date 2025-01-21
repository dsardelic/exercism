import gleam/dict
import gleam/function
import gleam/int
import gleam/list

pub type Category {
  Ones
  Twos
  Threes
  Fours
  Fives
  Sixes
  FullHouse
  FourOfAKind
  LittleStraight
  BigStraight
  Choice
  Yacht
}

pub fn score(category: Category, dice: List(Int)) -> Int {
  case category {
    Ones -> number_score(dice, 1)
    Twos -> number_score(dice, 2)
    Threes -> number_score(dice, 3)
    Fours -> number_score(dice, 4)
    Fives -> number_score(dice, 5)
    Sixes -> number_score(dice, 6)
    FullHouse -> full_house_score(dice)
    FourOfAKind -> four_of_a_kind_score(dice)
    LittleStraight -> little_straight_score(dice)
    BigStraight -> big_straight_score(dice)
    Choice -> choice_score(dice)
    Yacht -> yacht_score(dice)
  }
}

fn dice_counter(dice: List(Int)) -> List(#(Int, Int)) {
  dice
  |> list.group(function.identity)
  |> dict.map_values(fn(_key, value) { list.length(value) })
  |> dict.to_list
}

fn number_score(dice: List(Int), number: Int) -> Int {
  dice |> list.filter(fn(n) { n == number }) |> int.sum
}

fn full_house_score(dice: List(Int)) -> Int {
  case dice_counter(dice) {
    [#(number1, 2), #(number2, 3)] -> number1 * 2 + number2 * 3
    [#(number1, 3), #(number2, 2)] -> number1 * 3 + number2 * 2
    _ -> 0
  }
}

fn four_of_a_kind_score(dice: List(Int)) -> Int {
  case dice_counter(dice) {
    [#(_, 1), #(number2, 4)] -> number2 * 4
    [#(number1, 4), #(_, 1)] -> number1 * 4
    [#(number, 5)] -> number * 4
    _ -> 0
  }
}

fn little_straight_score(dice: List(Int)) -> Int {
  case dice |> list.sort(int.compare) {
    [1, 2, 3, 4, 5] -> 30
    _ -> 0
  }
}

fn big_straight_score(dice: List(Int)) -> Int {
  case dice |> list.sort(int.compare) {
    [2, 3, 4, 5, 6] -> 30
    _ -> 0
  }
}

fn choice_score(dice: List(Int)) -> Int {
  dice |> int.sum
}

fn yacht_score(dice: List(Int)) -> Int {
  case dice_counter(dice) {
    [#(_, 5)] -> 50
    _ -> 0
  }
}

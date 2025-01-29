import gleam/dict
import gleam/int
import gleam/list

pub type Error {
  ImpossibleTarget
}

pub fn find_fewest_coins(
  coins: List(Int),
  target: Int,
) -> Result(List(Int), Error) {
  case list.contains(coins, target) {
    True -> Ok([target])
    False -> {
      let coins = coins |> list.sort(int.compare)
      case coins {
        [] -> Error(ImpossibleTarget)
        [_, ..] if target == 0 -> Ok([])
        [lowest_value_coin, ..] if target < lowest_value_coin ->
          Error(ImpossibleTarget)
        [lowest_value_coin, ..] -> {
          let minimal_combination_per_amount =
            update_minimal_combination_per_amount(
              dict.new(),
              0,
              [],
              coins,
              coins,
            )
          do_find_fewest_coins(
            lowest_value_coin,
            target,
            minimal_combination_per_amount,
            coins,
          )
        }
      }
    }
  }
}

fn do_find_fewest_coins(amount, target, minimal_combination_per_amount, coins) {
  case amount {
    _ if amount == target ->
      case minimal_combination_per_amount |> dict.get(amount) {
        Ok(lst) -> Ok(lst |> list.sort(int.compare))
        Error(_) -> Error(ImpossibleTarget)
      }
    _ if amount < target ->
      case minimal_combination_per_amount |> dict.get(amount) {
        Error(_) ->
          do_find_fewest_coins(
            amount + 1,
            target,
            minimal_combination_per_amount,
            coins,
          )
        Ok(combination) ->
          do_find_fewest_coins(
            amount + 1,
            target,
            update_minimal_combination_per_amount(
              minimal_combination_per_amount,
              amount,
              combination,
              coins,
              coins,
            ),
            coins,
          )
      }
    _ -> panic as "Infinite loop ahead"
  }
}

fn update_minimal_combination_per_amount(
  minimal_combination_per_amount,
  amount,
  combination,
  coins,
  coins_to_process,
) {
  case coins_to_process {
    [] -> minimal_combination_per_amount
    [coin, ..rest_of_coins] ->
      case minimal_combination_per_amount |> dict.get(amount + coin) {
        Error(_) ->
          update_minimal_combination_per_amount(
            minimal_combination_per_amount
              |> dict.insert(amount + coin, [coin, ..combination]),
            amount,
            combination,
            coins,
            rest_of_coins,
          )
        Ok(existing_combination) ->
          case
            list.length(combination) + 1 < list.length(existing_combination)
          {
            True ->
              // better combination found
              update_minimal_combination_per_amount(
                minimal_combination_per_amount
                  |> dict.insert(amount + coin, [coin, ..combination]),
                amount,
                combination,
                coins,
                rest_of_coins,
              )
            False ->
              update_minimal_combination_per_amount(
                minimal_combination_per_amount,
                amount,
                combination,
                coins,
                rest_of_coins,
              )
          }
      }
  }
}

import gleam/list

pub type Pizza {
  Margherita
  Caprese
  Formaggio
  ExtraSauce(Pizza)
  ExtraToppings(Pizza)
}

pub fn pizza_price(pizza: Pizza) -> Int {
  pizza_price_accumulate(0, pizza)
}

fn pizza_price_accumulate(acc: Int, pizza: Pizza) -> Int {
  case pizza {
    Margherita -> acc + 7
    Caprese -> acc + 9
    Formaggio -> acc + 10
    ExtraSauce(base_pizza) -> pizza_price_accumulate(acc + 1, base_pizza)
    ExtraToppings(base_pizza) -> pizza_price_accumulate(acc + 2, base_pizza)
  }
}

pub fn order_price(order: List(Pizza)) -> Int {
  let pizzas_price =
    order
    |> list.fold(0, fn(acc: Int, pizza: Pizza) { acc + pizza_price(pizza) })
  case order {
    [] -> 0
    [_] -> pizzas_price + 3
    [_, _] -> pizzas_price + 2
    _ -> pizzas_price
  }
}

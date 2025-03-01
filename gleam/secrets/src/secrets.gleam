import gleam/int

pub fn secret_add(secret: Int) -> fn(Int) -> Int {
  int.add(_, secret)
}

pub fn secret_subtract(secret: Int) -> fn(Int) -> Int {
  int.subtract(_, secret)
}

pub fn secret_multiply(secret: Int) -> fn(Int) -> Int {
  int.multiply(_, secret)
}

pub fn secret_divide(secret: Int) -> fn(Int) -> Int {
  fn(x) {
    case int.floor_divide(x, secret) {
      Ok(n) -> n
      Error(_) -> panic as "No instruction what to do at this point"
    }
  }
}

pub fn secret_combine(
  secret_function1: fn(Int) -> Int,
  secret_function2: fn(Int) -> Int,
) -> fn(Int) -> Int {
  fn(x) {
    x
    |> secret_function1
    |> secret_function2
  }
}

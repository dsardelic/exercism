import gleam/list

pub fn prime(number: Int) -> Result(Int, Nil) {
  do_prime(2, 0, number, [])
}

fn do_prime(n, i, limit, primes) {
  case i == limit {
    True -> list.first(primes)
    False ->
      case is_prime(n, primes) {
        False -> do_prime(n + 1, i, limit, primes)
        True -> do_prime(n + 1, i + 1, limit, [n, ..primes])
      }
  }
}

fn is_prime(number, primes) {
  list.all(primes, fn(prime) { number % prime != 0 })
}

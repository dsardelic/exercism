import gleam/float
import gleam/list
import gleam/order.{type Order}

pub type City {
  City(name: String, temperature: Temperature)
}

pub type Temperature {
  Celsius(Float)
  Fahrenheit(Float)
}

pub fn fahrenheit_to_celsius(f: Float) -> Float {
  { f -. 32.0 } /. 1.8
}

pub fn compare_temperature(left: Temperature, right: Temperature) -> Order {
  case left, right {
    Fahrenheit(l), Fahrenheit(r) | Celsius(l), Celsius(r) -> float.compare(l, r)
    Fahrenheit(l), Celsius(r) -> float.compare(fahrenheit_to_celsius(l), r)
    Celsius(l), Fahrenheit(r) -> float.compare(l, fahrenheit_to_celsius(r))
  }
}

pub fn sort_cities_by_temperature(cities: List(City)) -> List(City) {
  list.sort(cities, by: fn(l, r) {
    compare_temperature(l.temperature, r.temperature)
  })
}

import gleam/list

pub fn wines_of_color(wines: List(Wine), color: Color) -> List(Wine) {
  wines |> list.filter(fn(wine) { wine.color == color })
}

pub fn wines_from_country(wines: List(Wine), country: String) -> List(Wine) {
  wines |> list.filter(fn(wine) { wine.country == country })
}

// Please define the required labelled arguments for this function
pub fn filter(
  wines: List(Wine),
  country country: String,
  color color: Color,
) -> List(Wine) {
  wines |> wines_from_country(country) |> wines_of_color(color)
}

pub type Wine {
  Wine(name: String, year: Int, country: String, color: Color)
}

pub type Color {
  Red
  Rose
  White
}

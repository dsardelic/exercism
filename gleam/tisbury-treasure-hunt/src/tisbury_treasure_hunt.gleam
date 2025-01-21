import gleam/list
import gleam/pair

pub fn place_location_to_treasure_location(
  place_location: #(String, Int),
) -> #(Int, String) {
  pair.swap(place_location)
}

pub fn treasure_location_matches_place_location(
  place_location: #(String, Int),
  treasure_location: #(Int, String),
) -> Bool {
  place_location_to_treasure_location(place_location) == treasure_location
}

pub fn count_place_treasures(
  place: #(String, #(String, Int)),
  treasures: List(#(String, #(Int, String))),
) -> Int {
  treasures
  |> list.fold(0, fn(acc: Int, treasure: #(String, #(Int, String))) {
    case treasure.1 == place_location_to_treasure_location(place.1) {
      True -> 1 + acc
      False -> acc
    }
  })
}

pub fn special_case_swap_possible(
  found_treasure: #(String, #(Int, String)),
  place: #(String, #(String, Int)),
  desired_treasure: #(String, #(Int, String)),
) -> Bool {
  let #(found_treasure_name, _) = found_treasure
  let #(place_name, _) = place
  let #(desired_treasure_name, _) = desired_treasure
  case found_treasure_name, place_name, desired_treasure_name {
    "Brass Spyglass", "Abandoned Lighthouse", _
    | "Amethyst Octopus", _, "Crystal Crab"
    | "Amethyst Octopus", "Stormy Breakwater", "Glass Starfish"
    | "Vintage Pirate Hat",
      "Harbor Managers Office",
      "Model Ship in Large Bottle"
    | "Vintage Pirate Hat",
      "Harbor Managers Office",
      "Antique Glass Fishnet Float"
    -> True
    _, _, _ -> False
  }
}

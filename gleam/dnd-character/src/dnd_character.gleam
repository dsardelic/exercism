import gleam/float
import gleam/int
import gleam/list
import gleam/order

pub type Character {
  Character(
    charisma: Int,
    constitution: Int,
    dexterity: Int,
    hitpoints: Int,
    intelligence: Int,
    strength: Int,
    wisdom: Int,
  )
}

pub fn generate_character() -> Character {
  let strength = ability()
  let dexterity = ability()
  let constitution = ability()
  let intelligence = ability()
  let wisdom = ability()
  let charisma = ability()
  let hitpoints = 10 + modifier(constitution)

  Character(
    strength:,
    dexterity:,
    constitution:,
    intelligence:,
    wisdom:,
    charisma:,
    hitpoints:,
  )
}

pub fn modifier(score: Int) -> Int {
  score
  |> int.subtract(10)
  |> int.to_float
  |> fn(x) { x /. 2.0 }
  |> float.floor
  |> float.truncate
}

pub fn ability() -> Int {
  let rolls = [
    int.random(6) + 1,
    int.random(6) + 1,
    int.random(6) + 1,
    int.random(6) + 1,
  ]

  rolls
  |> list.sort(int.compare |> order.reverse)
  |> list.take(3)
  |> int.sum
}

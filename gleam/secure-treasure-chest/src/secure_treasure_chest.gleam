import gleam/string

pub opaque type TreasureChest(a) {
  TreasureChest(password: String, treasure: a)
}

pub fn create(
  password: String,
  contents: treasure,
) -> Result(TreasureChest(treasure), String) {
  case string.length(password) {
    length if length < 8 -> Error("Password must be at least 8 characters long")
    _ -> Ok(TreasureChest(password, contents))
  }
}

pub fn open(
  chest: TreasureChest(treasure),
  password: String,
) -> Result(treasure, String) {
  case password == chest.password {
    True -> Ok(chest.treasure)
    False -> Error("Incorrect password")
  }
}

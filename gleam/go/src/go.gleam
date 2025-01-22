import gleam/result

pub type Player {
  Black
  White
}

pub type Game {
  Game(
    white_captured_stones: Int,
    black_captured_stones: Int,
    player: Player,
    error: String,
  )
}

pub fn apply_rules(
  game: Game,
  rule1: fn(Game) -> Result(Game, String),
  rule2: fn(Game) -> Game,
  rule3: fn(Game) -> Result(Game, String),
  rule4: fn(Game) -> Result(Game, String),
) -> Game {
  case game |> rule1 |> result.try(rule3) |> result.try(rule4) {
    Ok(game) ->
      case game.player {
        Black -> Game(..game, player: White) |> rule2
        White -> Game(..game, player: Black) |> rule2
      }
    Error(str) -> Game(..game, error: str)
  }
}

import gleam/dict.{type Dict}

pub type ScoreBoard =
  Dict(String, Int)

pub fn create_score_board() -> ScoreBoard {
  dict.from_list([#("The Best Ever", 1_000_000)])
}

pub fn add_player(
  score_board: ScoreBoard,
  player: String,
  score: Int,
) -> ScoreBoard {
  dict.insert(score_board, player, score)
}

pub fn remove_player(score_board: ScoreBoard, player: String) -> ScoreBoard {
  dict.delete(score_board, player)
}

pub fn update_score(
  score_board: ScoreBoard,
  player: String,
  points: Int,
) -> ScoreBoard {
  case dict.get(score_board, player) {
    Ok(current_points) ->
      dict.insert(score_board, player, points + current_points)
    Error(_) -> score_board
  }
}

pub fn apply_monday_bonus(score_board: ScoreBoard) -> ScoreBoard {
  dict.map_values(score_board, fn(_key, value) { value + 100 })
}

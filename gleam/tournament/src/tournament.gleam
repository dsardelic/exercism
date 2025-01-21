import gleam/dict
import gleam/int
import gleam/list
import gleam/option.{None, Some}
import gleam/order.{type Order, Gt, Lt}
import gleam/string

type Stats {
  Stats(played: Int, wins: Int, draws: Int, losses: Int, points: Int)
}

type Standings =
  dict.Dict(String, Stats)

type Outcome {
  WIN
  LOSS
  DRAW
}

pub fn tally(input: String) -> String {
  case input {
    "" -> table_to_string([])
    _ ->
      input
      |> string.split("\n")
      |> list.fold(dict.new(), input_rows_folder)
      |> dict.to_list
      |> list.sort(table_data_comparer)
      |> list.reverse
      |> table_to_string
  }
}

fn input_rows_folder(standings: Standings, row: String) -> Standings {
  let assert [team1, team2, outcome] = string.split(row, ";")
  case outcome {
    "win" -> {
      standings |> process_outcome(team1, WIN) |> process_outcome(team2, LOSS)
    }
    "loss" -> {
      standings |> process_outcome(team1, LOSS) |> process_outcome(team2, WIN)
    }
    "draw" -> {
      standings |> process_outcome(team1, DRAW) |> process_outcome(team2, DRAW)
    }
    _ -> panic as "Invalid outcome"
  }
}

fn process_outcome(
  standings: Standings,
  team: String,
  outcome: Outcome,
) -> Standings {
  dict.upsert(standings, team, fn(stats) {
    case stats {
      None -> update_stats(Stats(0, 0, 0, 0, 0), outcome)
      Some(stats) -> update_stats(stats, outcome)
    }
  })
}

fn update_stats(stats: Stats, outcome: Outcome) -> Stats {
  case stats, outcome {
    Stats(played, wins, draws, losses, points), WIN ->
      Stats(played + 1, wins + 1, draws, losses, points + 3)
    Stats(played, wins, draws, losses, points), DRAW ->
      Stats(played + 1, wins, draws + 1, losses, points + 1)
    Stats(played, wins, draws, losses, points), LOSS ->
      Stats(played + 1, wins, draws, losses + 1, points)
  }
}

fn table_data_comparer(left: #(String, Stats), right: #(String, Stats)) -> Order {
  case left, right {
    #(_, l_stats), #(_, r_stats) if l_stats.points < r_stats.points -> Lt
    #(_, l_stats), #(_, r_stats) if l_stats.points > r_stats.points -> Gt
    #(l_name, _), #(r_name, _) -> string.compare(r_name, l_name)
  }
}

fn table_to_string(table_data: List(#(String, Stats))) -> String {
  let table_header = "Team                           | MP |  W |  D |  L |  P"
  let table_data_rows = table_data |> list.map(table_data_mapper)
  [table_header, ..table_data_rows] |> string.join("\n")
}

fn table_data_mapper(row_data: #(String, Stats)) {
  case row_data {
    #(name, Stats(played, wins, draws, losses, points)) ->
      [
        string.pad_right(name, 30, " "),
        string.pad_left(int.to_string(played), 2, " "),
        string.pad_left(int.to_string(wins), 2, " "),
        string.pad_left(int.to_string(draws), 2, " "),
        string.pad_left(int.to_string(losses), 2, " "),
        string.pad_left(int.to_string(points), 2, " "),
      ]
      |> string.join(" | ")
  }
}

import gleam/string

pub type Robot {
  Robot(direction: Direction, position: Position)
}

pub type Direction {
  North
  East
  South
  West
}

pub type Position {
  Position(x: Int, y: Int)
}

pub fn create(direction: Direction, position: Position) -> Robot {
  Robot(direction, position)
}

pub fn move(
  direction: Direction,
  position: Position,
  instructions: String,
) -> Robot {
  do_move(create(direction, position), instructions |> string.to_graphemes)
}

fn do_move(robot: Robot, instructions: List(String)) -> Robot {
  case instructions {
    [] -> robot
    [instruction, ..rest] -> {
      case instruction {
        "A" ->
          do_move(
            Robot(robot.direction, advance(robot.position, robot.direction)),
            rest,
          )
        "L" -> do_move(Robot(turn_left(robot.direction), robot.position), rest)
        "R" -> do_move(Robot(turn_right(robot.direction), robot.position), rest)
        _ -> panic as "Unknown instruction"
      }
    }
  }
}

fn turn_left(direction: Direction) -> Direction {
  case direction {
    North -> West
    East -> North
    South -> East
    West -> South
  }
}

fn turn_right(direction: Direction) -> Direction {
  case direction {
    North -> East
    East -> South
    South -> West
    West -> North
  }
}

fn advance(position: Position, direction: Direction) -> Position {
  case direction {
    North -> Position(position.x, position.y + 1)
    East -> Position(position.x + 1, position.y)
    South -> Position(position.x, position.y - 1)
    West -> Position(position.x - 1, position.y)
  }
}

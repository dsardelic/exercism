import gleam/list
import gleam/string

pub type Student {
  Alice
  Bob
  Charlie
  David
  Eve
  Fred
  Ginny
  Harriet
  Ileana
  Joseph
  Kincaid
  Larry
}

pub type Plant {
  Radishes
  Clover
  Violets
  Grass
}

pub fn plants(diagram: String, student: Student) -> List(Plant) {
  let class = [
    Alice,
    Bob,
    Charlie,
    David,
    Eve,
    Fred,
    Ginny,
    Harriet,
    Ileana,
    Joseph,
    Kincaid,
    Larry,
  ]

  let plants_rows =
    diagram |> string.split("\n") |> list.map(string.to_graphemes)

  plants_loop(plants_rows, class, student)
}

fn plants_loop(
  plants_rows: List(List(String)),
  class: List(Student),
  student: Student,
) {
  case plants_rows, class {
    [[char_11, char_12, ..rest_row_1], [char_21, char_22, ..rest_row_2]],
      [some_student, ..rest_of_class]
    -> {
      case some_student == student {
        True -> [
          char_to_plant(char_11),
          char_to_plant(char_12),
          char_to_plant(char_21),
          char_to_plant(char_22),
        ]
        False -> plants_loop([rest_row_1, rest_row_2], rest_of_class, student)
      }
    }
    _, _ -> panic as "Invalid data"
  }
}

fn char_to_plant(char: String) -> Plant {
  case char {
    "G" -> Grass
    "C" -> Clover
    "R" -> Radishes
    "V" -> Violets
    _ -> panic as { "Invalid diagram entry: " <> char }
  }
}

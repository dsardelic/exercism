import gleam/list
import gleam/string

pub fn is_paired(value: String) -> Bool {
  validate(value |> string.to_graphemes, list.new())
}

fn validate(graphemes: List(String), stack: List(String)) -> Bool {
  case graphemes, stack {
    [], stack -> stack |> list.is_empty
    [gs_h, ..gs_t], [] -> {
      case gs_h {
        "(" | "[" | "{" -> validate(gs_t, [gs_h])
        ")" | "]" | "}" -> False
        _ -> validate(gs_t, [])
      }
    }
    [gs_h, ..gs_t], [stack_h, ..stack_t] -> {
      case gs_h, stack_h {
        "(", _ | "[", _ | "{", _ -> validate(gs_t, [gs_h, ..stack])
        ")", "(" | "]", "[" | "}", "{" -> validate(gs_t, stack_t)
        ")", _ | "]", _ | "}", _ -> False
        _, _ -> validate(gs_t, stack)
      }
    }
  }
}

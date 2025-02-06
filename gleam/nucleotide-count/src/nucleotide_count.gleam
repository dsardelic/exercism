import gleam/dict.{type Dict}
import gleam/result
import gleam/string

pub fn nucleotide_count(dna: String) -> Result(Dict(String, Int), Nil) {
  do_nucleotide_count(
    dna |> string.to_graphemes,
    dict.from_list([#("A", 0), #("C", 0), #("G", 0), #("T", 0)]),
  )
}

fn do_nucleotide_count(dna, counter) {
  case dna {
    [] -> Ok(counter)
    [nucleotide, ..rest] ->
      result.try(dict.get(counter, nucleotide), fn(count) {
        do_nucleotide_count(rest, dict.insert(counter, nucleotide, count + 1))
      })
  }
}

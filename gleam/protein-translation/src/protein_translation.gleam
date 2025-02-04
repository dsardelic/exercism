import gleam/list
import gleam/string

pub fn proteins(rna: String) -> Result(List(String), Nil) {
  rna
  |> string.to_graphemes
  |> list.sized_chunk(3)
  |> list.map(string.concat)
  |> proteins_loop([])
}

pub fn proteins_loop(lst, acc) {
  case lst {
    [] -> Ok(list.reverse(acc))
    ["AUG", ..rest] -> proteins_loop(rest, ["Methionine", ..acc])
    ["UUU", ..rest] | ["UUC", ..rest] ->
      proteins_loop(rest, ["Phenylalanine", ..acc])
    ["UUA", ..rest] | ["UUG", ..rest] -> proteins_loop(rest, ["Leucine", ..acc])
    ["UCU", ..rest] | ["UCC", ..rest] | ["UCA", ..rest] | ["UCG", ..rest] ->
      proteins_loop(rest, ["Serine", ..acc])
    ["UAU", ..rest] | ["UAC", ..rest] ->
      proteins_loop(rest, ["Tyrosine", ..acc])
    ["UGU", ..rest] | ["UGC", ..rest] ->
      proteins_loop(rest, ["Cysteine", ..acc])
    ["UGG", ..rest] -> proteins_loop(rest, ["Tryptophan", ..acc])
    ["UAA", ..] | ["UAG", ..] | ["UGA", ..] -> Ok(list.reverse(acc))
    _ -> Error(Nil)
  }
}

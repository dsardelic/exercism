import gleam/list
import gleam/result
import gleam/string

pub fn to_rna(dna: String) -> Result(String, Nil) {
  dna
  |> string.to_graphemes
  |> list.try_map(fn(nucleotide) {
    case nucleotide {
      "A" -> Ok("U")
      "C" -> Ok("G")
      "G" -> Ok("C")
      "T" -> Ok("A")
      _ -> Error(Nil)
    }
  })
  |> result.map(string.join(_, ""))
}

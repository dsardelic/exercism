import gleam/list

pub type Nucleotide {
  Adenine
  Cytosine
  Guanine
  Thymine
}

pub fn encode_nucleotide(nucleotide: Nucleotide) -> Int {
  case nucleotide {
    Adenine -> 0b00
    Cytosine -> 0b01
    Guanine -> 0b10
    Thymine -> 0b11
  }
}

pub fn decode_nucleotide(nucleotide: Int) -> Result(Nucleotide, Nil) {
  case nucleotide {
    0b00 -> Ok(Adenine)
    0b01 -> Ok(Cytosine)
    0b10 -> Ok(Guanine)
    0b11 -> Ok(Thymine)
    _ -> Error(Nil)
  }
}

pub fn encode(dna: List(Nucleotide)) -> BitArray {
  dna
  |> list.fold(<<>>, fn(acc: BitArray, nucleotide) {
    <<acc:bits, encode_nucleotide(nucleotide):2>>
  })
}

pub fn decode(dna: BitArray) -> Result(List(Nucleotide), Nil) {
  do_decode([], dna)
}

fn do_decode(acc: List(Nucleotide), dna: BitArray) {
  case dna {
    <<>> -> Ok(list.reverse(acc))
    <<code:2, rest:bits>> ->
      case decode_nucleotide(code) {
        Ok(nucleotide) -> do_decode([nucleotide, ..acc], rest)
        Error(Nil) -> Error(Nil)
      }
    _ -> Error(Nil)
  }
}

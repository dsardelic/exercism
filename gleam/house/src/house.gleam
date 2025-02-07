import gleam/list
import gleam/string

const all_whats_and_whos = [
  #("lay in", "the house that Jack built"),
  #("ate", "the malt"),
  #("killed", "the rat"),
  #("worried", "the cat"),
  #("tossed", "the dog"),
  #("milked", "the cow with the crumpled horn"),
  #("kissed", "the maiden all forlorn"),
  #("married", "the man all tattered and torn"),
  #("woke", "the priest all shaven and shorn"),
  #("kept", "the rooster that crowed in the morn"),
  #("belonged to", "the farmer sowing his corn"),
  #("", "the horse and the hound and the horn"),
]

pub fn recite(start_verse start_verse: Int, end_verse end_verse: Int) -> String {
  do_recite(start_verse, end_verse, [])
}

fn do_recite(start_verse, end_verse, acc) {
  case start_verse > end_verse {
    True -> acc |> list.reverse |> string.join("\n")
    False ->
      do_recite(start_verse + 1, end_verse, [
        verse(all_whats_and_whos |> list.take(start_verse) |> list.reverse),
        ..acc
      ])
  }
}

fn verse(whats_and_whos) {
  let assert [#(_what, who), ..rest] = whats_and_whos
  "This is " <> who <> subverse(rest)
}

fn subverse(whats_and_whos) {
  case whats_and_whos {
    [#(what, who), ..rest] -> " that " <> what <> " " <> who <> subverse(rest)
    _ -> "."
  }
}

import gleam/list
import gleam/string

pub fn find_anagrams(word: String, candidates: List(String)) -> List(String) {
  let all_anagrams =
    word
    |> string.to_graphemes
    |> list.permutations
    |> list.map(fn(list) { string.join(list, "") })
    |> list.filter(fn(anagram) {
      string.uppercase(anagram) != string.uppercase(word)
    })

  candidates
  |> list.filter(fn(candidate) {
    list.any(all_anagrams, fn(anagram) {
      string.uppercase(anagram) == string.uppercase(candidate)
    })
  })
}

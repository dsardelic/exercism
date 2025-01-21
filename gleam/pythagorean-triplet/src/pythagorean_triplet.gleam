import gleam/iterator.{Done, Next}

pub type Triplet {
  Triplet(Int, Int, Int)
}

pub fn triplets_with_sum(sum: Int) -> List(Triplet) {
  // shave off some execution time
  let xs_iterator = iterator.range(1, sum / 3)

  let x_to_triplets = fn(x: Int) {
    iterator.unfold(from: x + 1, with: fn(y: Int) {
      let z = sum - x - y
      case y < z {
        False -> Done
        True -> Next(element: Triplet(x, y, z), accumulator: y + 1)
      }
    })
  }

  let is_valid_triplet = fn(triplet: Triplet) {
    case triplet {
      Triplet(x, y, z) if x * x + y * y == z * z -> True
      _ -> False
    }
  }

  xs_iterator
  |> iterator.flat_map(x_to_triplets)
  |> iterator.filter(is_valid_triplet)
  |> iterator.to_list
}

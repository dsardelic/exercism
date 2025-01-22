import gleam/float

pub fn score(x: Float, y: Float) -> Int {
  case float.square_root(x *. x +. y *. y) {
    Ok(distance) if distance <=. 1.0 -> 10
    Ok(distance) if distance <=. 5.0 -> 5
    Ok(distance) if distance <=. 10.0 -> 1
    _ -> 0
  }
}

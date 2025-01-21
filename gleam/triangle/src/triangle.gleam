import gleam/list

pub fn equilateral(a: Float, b: Float, c: Float) -> Bool {
  valid_triangle(a, b, c) && a == b && a == c
}

pub fn isosceles(a: Float, b: Float, c: Float) -> Bool {
  valid_triangle(a, b, c) && { a == b || a == c || b == c }
}

pub fn scalene(a: Float, b: Float, c: Float) -> Bool {
  valid_triangle(a, b, c) && !{ a == b || a == c || b == c }
}

fn valid_triangle(a: Float, b: Float, c: Float) -> Bool {
  list.all([a, b, c], fn(x) { x >. 0.0 })
  && a +. b >. c
  && a +. c >. b
  && b +. c >. a
}

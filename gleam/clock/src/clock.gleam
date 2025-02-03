import gleam/int
import gleam/string

pub type Clock {
  Clock(hours: Int, minutes: Int)
}

pub fn create(hour hour: Int, minute minute: Int) -> Clock {
  handle_negative_values({ minute / 60 + hour } % 24, minute % 60)
}

fn handle_negative_values(hours, minutes) {
  case hours, minutes {
    _, _ if minutes < 0 -> handle_negative_values(hours - 1, minutes + 60)
    _, _ if hours < 0 -> handle_negative_values(hours + 24, minutes)
    _, _ -> Clock(hours, minutes)
  }
}

pub fn add(clock: Clock, minutes minutes: Int) -> Clock {
  create(clock.hours, clock.minutes + minutes)
}

pub fn subtract(clock: Clock, minutes minutes: Int) -> Clock {
  add(clock, -minutes)
}

pub fn display(clock: Clock) -> String {
  string.pad_left(int.to_string(clock.hours), 2, "0")
  <> ":"
  <> string.pad_left(int.to_string(clock.minutes), 2, "0")
}

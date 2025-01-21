pub fn expected_minutes_in_oven() -> Int {
  40
}

pub fn remaining_minutes_in_oven(time_in_oven: Int) -> Int {
  expected_minutes_in_oven() - time_in_oven
}

pub fn preparation_time_in_minutes(no_of_layers: Int) -> Int {
  2 * no_of_layers
}

pub fn total_time_in_minutes(no_of_layers: Int, time_in_oven: Int) -> Int {
  preparation_time_in_minutes(no_of_layers) + time_in_oven
}

pub fn alarm() -> String {
  "Ding!"
}

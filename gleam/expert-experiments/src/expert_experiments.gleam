import gleam/result

pub fn with_retry(experiment: fn() -> Result(t, e)) -> Result(t, e) {
  case experiment() {
    Ok(value) -> Ok(value)
    Error(_) -> experiment()
  }
}

pub fn record_timing(
  time_logger: fn() -> Nil,
  experiment: fn() -> Result(t, e),
) -> Result(t, e) {
  time_logger()
  let outcome = experiment()
  time_logger()
  outcome
}

pub fn run_experiment(
  name: String,
  setup: fn() -> Result(t, e),
  action: fn(t) -> Result(u, e),
  record: fn(t, u) -> Result(v, e),
) -> Result(#(String, v), e) {
  use setup_result <- result.try(setup())
  use action_result <- result.try(action(setup_result))
  use recording_data <- result.try(record(setup_result, action_result))
  Ok(#(name, recording_data))
}

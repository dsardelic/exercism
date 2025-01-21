from dataclasses import dataclass


@dataclass(frozen=True)
class FilledVolumes:
    one: int
    two: int

    def increase_by(self, delta_one, delta_two):
        return self.__class__(self.one + delta_one, self.two + delta_two)


def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > bucket_one and goal > bucket_two:
        raise ValueError(f"Neither bucket can hold {goal} litres.")
    visited = {FilledVolumes(0, 0)}
    unprocessed = fill(bucket_one, bucket_two, FilledVolumes(0, 0), start_bucket)
    action_count = 1
    while unprocessed:
        new_uprocessed = set()
        for filled_volumes in unprocessed:
            if filled_volumes in visited or is_illegal_state(
                bucket_one, bucket_two, filled_volumes, start_bucket
            ):
                continue
            if goal in (filled_volumes.one, filled_volumes.two):
                return (
                    action_count,
                    "one" if goal == filled_volumes.one else "two",
                    (
                        filled_volumes.two
                        if goal == filled_volumes.one
                        else filled_volumes.one
                    ),
                )
            new_uprocessed = new_uprocessed.union(
                *(
                    action(bucket_one, bucket_two, filled_volumes, bucket_id)
                    for action in (pour, empty, fill)
                    for bucket_id in ("one", "two")
                )
            )
            visited.add(filled_volumes)
        unprocessed = new_uprocessed
        action_count += 1
    raise ValueError("Desired water quantity cannot be achieved.")


def pour(bucket_one, bucket_two, filled_volumes, bucket_id):
    return {
        "one": pour_from_bucket_one,
        "two": pour_from_bucket_two,
    }[
        bucket_id
    ](bucket_one, bucket_two, filled_volumes)


def pour_from_bucket_one(_, bucket_two, filled_volumes):
    can_pour_out = filled_volumes.one
    can_take_in = bucket_two - filled_volumes.two
    if can_pour_out < can_take_in:
        return {filled_volumes.increase_by(-can_pour_out, can_pour_out)}
    if can_pour_out > can_take_in:
        return {filled_volumes.increase_by(-can_take_in, can_take_in)}
    return {
        filled_volumes.increase_by(-can_pour_out, can_pour_out),
        filled_volumes.increase_by(-can_take_in, can_take_in),
    }


def pour_from_bucket_two(bucket_one, _, filled_volumes):
    can_take_in = bucket_one - filled_volumes.one
    can_pour_out = filled_volumes.two
    if can_pour_out < can_take_in:
        return {filled_volumes.increase_by(can_pour_out, -can_pour_out)}
    if can_pour_out > can_take_in:
        return {filled_volumes.increase_by(can_take_in, -can_take_in)}
    return {
        filled_volumes.increase_by(can_pour_out, -can_pour_out),
        filled_volumes.increase_by(can_take_in, -can_take_in),
    }


def empty(_bucket_one, _bucket_two, filled_volumes, bucket_id):
    return {
        {
            "one": FilledVolumes(0, filled_volumes.two),
            "two": FilledVolumes(filled_volumes.one, 0),
        }[bucket_id]
    }


def fill(bucket_one, bucket_two, filled_volumes, bucket_id):
    return {
        {
            "one": FilledVolumes(bucket_one, filled_volumes.two),
            "two": FilledVolumes(filled_volumes.one, bucket_two),
        }[bucket_id]
    }


def is_illegal_state(bucket_one, bucket_two, filled_volumes, start_bucket):
    return (
        start_bucket == "one"
        and not filled_volumes.one
        and filled_volumes.two == bucket_two
    ) or (
        start_bucket == "two"
        and not filled_volumes.two
        and filled_volumes.one == bucket_one
    )

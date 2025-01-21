from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    id_: int
    weight: int
    value: int


def maximum_value(maximum_weight, items_data):
    max_values_per_weight = defaultdict(int)
    max_value_item_sets_per_weight = defaultdict(set)

    items = sorted(
        (
            Item(item_index, item["weight"], item["value"])
            for item_index, item in enumerate(items_data)
        ),
        key=lambda item: (item.weight, -item.value),
    )

    not_too_heavy_items = [item for item in items if item.weight <= maximum_weight]
    if not not_too_heavy_items:
        return 0
    for item in not_too_heavy_items:
        if not max_values_per_weight[item.weight]:
            max_values_per_weight[item.weight] = item.value
            max_value_item_sets_per_weight[item.weight] = {frozenset([item])}

    for weight in range(maximum_weight + 1):
        for item_set in max_value_item_sets_per_weight[weight]:
            for item in not_too_heavy_items:
                if weight + item.weight > maximum_weight:
                    break
                if item not in item_set:
                    if (
                        max_values_per_weight[weight] + item.value
                        > max_values_per_weight[weight + item.weight]
                    ):
                        max_values_per_weight[weight + item.weight] = (
                            max_values_per_weight[weight] + item.value
                        )
                        max_value_item_sets_per_weight[weight + item.weight] = {
                            frozenset([*item_set, item])
                        }
                    elif (
                        max_values_per_weight[weight] + item.value
                        == max_values_per_weight[weight + item.weight]
                    ):
                        max_value_item_sets_per_weight[weight + item.weight].add(
                            frozenset([*item_set, item])
                        )

    return max(max_values_per_weight.values())

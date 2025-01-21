def flatten(iterable):
    def flatten_items():
        for item in iterable:
            if isinstance(item, list):
                yield from flatten(item)
            elif item is not None and item != "null":
                yield item

    return list(flatten_items())

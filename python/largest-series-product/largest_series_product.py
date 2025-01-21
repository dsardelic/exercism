def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if not all(item.isdigit() for item in series):
        raise ValueError("digits input must only contain digits")
    max_product = 0
    lo_ix = 0
    while lo_ix < len(series) and series[lo_ix] == "0":
        lo_ix += 1
    hi_ix = lo_ix
    product = 1
    while hi_ix < len(series):
        if series[hi_ix] == "0":
            lo_ix, hi_ix = hi_ix + 1, hi_ix + 1
            product = 1
        else:
            product *= int(series[hi_ix])
            if hi_ix - lo_ix == size:
                product //= int(series[lo_ix])
                lo_ix += 1
            if hi_ix - lo_ix >= size - 1:
                max_product = max(max_product, product)
            hi_ix += 1
    return max_product

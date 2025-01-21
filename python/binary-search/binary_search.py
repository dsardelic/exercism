def find(search_list, value):
    def find_in_range(min_index, max_index):
        if min_index >= max_index:
            raise ValueError("value not in array")
        mid_index = (max_index + min_index) // 2
        if search_list[mid_index] > value:
            return find_in_range(min_index, mid_index)
        if search_list[mid_index] < value:
            return find_in_range(mid_index + 1, max_index)
        return mid_index

    if not search_list:
        raise ValueError("value not in array")
    if value < search_list[0] or value > search_list[-1]:
        raise ValueError("value not in array")
    return find_in_range(0, len(search_list))

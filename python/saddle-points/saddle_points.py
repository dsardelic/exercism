def saddle_points(matrix):
    if not matrix:
        return []
    max_row_heights = []
    min_col_heights = [float("inf")] * len(matrix[0])
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")
        max_row_heights.append(max(row))
        for col_index, height in enumerate(row):
            min_col_heights[col_index] = min(min_col_heights[col_index], height)
    return [
        {"row": i + 1, "column": j + 1}
        for i, max_row_height in enumerate(max_row_heights)
        for j, min_col_height in enumerate(min_col_heights)
        if max_row_height == min_col_height
    ]

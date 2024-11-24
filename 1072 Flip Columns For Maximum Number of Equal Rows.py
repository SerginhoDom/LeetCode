def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:
    seen = {}
    max_count = 1

    for row in matrix:
        row_tuple = tuple(row)
        flipped_row_tuple = tuple(1 - value for value in row)

        for current_row in [row_tuple, flipped_row_tuple]:
            if current_row in seen:
                seen[current_row] += 1
            else:
                seen[current_row] = 1

            max_count = max(max_count, seen[current_row])

    return max_count


matrix = [[0, 1], [1, 0]]
print(maxEqualRowsAfterFlips(matrix))
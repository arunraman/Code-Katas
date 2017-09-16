# Count the possible paths from top left to bottom right of a mXn matrix
def num_paths_matrix_recursive(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return num_paths_matrix_recursive(rows - 1, cols) + num_paths_matrix_recursive(rows, cols - 1)

print num_paths_matrix_recursive(3, 3)
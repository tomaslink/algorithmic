from typing import List


def rotate_matrix(matrix: List[List]) -> None:
    """Rotates a matrix (in-place) 90 degrees clock-wise.

    Complexity:
    - Time: O(N^2)
    - Space: O(N^2)
    """
    if len(matrix) != len(matrix[0]):
        raise ValueError("Input matrix must be square.")

    n = len(matrix)

    for layer in range(n // 2):
        start = layer
        end = n - 1 - layer
        for i in range(start, end):
            offset = i - start
            top = matrix[start][i]

            matrix[start][i] = matrix[end - offset][start]
            matrix[end - offset][start] = matrix[end][end - offset]
            matrix[end][end - offset] = matrix[i][end]
            matrix[i][end] = top


def set_zeros(matrix: List[List]) -> None:
    """Modifies a matrix (in-place), so that if an element of it is zero,
        its entire row and column are set to zero.

    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """

    def nullify_row(matrix, i):
        matrix[i] = [0 for _ in matrix[i]]

    def nullify_column(matrix, j):
        for row in matrix:
            row[j] = 0

    def contains_zero(vector):
        for v in vector:
            if v == 0:
                return True

        return False

    first_row_has_zero = contains_zero(matrix[0])
    first_column_has_zero = contains_zero([row[0] for row in matrix])

    # We use first row and first column to reference which rows and columns must be nullified.
    # This way we can reach O(1) space.
    for i, row in enumerate(matrix[1:], 1):
        for j, cell in enumerate(row[1:], 1):
            if cell == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify rows in the rest of the matrix based on the values in the first column
    for i, row in enumerate(matrix[1:], 1):
        if row[0] == 0:
            nullify_row(matrix, i)

    # Nullify columns in the rest of the matrix based on the values in the first row
    for j, cell in enumerate(matrix[0][1:], 1):
        if cell == 0:
            nullify_column(matrix, j)

    if first_row_has_zero:
        nullify_row(matrix, 0)

    if first_column_has_zero:
        nullify_column(matrix, 0)

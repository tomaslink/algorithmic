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

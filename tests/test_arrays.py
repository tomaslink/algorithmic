import pytest

from algorithmic import arrays


def print_matrix(matrix):
    print("")
    for s in matrix:
        print(s)


def test_rotate_matrix():
    matrix = [[1, 2], [3, 4]]
    arrays.rotate_matrix(matrix)
    assert matrix == [[3, 1], [4, 2]]

    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        arrays.rotate_matrix(matrix)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arrays.rotate_matrix(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_zero_matrix():
    matrix = [[1, 2], [3, 4]]
    arrays.zero_matrix(matrix)
    assert matrix == [[1, 2], [3, 4]]

    matrix = [[1, 0], [3, 4]]
    arrays.zero_matrix(matrix)
    assert matrix == [[0, 0], [3, 0]]

    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    arrays.zero_matrix(matrix)
    assert matrix == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    matrix = [[1, 0, 0], [4, 5, 6], [7, 8, 9]]
    arrays.zero_matrix(matrix)
    assert matrix == [[0, 0, 0], [4, 0, 0], [7, 0, 0]]

import pytest

from algorithmic import arrays


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

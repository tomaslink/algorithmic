"""Algorithms for string manipulation."""

from typing import Generator

ASCII_MAX_LENGTH = 128
ASCII_EMPTY_SPACE = 32


def unique(string: str) -> bool:
    """Determines whether an ASCII string has all unique characters.

    Time: O(N).
    Space: O(1).string

    Where N is the length of the string.
    Since we have a fixed maximum for N, we could also think the time complexity as O(1).

    Args:
        string: the string to be tested.
    """

    if len(string) > ASCII_MAX_LENGTH:
        return False

    chars = set()
    for char in string:
        if char in chars:
            return False

        chars.add(char)

    return True


def check_permutation(s1: str, s2: str) -> bool:
    """Given two ASCII strings, determines whether one is a permutation of the other.

    The algorithm is case-sensitive.

    Time: O(N * log(N)).
    Space: O(N).

    Where N = max(A, B) and A, B are the lengths of the strings s1 and s2, respectively.

    This is not the most time efficient algorithm.
        If we calculate character counts in each string and compare, we can reach O(N).

    Args:
        s1: first string.
        s2: second string.
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)  # TimSort.


def urlify(string: bytearray, true_length: int) -> None:
    """Given an ASCII string represented as a bytearray,
        replaces all spaces in the string with '%20'.

    The replacement is done in-place and the algorithm assumes
        that the string has sufficient space at the end to hold the additional characters.

    Time: O(N).
    Space: O(M).

    Where N is the true length and M the length of string.

    Args:
        string: the string to modify.
        true_length: the "true" length, i.e., without the extra space at the end.
    """
    space_count = 0
    for i in range(true_length):
        if string[i] == ASCII_EMPTY_SPACE:
            space_count += 1

    # reverse pass
    index = true_length + space_count * 2

    i = true_length - 1
    while i >= 0:
        if string[i] == ASCII_EMPTY_SPACE:
            string[index - 1] = ord('0')
            string[index - 2] = ord('2')
            string[index - 3] = ord('%')
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1

        i -= 1


def permutations(string: str) -> Generator[str, None, None]:
    """Returns a generator with all permutations of a string.

    Exercising the full generator will produce:
    - Time: O(N!).
    - Space: O(N!).

    Args:
        string: the string to do permutations with.

    Returns:
        generator for the permutations.
    """
    if len(string) == 0:
        yield string
    else:
        for i, c in enumerate(string):
            for perm in permutations(string[:i] + string[i + 1:]):
                yield c + perm

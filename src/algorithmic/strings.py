"""Algorithms for string manipulation."""

from typing import Generator

ASCII_MAX_LENGTH = 128
ASCII_EMPTY_SPACE = 32


def unique(string: str) -> bool:
    """Determines whether an ASCII string has all unique characters.

    - Time: O(N).
    - Space: O(1)

    Where N is the length of the string.
    Since we have a fixed maximum for N, we could also think the time complexity as O(1).

    Args:
        string: the string to be tested.

    Notes:

    1. We can reduce our space usage by a factor of eight by using a bit vector (TODO).
    2. If can't use additional data structures like set(), these are alternative implementations:
        - Compare every character of the string to every other character of the string.
            - Time: 0(N^2)
            - Space: 0(1).
        - If we are allowed to modify the input string:
            - Sort the string and linearly check for neighboring characters that are identical.
            - Time: O(N * log(N)) (the sorting part).
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

    - Time: O(N * log(N)).
    - Space: O(N).

    Where N = max(A, B) and A, B are the lengths of the strings s1 and s2, respectively.

    This is not the most time efficient algorithm.
        If we calculate character counts in each string and compare, we can reach O(N).

    Args:
        s1: first string.
        s2: second string.
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)  # TODO: implement TimSort.


def urlify(string: bytearray, true_length: int) -> None:
    """Given an ASCII string represented as a bytearray,
        replaces all spaces in the string with '%20'.

    The replacement is done in-place and the algorithm assumes
        that the string has sufficient space at the end to hold the additional characters.

    - Time: O(N).
    - Space: O(M).

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


def palindrome_permutation(string: str) -> bool:
    """Determines if a string is a palindrome permutation.

    In here, a palindrome is a word or phrase that,
        removed its spaces and all lowercase, is the same forward than backwards.

    This algorithms exploits the fact that if a string is a palindrome,
        at the most 1 character has an odd count of occurrences
        (the one in the middle for an odd string)

    - Time: O(N).
    - Space: O(N).
    """

    string = string.replace(" ", "")
    string = string.lower()

    occurrences = {word: 0 for word in set(string)}

    for word in string:
        occurrences[word] += 1

    odd_counts = 0
    for count in occurrences.values():
        odd_counts += count % 2

    return odd_counts <= 1


def is_palindrome(string: str) -> bool:
    """Determines whether a string is a palindrome."""
    string = string.replace(" ", "")
    string = string.lower()

    return string == string[::-1]

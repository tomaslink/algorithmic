"""Algorithms for string manipulation."""

from typing import Generator

ASCII_MAX_LENGTH = 128
ASCII_EMPTY_SPACE = 32


def unique(string: str) -> bool:
    """Checks if an ASCII string has all unique characters.

    Complexity:
    - Time: O(N).
    - Space: O(1).

    Where N is the length of the string.
    Since we have a fixed maximum for N, we could also think the time complexity as O(1).

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
    """Given two ASCII strings, checks if one is a permutation of the other.

    The algorithm is case-sensitive.

    Complexity:
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

    Complexity:
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
    """Generates all possible permutations of a string.

    Complexity (exercising the full generator):
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
    """Checks if a string is a palindrome permutation.

    In here, a palindrome is a word or phrase that,
        removed its spaces and all lowercase, is the same forward than backwards.

    This algorithms exploits the fact that if a string is a palindrome,
        at the most 1 character has an odd count of occurrences
        (the one in the middle for an odd string).

    Complexity:
    - Time: O(N).
    - Space: O(N).
    """

    string = string.replace(" ", "")
    string = string.lower()

    occurrences = {k: 0 for k in set(string)}

    for char in string:
        occurrences[char] += 1

    odd_counts = 0
    for count in occurrences.values():
        odd_counts += count % 2

    return odd_counts <= 1


def is_palindrome(string: str) -> bool:
    """Checks if a string is a palindrome.

    Complexity:
        Time: O(N).
        Space: O(N).
    """
    string = string.replace(" ", "")
    string = string.lower()

    return string == string[::-1]


def one_away(s1: str, s2: str) -> bool:
    """Given two ASCII strings s1 and s2, checks if s2 is one or zero modifications away from s1.
    The possible modifications of a string are insert a character,
        remove a character and replace a character.

    Complexity:
    - Time: O(N).
    - Space: O(N).
    """

    def one_insert_away(s1, s2):
        not_in_s2 = [char for char in s1 if char not in s2]

        if len(not_in_s2) == 1:
            s1_copy = s1.replace(not_in_s2[0], "")
            return s1_copy == s2

        return False

    def one_replace_away(s1, s2):
        diffs = 0
        for i, char in enumerate(s1):
            if char != s2[i]:
                diffs += 1

        return not diffs > 1

    def one_remove_away(s1, s2):
        return one_insert_away(s2, s1)  # swap strings, so insert becomes remove.

    if len(s1) == len(s2):
        return one_replace_away(s1, s2)

    if len(s2) == len(s1) - 1:
        return one_insert_away(s1, s2)

    if len(s2) == len(s1) + 1:
        return one_remove_away(s1, s2)

    return False


def compression(string: str) -> str:
    """Performs compression of a string by counting repeated characters."""

    current_char = string[0]
    count = 1

    compressed = ""

    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed += f"{current_char}{count}"
            current_char = char
            count = 1

    compressed += f"{current_char}{count}"

    if len(string) == len(compressed):
        return string

    return compressed


def rotation(s1: str, s2: str) -> str:
    """Checks if string s2 is a rotation of string s1, e.g.,
        "erbottlewat" is a rotation of "waterbottle".

    Complexity:
    - Time: O(A + B).
    - Space: O(A + B).

    Where A, B are the lengths of s1 and s2, respectively,
        assuming sub-string check has O(A + B) time.
    """
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    return s1 in ''.join([s2, s2])

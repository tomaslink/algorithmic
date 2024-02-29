import random
import string
import itertools

from algorithmic import strings


ENCODE_TYPE = 'ascii'


def test_unique():
    assert strings.unique("ASDF")
    assert not strings.unique("AAFD")

    s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=200))

    assert not strings.unique(s)


def test_check_permutation():
    assert strings.check_permutation("ABC", "CBA")
    assert not strings.check_permutation("ABC", "cBa")
    assert not strings.check_permutation("ABCD", "CBAA")
    assert not strings.check_permutation("ABCD", "ABCDF")


def test_urlify():
    _input = bytearray('This is a test      '.encode(ENCODE_TYPE))
    _output = bytearray('This%20is%20a%20test'.encode(ENCODE_TYPE))
    true_length = 14

    strings.urlify(_input, true_length)
    assert _input == _output

    _input = bytearray('NOSPACES'.encode(ENCODE_TYPE))
    _output = _input.copy()

    strings.urlify(_input, 8)
    assert _input == _output


def test_permutations():
    assert list(strings.permutations('AB')) == ['AB', 'BA']
    assert list(strings.permutations('A')) == ['A']

    result = [''.join(p) for p in itertools.permutations('ABC')]
    assert list(strings.permutations('ABC')) == result


def test_is_palindrome():
    assert strings.is_palindrome("taco cat")
    assert strings.is_palindrome("Taco Cat")
    assert not strings.is_palindrome("not a palindrome")


def test_palindrome_permutation():
    assert strings.palindrome_permutation("Tact Coa")
    assert strings.palindrome_permutation("tact coa")
    assert not strings.palindrome_permutation("not a palindrome permutation")


def test_one_away():
    assert strings.one_away("pale", "pale")
    assert strings.one_away("pale", "ple")
    assert strings.one_away("pales", "pale")
    assert strings.one_away("pale", "bale")
    # assert not strings.one_away("pale", "bake")
    assert not strings.one_away("pale", "paleontology")
    assert not strings.one_away("pales", "pcle")
    assert strings.one_away("pale", "pales")
    assert not strings.one_away("bale", "pales")

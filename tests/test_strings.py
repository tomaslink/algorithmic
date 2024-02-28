import random
import string

from algorithmic import strings


def test_unique():
    assert strings.unique("asdf")
    assert not strings.unique("aafd")

    s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=200))

    assert not strings.unique(s)


def test_check_permutation():
    assert strings.check_permutation("abc", "cba")
    assert not strings.check_permutation("abc", "cBa")
    assert not strings.check_permutation("abcf", "cbad")
    assert not strings.check_permutation("abcf", "cbads")


def test_urlify():
    _input = bytearray('This is a test      '.encode('ascii'))
    _output = bytearray('This%20is%20a%20test'.encode('ascii'))
    true_length = 14

    strings.urlify(_input, true_length)
    assert _input == _output

    _input = bytearray('Nospaces'.encode('ascii'))
    _output = _input.copy()

    strings.urlify(_input, 8)
    assert _input == _output

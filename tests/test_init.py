from algorithmic import version


def test_init():
    assert isinstance(version(), str)

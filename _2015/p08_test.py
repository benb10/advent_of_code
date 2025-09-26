from pathlib import Path

from . import p08_a, p08_b


def test_p08a_small():
    s = """
    ""
    "abc"
    "aaa\\"aaa"
    "\\x27"
    """

    assert p08_a.run(s) == 12


def test_p08a():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_a.run(s) == 1350


def test_p08b_small():
    s = """
    ""
    "abc"
    "aaa\\"aaa"
    "\\x27"
    """

    assert p08_b.run(s) == 19


def test_p08b():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_b.run(s) == 2085

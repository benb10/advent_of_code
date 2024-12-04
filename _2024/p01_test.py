from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    assert p01_a.run(s) == 11


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 2285373


def test_p01b_small():
    s = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    assert p01_b.run(s) == 31


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 21142653

from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263"""

    assert p01_a.run(s) == 7


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 1228


def test_p01b_small():
    s = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263"""

    assert p01_b.run(s) == 5


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 1257

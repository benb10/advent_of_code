from pathlib import Path

from . import p05_a, p05_b


def test_p05a_small():
    s = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""

    assert p05_a.run(s) == 5


def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == 4826


def test_p05b_small():
    s = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""

    assert p05_b.run(s) == 12


def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 16793

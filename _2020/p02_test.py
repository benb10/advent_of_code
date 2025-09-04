from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc"""

    assert p02_a.run(s) == 2


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 493


def test_p02b_small():
    s = """1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc"""

    assert p02_b.run(s) == 1


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 593

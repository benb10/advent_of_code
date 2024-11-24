from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = "))((((("

    assert p01_a.run(s) == 3


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 280


def test_p01b_small():
    s = "()())"

    assert p01_b.run(s) == 5


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 1797

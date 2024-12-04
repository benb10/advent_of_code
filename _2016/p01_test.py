from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = "R5, L5, R5, R3"

    assert p01_a.run(s) == 12


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 273


def test_p01b_small():
    s = "R8, R4, R4, R8"

    assert p01_b.run(s) == 4


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 115

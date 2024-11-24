from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = """1969
    100756
    """

    assert p01_a.run(s) == 34237


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 3401852


def test_p01b_small():
    s = """1969
    100756
    """

    assert p01_b.run(s) == 51312


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 5099916

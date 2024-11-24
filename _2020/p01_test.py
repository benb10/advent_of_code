from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = """1721
    979
    366
    299
    675
    1456"""

    assert p01_a.run(s) == 514579


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 858496


def test_p01b_small():
    s = """1721
        979
        366
        299
        675
        1456"""

    assert p01_b.run(s) == 241861950


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 263819430

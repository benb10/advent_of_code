from pathlib import Path

from . import p06_a, p06_b


def test_p06a_small():
    s = """Time:      7  15   30
    Distance:  9  40  200"""

    assert p06_a.run(s) == 288


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 781200


def test_p06b_small():
    s = """Time:      7  15   30
    Distance:  9  40  200"""

    assert p06_b.run(s) == 71503


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 49240091

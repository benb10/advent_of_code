from pathlib import Path

from . import p06_a, p06_b


def test_p06a_small():
    s = "0\t2\t7\t0"

    assert p06_a.run(s) == 5


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 12841


def test_p06b_small():
    s = "0\t2\t7\t0"

    assert p06_b.run(s) == 4


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 8038

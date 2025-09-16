from pathlib import Path

from . import p06_a, p06_b


def test_p06a_small():
    s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    assert p06_a.run(s) == 7


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 1640


def test_p06b_small():
    s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    assert p06_b.run(s) == 19


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 3613

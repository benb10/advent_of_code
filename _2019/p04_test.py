from pathlib import Path

from . import p04_a, p04_b


def test_p04a_small():
    s = "100000-200000"

    assert p04_a.run(s) == 1231


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 1610


def test_p04b_small():
    s = "100000-200000"

    assert p04_b.run(s) == 898


def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 1104

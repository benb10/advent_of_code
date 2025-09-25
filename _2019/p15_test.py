from pathlib import Path

from . import p15_a, p15_b


def test_p15a_small():
    s = "104,2,104,0,104,0,104,0,99"

    assert p15_a.run(s) == 1


def test_p15a():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_a.run(s) == 304


def test_p15b_small():
    s = "104,2,104,0,104,0,104,0,99"

    assert p15_b.run(s) == 1


def test_p15b():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_b.run(s) == 310

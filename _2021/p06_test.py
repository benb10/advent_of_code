from pathlib import Path

from . import p06_a, p06_b


def test_p06a_small():
    s = """3,4,3,1,2"""

    assert p06_a.run(s) == 5934


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 379414


def test_p06b_small():
    s = """3,4,3,1,2"""

    assert p06_b.run(s) == 26984457539


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 1705008653296

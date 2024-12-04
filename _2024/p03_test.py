from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert p03_a.run(s) == 161


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 173731097


def test_p03b_small():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert p03_b.run(s) == 48


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 93729253

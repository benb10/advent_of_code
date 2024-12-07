from pathlib import Path

import pytest

from . import p07_a, p07_b


def test_p07a_small():
    s = """
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20"""

    assert p07_a.run(s) == 3749


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 6392012777720


def test_p07b_small():
    s = """
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20"""

    assert p07_b.run(s) == 11387


@pytest.mark.skip("slow")
def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 61561126043536

from pathlib import Path

import pytest

from . import p06_a, p06_b


def test_p06a_small():
    s = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#..."""

    assert p06_a.run(s) == 41


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 4665


def test_p06b_small():
    s = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#..."""

    assert p06_b.run(s) == 6


@pytest.mark.runtime(21)
def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 1688

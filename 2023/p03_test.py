from pathlib import Path

import p03_a
import p03_b


def test_p03a_small():
    s = """467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.."""

    assert p03_a.run(s) == 4361


def test_p03a():
    s = Path("p03_input.txt").read_text()

    assert p03_a.run(s) == 525911


def test_p03b_small():
    s = """467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.."""

    assert p03_b.run(s) == 467835


def test_p03b():
    s = Path("p03_input.txt").read_text()

    assert p03_b.run(s) == 75805607

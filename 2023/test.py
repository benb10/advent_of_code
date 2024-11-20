from pathlib import Path

import p01a
import p01b


def test_p1a_small():
    s = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    assert p01a.run(s) == 142


def test_p1a():
    s = Path("p01_input.txt").read_text()

    assert p01a.run(s) == 55_607


def test_p1b_small():
    s = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""

    assert p01b.run(s) == 281


def test_p1b():
    s = Path("p01_input.txt").read_text()

    assert p01b.run(s) == 55291

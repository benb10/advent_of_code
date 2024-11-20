from pathlib import Path

import p01_a
import p01_b


def test_p01a_small():
    s = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    assert p01_a.run(s) == 142


def test_p01a():
    s = Path("p01_input.txt").read_text()

    assert p01_a.run(s) == 55_607


def test_p01b_small():
    s = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""

    assert p01_b.run(s) == 281


def test_p01b():
    s = Path("p01_input.txt").read_text()

    assert p01_b.run(s) == 55291

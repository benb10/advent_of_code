from pathlib import Path

from . import p04_a, p04_b


def test_p04a_small():
    s = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX"""

    assert p04_a.run(s) == 18


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 2534


def test_p04b_small():
    s = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX"""

    assert p04_b.run(s) == 9


def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 1866

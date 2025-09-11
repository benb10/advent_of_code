from pathlib import Path

from . import p05_a, p05_b


def test_p05a_small():
    s = """ugknbfddgicrmopn
    aaa
    jchzalrnumimnmhp"""

    assert p05_a.run(s) == 2


def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == 258


def test_p05b_small():
    s = """
    qjhvhtzxzqqjkmpb
    xxyxx
    uurcxstgmygtbstg
    ieodomkazucvgmuy"""

    assert p05_b.run(s) == 2


def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 53

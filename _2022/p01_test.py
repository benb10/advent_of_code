from pathlib import Path

from . import p01_a, p01_b


def test_p01a_small():
    s = """1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000"""

    assert p01_a.run(s) == 24_000


def test_p01a():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_a.run(s) == 70116


def test_p01b_small():
    s = """1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000"""

    assert p01_b.run(s) == 45000


def test_p01b():
    s = (Path(__file__).parent / "p01_input.txt").read_text()

    assert p01_b.run(s) == 206582

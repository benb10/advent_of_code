from pathlib import Path

from . import p04_a, p04_b


def test_p04a_small():
    s = """
    aa bb cc dd ee
    aa bb cc dd aa
    aa bb cc dd aaa
    """

    assert p04_a.run(s) == 2


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 451


def test_p04b_small():
    s = """abcde fghij
    abcde xyz ecdab
    a ab abc abd abf abj
    iiii oiii ooii oooi oooo
    oiii ioii iioi iiio"""

    assert p04_b.run(s) == 3


def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 223

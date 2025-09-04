from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """abcdef
    bababc
    abbcde
    abcccd
    aabcdd
    abcdee
    ababab"""

    assert p02_a.run(s) == 12


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 4712


def test_p02b_small():
    s = """abcde
    fghij
    klmno
    pqrst
    fguij
    axcye
    wvxyz"""

    assert p02_b.run(s) == "fgij"


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == "lufjygedpvfbhftxiwnaorzmq"

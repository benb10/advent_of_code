from pathlib import Path

from . import p14_a, p14_b


def test_p14a_small():
    s = """NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C"""

    assert p14_a.run(s) == 1588


def test_p14a():
    s = (Path(__file__).parent / "p14_input.txt").read_text()

    assert p14_a.run(s) == 2590


def test_p14b_small():
    s = """NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C"""

    assert p14_b.run(s) == 2188189693529


def test_p14b():
    s = (Path(__file__).parent / "p14_input.txt").read_text()

    assert p14_b.run(s) == 2875665202438

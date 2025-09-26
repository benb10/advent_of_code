from pathlib import Path

from . import p08_a, p08_b


def test_p08a_small():
    s = """RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)"""

    assert p08_a.run(s) == 2


def test_p08a():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_a.run(s) == 19951


def test_p08b_small():
    s = """LR
    
    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)"""

    assert p08_b.run(s) == 6


def test_p08b():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_b.run(s) == 16342438708751

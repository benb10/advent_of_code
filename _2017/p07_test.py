from pathlib import Path

from . import p07_a, p07_b


def test_p07a_small():
    s = """pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)"""

    assert p07_a.run(s) == "tknk"


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == "airlri"


def test_p07b_small():
    s = """pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)"""

    assert p07_b.run(s) == 60


def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 1206

from pathlib import Path

from . import p07_a, p07_b


def test_p07a_small():
    s = """abba[mnop]qrst
    abcd[bddb]xyyx
    aaaa[qwer]tyui
    ioxxoj[asdfgh]zxcvbn"""

    assert p07_a.run(s) == 2


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 105


def test_p07b_small():
    s = """aba[bab]xyz
    xyx[xyx]xyx
    aaa[kek]eke
    zazbz[bzb]cdb"""

    assert p07_b.run(s) == 3


def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 258

from pathlib import Path

from . import p04_a, p04_b


def test_p04a_small():
    s = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]"""

    assert p04_a.run(s) == 1514


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 245102


def test_p04b_small():
    s = """
    ab-c-343[aaaaa]
    lmprfnmjc-mzhcar-qrmpyec-2[bbbbb]"""

    assert p04_b.run(s) == 2


def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 324

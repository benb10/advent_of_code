from pathlib import Path

from . import p08_a, p08_b


def test_p08a_small():
    s = """nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""

    assert p08_a.run(s) == 5


def test_p08a():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_a.run(s) == 1548


def test_p08b_small():
    s = """nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""

    assert p08_b.run(s) == 8


def test_p08b():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_b.run(s) == 1375

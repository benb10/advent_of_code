from pathlib import Path

from . import p06_a, p06_b


def test_p06a_small():
    s = """abc
    
    a
    b
    c
    
    ab
    ac
    
    a
    a
    a
    a
    
    b"""

    assert p06_a.run(s) == 11


def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 6612


def test_p06b_small():
    s = """abc
    
    a
    b
    c
    
    ab
    ac
    
    a
    a
    a
    a
    
    b"""

    assert p06_b.run(s) == 6


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 3268

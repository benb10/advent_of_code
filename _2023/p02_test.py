from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert p02_a.run(s) == 8


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 2720


def test_p02b_small():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert p02_b.run(s) == 2286


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 71535

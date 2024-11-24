from pathlib import Path

from . import p13_a, p13_b


def test_p13a_small():
    s = """6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0
    
    fold along y=7
    fold along x=5"""

    assert p13_a.run(s) == 17


def test_p13a():
    s = (Path(__file__).parent / "p13_input.txt").read_text()

    assert p13_a.run(s) == 751


def test_p13b_small():
    # N/A
    pass


def test_p13b():
    s = (Path(__file__).parent / "p13_input.txt").read_text()

    assert p13_b.run(s) == (
        "###...##..#..#.###..#..#.#....#..#.#...\n"
        "#..#.#..#.#..#.#..#.#.#..#....#.#..#...\n"
        "#..#.#....####.#..#.##...#....##...#...\n"
        "###..#.##.#..#.###..#.#..#....#.#..#...\n"
        "#....#..#.#..#.#.#..#.#..#....#.#..#...\n"
        "#.....###.#..#.#..#.#..#.####.#..#.####\n"
    )

from pathlib import Path

import pytest

from . import p11_a, p11_b


def test_p11a_small():
    s = "104,0,104,0,104,0,104,0,99"

    assert p11_a.run(s) == 2


@pytest.mark.runtime(3)
def test_p11a():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_a.run(s) == 2469


def test_p11b_small():
    s = "104,1,104,1,104,1,104,1,99"

    assert p11_b.run(s) == "##\n.."


def test_p11b():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_b.run(s) == (
        ".#..#.#.....##..####..##..####..##..#..#...\n"
        ".#.#..#....#..#....#.#..#.#....#..#.#..#...\n"
        ".##...#....#......#..#..#.###..#....#..#...\n"
        ".#.#..#....#.....#...####.#....#.##.#..#...\n"
        ".#.#..#....#..#.#....#..#.#....#..#.#..#...\n"
        ".#..#.####..##..####.#..#.####..###..##...."
    )

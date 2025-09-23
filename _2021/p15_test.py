from pathlib import Path

import pytest

from . import p15_a, p15_b


def test_p15a_small():
    s = """1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581"""

    assert p15_a.run(s) == 40


@pytest.mark.skip("slow")
def test_p15a():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_a.run(s) == 720


def test_p15b_small():
    s = """1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581"""

    assert p15_b.run(s) == 315


@pytest.mark.skip("slow")
def test_p15b():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_b.run(s) == 1

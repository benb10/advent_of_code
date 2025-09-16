from pathlib import Path

import pytest

from . import p06_a, p06_b


def test_p06a_small():
    s = """1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9"""

    assert p06_a.run(s) == 17


@pytest.mark.skip("slow - might be able to improve performance")
def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 4284


def test_p06b_small():
    s = "\n".join(f"{x}, {y}" for x in range(20) for y in range(20))

    assert p06_b.run(s) == 1096


def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 35490

from pathlib import Path

from . import p05_a, p05_b


def test_p05a_small():
    s = (
        "    [D]\n"
        "[N] [C] \n"
        "[Z] [M] [P]\n"
        " 1   2   3 \n"
        "\n"
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2\n"
    )

    assert p05_a.run(s) == "CMZ"


def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == "SHMSDGZVC"


def test_p05b_small():
    s = (
        "    [D]\n"
        "[N] [C] \n"
        "[Z] [M] [P]\n"
        " 1   2   3 \n"
        "\n"
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2\n"
    )

    assert p05_b.run(s) == "MCD"


def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == "VRZGHDFBQ"

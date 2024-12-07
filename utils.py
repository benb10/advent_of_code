import importlib
from pathlib import Path
from time import time
from typing import Callable

SOLUTION_CODE_TEMPLATE = """def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\\n")]
    return 0
"""
TEST_CODE_TEMPLATE = """from pathlib import Path

import pytest

from . import p{problem_str}_a
from . import p{problem_str}_b


@pytest.mark.skip("solution not complete")
def test_p{problem_str}a_small():
    s = \"\"\"\"\"\"

    assert p{problem_str}_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p{problem_str}a():
    s = (Path(__file__).parent / "p{problem_str}_input.txt").read_text()

    assert p{problem_str}_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p{problem_str}b_small():
    s = \"\"\"\"\"\"

    assert p{problem_str}_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p{problem_str}b():
    s = (Path(__file__).parent / "p{problem_str}_input.txt").read_text()

    assert p{problem_str}_b.run(s) == 1

"""


def create_files(year: int, problem_number: int) -> None:
    problem_str = str(problem_number).zfill(2)
    files = [
        (f"_{year}/p{problem_str}_a.py", SOLUTION_CODE_TEMPLATE),
        (f"_{year}/p{problem_str}_b.py", SOLUTION_CODE_TEMPLATE),
        (f"_{year}/p{problem_str}_input.txt", ""),
        (f"_{year}/p{problem_str}_test.py", TEST_CODE_TEMPLATE.format(problem_str=problem_str)),
    ]
    for file_name, text in files:
        path = Path(__file__).parent / file_name
        if path.exists():
            print(f"skipping {path} because it already exists")

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def get_function(year: int, day: int, part: str) -> Callable | None:
    problem_num_str = str(day).zfill(2)
    module = importlib.import_module(f"_{year}.p{problem_num_str}_test")
    test_function_name = f"test_p{problem_num_str}{part}"
    return getattr(module, test_function_name)


def get_runtimes(year: int) -> None:
    for day in range(1, 26):
        for part in ("a", "b"):
            try:
                function = get_function(year, day, part)
                start_time = time()
                function()
            except:  # noqa E722
                continue
            end_time = time()
            runtime = round(end_time - start_time, 7)
            print(f"year={year}, day={day}, part={part}, runtime={runtime}")

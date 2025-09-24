import importlib
from collections import defaultdict
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


def create_files(year: int, day: int) -> None:
    day_str = str(day).zfill(2)
    files = [
        (f"_{year}/p{day_str}_a.py", SOLUTION_CODE_TEMPLATE),
        (f"_{year}/p{day_str}_b.py", SOLUTION_CODE_TEMPLATE),
        (f"_{year}/p{day_str}_input.txt", ""),
        (f"_{year}/p{day_str}_test.py", TEST_CODE_TEMPLATE.format(problem_str=day_str)),
    ]
    for file_name, text in files:
        path = Path(__file__).parent / file_name
        if path.exists():
            print(f"skipping {path} because it already exists")
            continue

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


def check_files():
    directory = Path(__file__).parent
    year_to_day_nums = defaultdict(set)
    warnings = []

    for file in directory.rglob("*.py"):
        if not file.is_file():
            continue

        relative_file = file.relative_to(directory)

        file_name = file.name
        is_known_file = check_is_known_file(relative_file)
        if not is_known_file:
            warnings.append(f"unknown file: {relative_file}")

        is_problem_file = (
            file_name[0] == "p" and file_name[1:3].isdigit() and file_name[3] == "_" and file_name[4:] == "a.py"
        )
        if not is_problem_file:
            continue

        year_part = file.parts[-2]
        year = int(year_part[1:])
        day = int(file_name[1:3])

        other_files = [file.parent / x for x in [f"p{day:02d}_b.py", f"p{day:02d}_input.txt", f"p{day:02d}_test.py"]]
        for other_file in other_files:
            if not other_file.exists():
                warnings.append(f"missing file: {other_file.relative_to(directory)}")

        year_to_day_nums[year].add(day)

    for warning in warnings:
        print(warning)

    print()
    print(f"Found {len(warnings)} warning(s)")
    print()

    min_year = min(year_to_day_nums)
    max_year = max(year_to_day_nums)

    for year in range(min_year, max_year + 1):
        day_nums = year_to_day_nums[year]
        day_strs = [f"{day:2}" for day in sorted(day_nums)]
        s = f"{year}: " + "  ".join(day_strs)
        print(s)

    num_years = max_year - min_year + 1
    num_days = 25 * num_years
    num_days_completed = sum(len(x) for x in year_to_day_nums.values())
    completion_percent = round(100 * num_days_completed / num_days, 2)
    print()
    print(f"Completion: {num_days_completed}/{num_days} ({completion_percent} %)")


def check_is_known_file(file: Path) -> bool:
    if file.parts in [
        ("_2019", "common.py"),
        ("_2019", "common_test.py"),
        ("conftest.py",),
        ("utils.py",),
    ]:
        return True

    if len(file.parts) != 2:
        return False

    year_part = file.parts[0]
    is_year = len(year_part) > 1 and year_part[0] == "_" and year_part[1:].isdigit()
    if not is_year:
        return False

    file_name = file.parts[1]
    is_known_file = file_name == "__init__.py" or (
        file_name[0] == "p"
        and file_name[1:3].isdigit()
        and file_name[3] == "_"
        and file_name[4:] in ["a.py", "b.py", "input.txt", "test.py"]
    )
    if not is_known_file:
        return False

    return True


create_files(2019, 13)
check_files()

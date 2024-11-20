from pathlib import Path

SOLUTION_CODE_TEMPLATE = """def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\\n")]
    return 0
"""
TEST_CODE_TEMPLATE = """from pathlib import Path

import p{problem_str}_a
import p{problem_str}_b


def test_p{problem_str}a_small():
    s = \"\"\"\"\"\"

    assert p{problem_str}_a.run(s) == 1


def test_p{problem_str}a():
    s = Path("p{problem_str}_input.txt").read_text()

    assert p{problem_str}_a.run(s) == 1


def test_p{problem_str}b_small():
    s = \"\"\"\"\"\"

    assert p{problem_str}_b.run(s) == 1


def test_p{problem_str}b():
    s = Path("p{problem_str}_input.txt").read_text()

    assert p{problem_str}_b.run(s) == 1

"""


def create_files(problem_number: int) -> None:
    problem_str = str(problem_number).zfill(2)
    files = [
        (f"p{problem_str}_a.py", SOLUTION_CODE_TEMPLATE),
        (f"p{problem_str}_b.py", SOLUTION_CODE_TEMPLATE),
        (f"p{problem_str}_input.txt", ""),
        (f"p{problem_str}_test.py", TEST_CODE_TEMPLATE.format(problem_str=problem_str)),
    ]
    for file_name, text in files:
        path = Path(file_name)
        if path.exists():
            print(f"skipping {path} because it already exists")

        path.write_text(text)
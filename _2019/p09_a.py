from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    output = run_intcode(nums, input_values=[1], log=True)

    assert len(output.outputs) == 1
    return output.outputs[0]


# from pathlib import Path
# s = (Path(__file__).parent / "p09_input.txt").read_text()
#
# print(run(s))

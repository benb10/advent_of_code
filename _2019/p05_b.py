from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    nums, outputs = run_intcode(nums, input_value=5, return_outputs=True)

    assert len(outputs) == 1
    return outputs[0]

from itertools import cycle


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]

    seen_frequencies = {0}
    current_frequency = 0

    for num in cycle(nums):
        current_frequency += num
        if current_frequency in seen_frequencies:
            break

        seen_frequencies.add(current_frequency)

    return current_frequency

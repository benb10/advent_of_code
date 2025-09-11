from collections import Counter
from copy import deepcopy


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    oxygen_str = get_rating(lines, min_or_max="max", default_match_char="1")
    co2_str = get_rating(lines, min_or_max="min", default_match_char="0")

    oxygen = int(oxygen_str, 2)
    co2 = int(co2_str, 2)

    return oxygen * co2


def get_rating(lines: list[str], min_or_max: str, default_match_char: str) -> str | None:
    assert min_or_max in ["min", "max"]

    filtered_lines = deepcopy(lines)
    width = len(lines[0])

    for i in range(width):
        chars_in_column = [line[i] for line in filtered_lines]
        char_to_count = Counter(chars_in_column)
        zero_count = char_to_count["0"]
        one_count = char_to_count["1"]

        if one_count > zero_count:
            match_char = "1" if min_or_max == "max" else "0"
        elif one_count < zero_count:
            match_char = "0" if min_or_max == "max" else "1"
        else:
            match_char = default_match_char

        filtered_lines = [line for line in filtered_lines if line[i] == match_char]

        if len(filtered_lines) == 1:
            return filtered_lines[0]

    return None

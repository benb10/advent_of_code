from math import ceil, floor, sqrt


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    time_line, distance_line = lines
    time_part = time_line.split(":")[1]
    distance_part = distance_line.split(":")[1]
    time = int(time_part.replace(" ", ""))
    distance = int(distance_part.replace(" ", ""))

    term_a = time / 2
    term_b = sqrt(time**2 - 4 * distance) / 2
    record_hold_times = [
        term_a + term_b,
        term_a - term_b,
    ]
    record_hold_time_lower, record_hold_time_upper = sorted(record_hold_times)
    min_winning_hold_time = floor(record_hold_time_lower + 1)
    max_winning_hold_time = ceil(record_hold_time_upper - 1)
    num_ways_to_win = max_winning_hold_time - min_winning_hold_time + 1

    return num_ways_to_win

from math import ceil, floor, sqrt


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    time_line, distance_line = lines
    time_part = time_line.split(":")[1]
    distance_part = distance_line.split(":")[1]
    times = [int(x) for x in time_part.strip().split(" ") if x]
    distances = [int(x) for x in distance_part.strip().split(" ") if x]

    total = 1

    for time, distance in zip(times, distances):
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
        total *= num_ways_to_win

    return total

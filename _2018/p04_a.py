from collections import defaultdict


def get_timestamp(line: str) -> str:
    return line.split("[")[1].split("]")[0]


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    sorted_lines = sorted(lines, key=get_timestamp)
    guard_id_to_mins_asleep = defaultdict(int)
    guard_id_to_min_to_times_asleep = defaultdict(lambda: {n: 0 for n in range(60)})

    current_guard_id = None
    sleep_start = None

    for line in sorted_lines:
        minute = int(line.split(":")[1].split("]")[0])

        if line.endswith("begins shift"):
            guard_id = int(line.split("#")[1].split(" ")[0])
            current_guard_id = guard_id

        elif line.endswith("falls asleep"):
            sleep_start = minute

        elif line.endswith("wakes up"):
            guard_id_to_mins_asleep[current_guard_id] += minute - sleep_start
            for min_asleep in range(sleep_start, minute):
                guard_id_to_min_to_times_asleep[current_guard_id][min_asleep] += 1

            sleep_start = None

        else:
            raise ValueError(f"Unrecognised line: {line}")

    sleepiest_guard_id, _mins_asleep = max(
        guard_id_to_mins_asleep.items(),
        key=lambda x: x[1],
    )
    sleepiest_minute, _times_asleep = max(
        guard_id_to_min_to_times_asleep[sleepiest_guard_id].items(),
        key=lambda x: x[1],
    )

    return sleepiest_guard_id * sleepiest_minute

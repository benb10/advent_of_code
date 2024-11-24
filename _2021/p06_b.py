from collections import defaultdict


def run(s: str) -> int:
    nums = [int(x) for x in s.split(",")]

    day_to_count = defaultdict(int)
    for num in nums:
        day_to_count[num] += 1

    for day_num in range(1, 257):
        new_day_to_count = defaultdict(int)

        for day, count in day_to_count.items():
            if day == 0:
                new_day_to_count[6] += count
                new_day_to_count[8] += count
            else:
                new_day_to_count[day - 1] += count

        day_to_count = new_day_to_count
    num_fish = sum(day_to_count.values())
    return num_fish

from collections import Counter


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    left_list = []
    right_list = []
    for line in lines:
        parts = line.split(" ")
        parts = [part for part in parts if part]
        part_1, part_2 = parts
        left_list.append(int(part_1))
        right_list.append(int(part_2))

    right_list_counter = Counter(right_list)

    total = 0

    for left_num in left_list:
        x = left_num * right_list_counter[left_num]
        total += x

    return total

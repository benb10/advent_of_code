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

    left_list.sort()
    right_list.sort()

    total = 0

    for left_num, right_num in zip(left_list, right_list):
        distance = abs(left_num - right_num)
        total += distance

    return total

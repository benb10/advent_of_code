def check_is_ordered(update: list[int], order_pairs: list[list[int]]) -> bool:
    num_to_pos = {num: i for i, num in enumerate(update)}

    for a, b in order_pairs:
        a_pos = num_to_pos.get(a)
        b_pos = num_to_pos.get(b)
        if a_pos is None or b_pos is None:
            continue
        if b_pos < a_pos:
            return False
    return True


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    empty_line_index = lines.index("")
    order_lines = lines[:empty_line_index]
    order_pairs = [[int(x) for x in line.split("|")] for line in order_lines]

    update_lines = lines[empty_line_index + 1 :]
    updates = [[int(x) for x in line.split(",")] for line in update_lines]

    total = 0

    for update in updates:
        is_ordered = check_is_ordered(update, order_pairs)

        if is_ordered:
            middle_num = update[len(update) // 2]
            total += middle_num

    return total

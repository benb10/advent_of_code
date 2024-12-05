from functools import cmp_to_key


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


def get_ordered_update(update: list[int], order_pairs: list[list[int]]) -> list[int]:
    pairs = {tuple(pair) for pair in order_pairs}

    def cmp_fn(a: int, b: int) -> int:
        if (a, b) in pairs:
            return -1
        if (b, a) in pairs:
            return 1
        return 0

    key_fn = cmp_to_key(cmp_fn)
    return sorted(update, key=key_fn)


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

        if not is_ordered:
            ordered_update = get_ordered_update(update, order_pairs)
            middle_num = ordered_update[len(ordered_update) // 2]
            total += middle_num

    return total

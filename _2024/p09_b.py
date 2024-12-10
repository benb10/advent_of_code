from collections import defaultdict


def check_is_start_of_file(file_blocks: list[int | None], idx: int) -> bool:
    if idx == 0:
        return True
    a = file_blocks[idx - 1]
    b = file_blocks[idx]
    return a != b and b is not None


def check_is_start_of_gap(file_blocks: list[int | None], idx: int) -> bool:
    a = file_blocks[idx - 1]
    b = file_blocks[idx]
    return a is not None and b is None


def get_file_length(file_blocks: list[int | None], idx: int) -> int:
    length = 0
    file_id = None
    num_file_blocks = len(file_blocks)
    while True:
        if idx >= num_file_blocks:
            break
        if file_blocks[idx] is None:
            break
        if file_id is None:
            # this is first iteration
            file_id = file_blocks[idx]

        if file_blocks[idx] != file_id:
            # end of file
            break

        length += 1
        idx += 1

    return length


def get_gap_length(file_blocks: list[int | None], idx: int) -> int:
    length = 0
    num_file_blocks = len(file_blocks)
    while True:
        if idx >= num_file_blocks:
            break
        if file_blocks[idx] is not None:
            break

        length += 1
        idx += 1

    return length


def get_length_to_gap_indexes(file_blocks: list[int | None]) -> dict[int : list[int]]:
    length_to_gap_indexes = defaultdict(list)
    for i, file_block in enumerate(file_blocks):
        if check_is_start_of_gap(file_blocks, i):
            gap_length = get_gap_length(file_blocks, i)
            length_to_gap_indexes[gap_length].append(i)

    return length_to_gap_indexes


def pop_next_gap_index(length_to_gap_indexes: dict[int : list[int]], length: int, idx_to_move_from: int) -> int | None:
    max_length = 9  # since gap length is a digit
    for gap_length in range(length, max_length + 1):
        gap_indexes = length_to_gap_indexes[gap_length]
        if gap_indexes:
            next_gap_index = gap_indexes[0]
            if next_gap_index > idx_to_move_from:
                # we can't move forwards, only backwards
                continue

            gap_indexes.pop(0)
            left_over_space = gap_length - length
            if left_over_space:
                left_over_start = next_gap_index + length
                length_to_gap_indexes[left_over_space] = sorted(
                    length_to_gap_indexes[left_over_space] + [left_over_start]
                )
            return next_gap_index


def pp(file_blocks):
    chars = ["." if c is None else str(c) for c in file_blocks]
    print("".join(chars))


def run(s: str) -> int:
    nums = [int(char) for char in s.strip()]
    file_blocks = []

    for i, num in enumerate(nums):
        is_file = i % 2 == 0
        file_id = i // 2 if is_file else None

        for j in range(num):
            file_blocks.append(file_id)

    idx_to_move_from = len(file_blocks) - 1
    length_to_gap_indexes = get_length_to_gap_indexes(file_blocks)

    moved_file_ids = set()
    print()
    while True:
        # pp(file_blocks)
        # print(file_blocks)
        # a = length_to_gap_indexes
        # b = get_length_to_gap_indexes(file_blocks[:idx_to_move_from])
        # if a != b:
        #     x=0
        if idx_to_move_from < 0:
            break
        while not check_is_start_of_file(file_blocks, idx_to_move_from):
            idx_to_move_from -= 1

        file_id = file_blocks[idx_to_move_from]

        if file_id in moved_file_ids:
            # not allowed to move file twice
            idx_to_move_from -= 1
            continue

        file_length = get_file_length(file_blocks, idx_to_move_from)
        next_gap_index = pop_next_gap_index(length_to_gap_indexes, file_length, idx_to_move_from)

        if next_gap_index is None:
            # there is no space to move this file to
            idx_to_move_from -= 1
            continue
        # print(file_id)

        if not all(x is None for x in file_blocks[next_gap_index : next_gap_index + file_length]):
            raise ValueError("AAA")

        if not all(x == file_id for x in file_blocks[idx_to_move_from : idx_to_move_from + file_length]):
            raise ValueError("BBB")

        file_blocks[next_gap_index : next_gap_index + file_length] = [file_id for _ in range(file_length)]
        file_blocks[idx_to_move_from : idx_to_move_from + file_length] = [None for _ in range(file_length)]
        idx_to_move_from -= 1
        moved_file_ids.add(file_id)

    checksum = 0
    for i, file_block in enumerate(file_blocks):
        if file_block is not None:
            checksum += i * file_block

    return checksum


# not the right answer:
# 6366116693035
# 6363831070327
if __name__ == "__main__":
    from pathlib import Path

    s = (Path(__file__).parent / "p09_input.txt").read_text()
    run(s)

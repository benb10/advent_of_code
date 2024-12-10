def run(s: str) -> int:
    nums = [int(char) for char in s.strip()]
    file_blocks = []

    for i, num in enumerate(nums):
        is_file = i % 2 == 0
        file_id = i // 2 if is_file else None

        for j in range(num):
            file_blocks.append(file_id)

    idx_to_move_from = len(file_blocks) - 1
    idx_to_move_to = 0

    while True:
        while file_blocks[idx_to_move_from] is None:
            idx_to_move_from -= 1

        while file_blocks[idx_to_move_to] is not None:
            idx_to_move_to += 1

        if idx_to_move_to > idx_to_move_from:
            # no more moves we can do
            break

        file_blocks[idx_to_move_to] = file_blocks[idx_to_move_from]
        file_blocks[idx_to_move_from] = None

    checksum = 0
    for i, file_block in enumerate(file_blocks):
        if file_block is None:
            break
        checksum += i * file_block

    return checksum

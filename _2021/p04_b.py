from itertools import batched


def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(x) for x in lines[0].split(",")]

    boards: list[list[list[int]]] = []

    for chunk in batched(lines[2:], 6):
        board_lines = chunk[:5]
        board = [[int(x) for x in line.split(" ") if x] for line in board_lines]
        boards.append(board)
    board_indices_without_bingo = [i for i in range(len(boards))]

    for num_to_read in range(5, len(nums) + 1):
        nums_read = nums[:num_to_read]
        for i, board in enumerate(boards):
            is_bingo = check_is_bingo(board, nums_read)

            if is_bingo and i in board_indices_without_bingo:
                if len(board_indices_without_bingo) == 1:
                    # this is the last board to get bingo
                    score = get_score(board, nums_read)
                    return score

                board_indices_without_bingo.remove(i)

    return None


def check_is_bingo(board: list[list[int]], nums_read: list[int]) -> bool:
    rows = board
    columns = list(zip(*board))
    board_lines = rows + columns

    for board_line in board_lines:
        if all(num in nums_read for num in board_line):
            return True

    return False


def get_score(board: list[list[int]], nums_read: list[int]) -> int:
    sum_unmarked_nums = 0

    for row in board:
        for num in row:
            if num not in nums_read:
                sum_unmarked_nums += num

    return sum_unmarked_nums * nums_read[-1]

from itertools import batched

from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]
    nums[0] = 2

    location_to_tile_id = {}

    instruction_pointer = 0
    relative_base = 0

    last_ball_x = None
    ball_x = None
    ball_y = None
    paddle_x = None
    score = 0

    while True:
        paddle_direction = 0

        if ball_x is not None and last_ball_x is not None:
            if ball_x == last_ball_x:
                # ball has stopped moving so game is over
                break

            ball_going_right = ball_x > last_ball_x

            walls_nearby = any(
                location_to_tile_id[(ball_x + dx, ball_y + dy)] == 2 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
            )
            if walls_nearby:
                target_x = ball_x
            else:
                target_x = ball_x + (1 if ball_going_right else -1)

            paddle_diff_x = target_x - paddle_x

            if paddle_diff_x == 0:
                paddle_direction = 0
            elif paddle_diff_x < 0:
                paddle_direction = -1
            else:
                paddle_direction = 1

        output = run_intcode(
            nums,
            input_values=[paddle_direction],
            stop_when_input_required=True,
            instruction_pointer=instruction_pointer,
            relative_base=relative_base,
        )

        nums = output.nums
        instruction_pointer = output.instruction_pointer
        relative_base = output.relative_base

        last_ball_x = ball_x

        for x, y, tile_id in batched(output.outputs, 3):
            if tile_id in [0, 1, 2, 3, 4]:
                location_to_tile_id[(x, y)] = tile_id
                if tile_id == 4:
                    ball_x = x
                    ball_y = y

                if tile_id == 3:
                    paddle_x = x
            else:
                score = tile_id

    return score


def pp(location_to_tile_id: dict[tuple[int, int], int]) -> None:
    xs = [a[0] for a in location_to_tile_id]
    ys = [a[1] for a in location_to_tile_id]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    rows = []

    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            tile_id = location_to_tile_id.get((x, y), "?")
            row += " " if tile_id == 0 else str(tile_id)
        rows.append(row)

    print("\n".join(rows))

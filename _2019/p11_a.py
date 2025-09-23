from collections import defaultdict
from enum import Enum

from .common import run_intcode


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]
    instruction_pointer = 0
    relative_base = 0

    location_to_colour = defaultdict(int)
    locations_painted = set()
    location = (0, 0)
    direction = Direction.NORTH

    while True:
        colour = location_to_colour[location]

        output = run_intcode(
            nums,
            input_values=[colour],
            instruction_pointer=instruction_pointer,
            relative_base=relative_base,
            stop_after_n_outputs=2,
        )

        nums = output.nums
        instruction_pointer = output.instruction_pointer
        relative_base = output.relative_base

        if not output.outputs:
            break

        assert len(output.outputs) == 2

        color_to_paint, direction_to_turn = output.outputs

        location_to_colour[location] = color_to_paint
        locations_painted.add(location)

        direction = get_new_direction(direction, direction_to_turn)
        location = move_location(location, direction)

    return len(locations_painted)


def get_new_direction(direction: Direction, direction_to_turn: int) -> Direction:
    dirs_clockwise: list[Direction] = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    current_i = dirs_clockwise.index(direction)
    diff = {0: -1, 1: 1}[direction_to_turn]
    new_i = (current_i + diff) % len(dirs_clockwise)
    return dirs_clockwise[new_i]


def move_location(location: tuple[int, int], direction: Direction) -> tuple[int, int]:
    x_diff, y_diff = {
        Direction.NORTH: (0, 1),
        Direction.EAST: (1, 0),
        Direction.SOUTH: (0, -1),
        Direction.WEST: (-1, 0),
    }[direction]
    x, y = location
    return x + x_diff, y + y_diff

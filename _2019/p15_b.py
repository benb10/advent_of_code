from dataclasses import dataclass
from itertools import count

from .common import run_intcode


@dataclass
class Job:
    starting_x: int
    starting_y: int
    distance_from_origin: int
    move: int
    nums: list[int]
    instruction_pointer: int
    relative_base: int


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    location_to_char = {(0, 0): "."}
    location_to_distance_from_origin = {(0, 0): 0}
    jobs_to_do = []
    for move in [1, 2, 3, 4]:
        jobs_to_do.append(
            Job(
                starting_x=0,
                starting_y=0,
                distance_from_origin=0,
                move=move,
                nums=nums,
                instruction_pointer=0,
                relative_base=0,
            )
        )
    i = 0
    while jobs_to_do:
        job = jobs_to_do.pop(0)

        output = run_intcode(
            job.nums,
            input_values=[job.move],
            instruction_pointer=job.instruction_pointer,
            relative_base=job.relative_base,
            stop_after_n_outputs=1,
        )
        assert len(output.outputs) == 1
        output_value = output.outputs[0]

        new_x, new_y = get_new_location(job.starting_x, job.starting_y, job.move)

        char = {
            0: "#",
            1: ".",
            2: "O",
        }[output_value]
        location_to_char[(new_x, new_y)] = char

        if output_value in [1, 2]:
            location_to_distance_from_origin[(new_x, new_y)] = job.distance_from_origin + 1
            # add new jobs
            moves_to_unknown_locations = get_moves_to_unknown_locations(new_x, new_y, location_to_char)
            for move in moves_to_unknown_locations:
                jobs_to_do.append(
                    Job(
                        starting_x=new_x,
                        starting_y=new_y,
                        distance_from_origin=job.distance_from_origin + 1,
                        move=move,
                        nums=output.nums,
                        instruction_pointer=output.instruction_pointer,
                        relative_base=output.relative_base,
                    )
                )

        i += 1

    oxygen_locations = {loc for loc, char in location_to_char.items() if char == "O"}
    total_area = sum(1 for loc, char in location_to_char.items() if char in [".", "O"])

    for minute in count(1):
        for oxygen_location in list(oxygen_locations):
            oxygen_locations.update(get_neighbour_locations(oxygen_location, location_to_char))

        if len(oxygen_locations) == total_area:
            return minute


MOVEMENT_TO_DX_DY = {
    1: (0, 1),  # north
    2: (0, -1),  # south
    3: (-1, 0),  # west
    4: (1, 0),  # east
}
MOVEMENT_TO_REVERSE = {
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}


def get_neighbour_locations(
    location: tuple[int, int], location_to_char: dict[tuple[int, int], str]
) -> list[tuple[int, int]]:
    neighbour_locations = []
    x, y = location

    for move in [1, 2, 3, 4]:
        new_location = get_new_location(x, y, move)
        if location_to_char[new_location] == ".":
            neighbour_locations.append(new_location)

    return neighbour_locations


def get_moves_to_unknown_locations(x: int, y: int, location_to_char: dict[tuple[int, int], str]) -> list[int]:
    moves_to_unknown_locations = []

    for move in [1, 2, 3, 4]:
        new_x, new_y = get_new_location(x, y, move)
        if (new_x, new_y) not in location_to_char:
            moves_to_unknown_locations.append(move)

    return moves_to_unknown_locations


def get_new_location(x: int, y: int, move: int) -> tuple[int, int]:
    dx, dy = MOVEMENT_TO_DX_DY[move]
    return x + dx, y + dy


def pp(location_to_char: dict[tuple[int, int], str]) -> None:
    xs = [a[0] for a in location_to_char]
    ys = [a[1] for a in location_to_char]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    rows = []

    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) == (0, 0):
                char = "S"
            else:
                char = location_to_char.get((x, y), " ")

            row += char
        rows.append(row)

    print("\n\n")
    print("\n".join(rows))

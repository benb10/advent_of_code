from dataclasses import dataclass
from typing import List


def new_risks(risks):
    size_x = len(risks)

    assert all(len(row) == len(risks[0]) for row in risks)
    size_y = len(risks[0])

    new_size_x = size_x * 5
    new_size_y = size_y * 5

    new = [[None for _ in range(new_size_y)] for _ in range(new_size_x)]
    for x in range(new_size_x):
        for y in range(new_size_y):
            if x < size_x and y < size_y:
                new[x][y] = risks[x][y]

            tile_count_x = x // size_x
            tile_count_y = y // size_y

            first_tile_x = x % size_x
            first_tile_y = y % size_y

            first_tile_val = risks[first_tile_x][first_tile_y]

            new_val = first_tile_val + tile_count_x + tile_count_y
            while new_val > 9:
                new_val -= 9

            new[x][y] = new_val

    return new


@dataclass
class Option:
    path: list
    costs: List[int]

    def passes_pt(self, pt):
        return pt in self.path


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    risks = [[int(x) for x in line.strip()] for line in lines]

    risks = new_risks(risks)

    end = (len(risks) - 1, len(risks[0]) - 1)

    pts = {(x, y) for x in range(len(risks)) for y in range(len(risks[0]))}

    options = [Option(path=[(0, 0)], costs=[0])]

    pt_to_best_cost = {(0, 0): 0}

    while True:
        option = options.pop(0)

        e = option.path[-1]

        if e == end:
            solution = option
            break

        end_x, end_y = e

        next_steps = [
            (end_x, end_y + 1),
            (end_x, end_y - 1),
            (end_x + 1, end_y),
            (end_x - 1, end_y),
        ]

        # filter out ones outside the grid:
        next_steps = [s for s in next_steps if s in pts]
        # filter out any that cause the path to loop into itself:
        next_steps = [s for s in next_steps if s not in option.path]

        for next_step in next_steps:
            next_x, next_y = next_step
            total_cost = option.costs[-1] + risks[next_x][next_y]
            if next_step not in pt_to_best_cost:
                pt_to_best_cost[next_step] = total_cost
            else:
                if total_cost > pt_to_best_cost[next_step]:
                    # no point adding new path.  too expensive
                    continue
                # we have a new cheapest option:
                pt_to_best_cost[next_step] = total_cost
                # remove all other paths:
                options = [o for o in options if next_step not in o.path]
            options.append(Option(path=option.path + [next_step], costs=option.costs + [total_cost]))

    return solution.costs[-1]

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Self


@dataclass
class Vector:
    r: int
    c: int

    def __add__(self, other: Self) -> Self:
        return Vector(self.r + other.r, self.c + other.c)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.r - other.r, self.c - other.c)

    def __hash__(self):
        return hash((self.r, self.c))


def check_is_within_bounds(location: Vector, num_rows: int, num_columns: int) -> bool:
    return (0 <= location.r < num_rows) and (0 <= location.c < num_columns)


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    frequency_to_locations = defaultdict(set)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != ".":
                frequency_to_locations[char].add(Vector(r, c))

    num_rows = len(lines)
    num_columns = len(lines[0])

    anti_node_locations = set()
    for frequency, locations in frequency_to_locations.items():
        for loc_1, loc_2 in combinations(locations, 2):
            diff = loc_2 - loc_1
            potential_anti_nodes = [loc_1 - diff, loc_2 + diff]
            for anti_node in potential_anti_nodes:
                if check_is_within_bounds(anti_node, num_rows, num_columns):
                    anti_node_locations.add(anti_node)

    return len(anti_node_locations)

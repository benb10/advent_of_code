from dataclasses import dataclass


@dataclass
class Island:
    plant_type: str
    coords: set[tuple[int, int]]

    @property
    def area(self) -> int:
        return len(self.coords)

    @property
    def perimeter(self) -> int:
        total = 0

        for r, c in self.coords:
            neighbours = [
                (r, c + 1),  # right
                (r + 1, c),  # down
                (r, c - 1),  # left
                (r - 1, c),  # up
            ]
            for neighbour in neighbours:
                if neighbour not in self.coords:
                    total += 1

        return total


def get_merged_island(islands: list[Island]) -> Island:
    plant_types = {island.plant_type for island in islands}
    if len(plant_types) != 1:
        raise ValueError(f"merging multiple plant types: {plant_types}")

    plant_type = list(plant_types)[0]
    merged_island = Island(
        plant_type=plant_type,
        coords=set(),
    )

    for island in islands:
        merged_island.coords.update(island.coords)

    return merged_island


def get_islands(lines: list[str]) -> list[Island]:
    islands = []

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            neighbours = {
                (r, c + 1),  # right
                (r + 1, c),  # down
                (r, c - 1),  # left
                (r - 1, c),  # up
            }
            related_islands = [island for island in islands if island.plant_type == char and island.coords & neighbours]
            if not related_islands:
                islands.append(
                    Island(
                        plant_type=char,
                        coords={
                            (r, c),
                        },
                    )
                )
            elif len(related_islands) == 1:
                related_island = related_islands[0]
                related_island.coords.add((r, c))
            else:
                # need to merge islands
                merged_island = get_merged_island(related_islands)
                merged_island.coords.add((r, c))
                for related_island in related_islands:
                    islands.remove(related_island)
                islands.append(merged_island)

    return islands


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    islands = get_islands(lines)

    total_fencing = 0

    for island in islands:
        total_fencing += island.area * island.perimeter

    return total_fencing

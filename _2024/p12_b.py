from dataclasses import dataclass


@dataclass
class SidePiece:
    r: int
    c: int
    side: str  # u d l r

    def is_adjacent(self, other) -> bool:
        if self.side != other.side:
            return False

        if self.side in ["u", "d"]:
            return self.r == other.r and abs(self.c - other.c) == 1

        if self.side in ["l", "r"]:
            return self.c == other.c and abs(self.r - other.r) == 1

        return False


@dataclass
class Island:
    plant_type: str
    coords: set[tuple[int, int]]

    @property
    def area(self) -> int:
        return len(self.coords)

    @property
    def num_sides(self) -> int:
        side_pieces = []

        for r, c in self.coords:
            neighbours = [
                ("r", (r, c + 1)),  # right
                ("d", (r + 1, c)),  # down
                ("l", (r, c - 1)),  # left
                ("u", (r - 1, c)),  # up
            ]
            for side, neighbour in neighbours:
                if neighbour not in self.coords:
                    side_pieces.append(SidePiece(r=r, c=c, side=side))

        sides = []

        for side_piece in sorted(side_pieces, key=lambda x: (x.r, x.c)):
            # see if we can add it to an existing side
            has_been_added = False

            for side in sides:
                for other_side_piece in side:
                    if side_piece.is_adjacent(other_side_piece):
                        side.append(side_piece)
                        has_been_added = True
                        break
                if has_been_added:
                    break

            if not has_been_added:
                # make a new side
                sides.append([side_piece])

        return len(sides)


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
        total_fencing += island.area * island.num_sides

    return total_fencing

from dataclasses import dataclass
from typing import Self


@dataclass
class Claim:
    id: int
    left_dist: int
    top_dist: int
    width: int
    height: int

    @property
    def row_range(self) -> tuple[int, int]:
        return self.top_dist, self.top_dist + self.height - 1

    @property
    def column_range(self) -> tuple[int, int]:
        return self.left_dist, self.left_dist + self.width - 1

    def overlaps(self, other_claim: Self) -> bool:
        rows_overlap = ranges_overlap(self.row_range, other_claim.row_range)
        if not rows_overlap:
            return False

        columns_overlap = ranges_overlap(self.column_range, other_claim.column_range)
        if not columns_overlap:
            return False

        return True


def ranges_overlap(range_1: tuple[int, int], range_2: tuple[int, int]) -> bool:
    a, b = range_1
    c, d = range_2

    range_1_before_2 = b < c
    range_2_before_1 = d < a

    return not (range_1_before_2 or range_2_before_1)


def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    claims = []

    for line in lines:
        a, _b, c, d = line.split(" ")

        claim_id = int(a.replace("#", ""))
        distances_str = c.replace(":", "")
        left_dist, top_dist = [int(x) for x in distances_str.split(",")]
        width, height = [int(x) for x in d.split("x")]
        claim = Claim(
            id=claim_id,
            left_dist=left_dist,
            top_dist=top_dist,
            width=width,
            height=height,
        )
        claims.append(claim)

    for claim in claims:
        overlaps_with_others = False

        for other_claim in claims:
            if claim.id == other_claim.id:
                continue

            if claim.overlaps(other_claim):
                overlaps_with_others = True
                break

        if not overlaps_with_others:
            return claim.id

    return None

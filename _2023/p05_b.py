from copy import deepcopy
from dataclasses import dataclass
from typing import Self


@dataclass
class Range:
    start: int
    end: int

    def __lt__(self, other: Self) -> bool:
        return self.end <= other.start

    def __gt__(self, other: Self) -> bool:
        return self.start >= other.end

    def __len__(self) -> int:
        return self.end - self.start

    def is_disjoint_from(self, other: Self) -> bool:
        return self < other or self > other

    def overlaps(self, other: Self) -> bool:
        return not self.is_disjoint_from(other)

    def is_within(self, other: Self) -> bool:
        starts_before = other.start <= self.start
        ends_after = self.end <= other.end
        return starts_before and ends_after

    def shifted(self, diff: int) -> Self:
        return Range(
            start=self.start + diff,
            end=self.end + diff,
        )

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    def pass_through_map(self, source_range: Self, dest_range: Self) -> tuple[list[Self], list[Self]]:
        """Return unmapped ranges and mapped ranges."""
        if self.is_disjoint_from(source_range):
            return [self], []

        diff = dest_range.start - source_range.start

        if self.is_within(source_range):
            return [], [self.shifted(diff)]

        if source_range.is_within(self):
            unmapped_start = Range(
                start=self.start,
                end=source_range.start,
            )
            unmapped_end = Range(
                start=source_range.end,
                end=self.end,
            )
            unmapped_ranges = []
            if not unmapped_start.is_empty:
                unmapped_ranges.append(unmapped_start)
            if not unmapped_end.is_empty:
                unmapped_ranges.append(unmapped_end)

            mapped_range = source_range.shifted(diff)
            return unmapped_ranges, [mapped_range]

        if source_range.start < self.start < source_range.end < self.end:
            mapped_start = Range(
                start=self.start,
                end=source_range.end,
            ).shifted(diff)
            unmapped_end = Range(
                start=source_range.end,
                end=self.end,
            )
            return [unmapped_end], [mapped_start]

        if self.start < source_range.start < self.end < source_range.end:
            unmapped_start = Range(
                start=self.start,
                end=source_range.start,
            )
            mapped_end = Range(
                start=source_range.start,
                end=self.end,
            ).shifted(diff)
            return [unmapped_start], [mapped_end]

        raise ValueError(f"failed to map: self={self}, source_range={source_range}, dest_range={dest_range}")


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    first_line = lines[0]
    seed_num_part = first_line.split(":")[1]
    seed_nums = [int(x) for x in seed_num_part.strip().split(" ")]
    num_seed_ranges = len(seed_nums) // 2
    seed_ranges = []
    for i in range(num_seed_ranges):
        start = seed_nums[2 * i]
        length = seed_nums[2 * i + 1]
        seed_ranges.append(Range(start=start, end=start + length))

    sections = []
    last_line = None
    for line in lines[2:]:
        line = line.strip()
        if line:
            if last_line:
                sections[-1].append(line)
            else:
                # start a new section
                sections.append([line])
        last_line = line

    ranges_through_process = [seed_ranges]

    for section in sections:
        unmapped_ranges = deepcopy(ranges_through_process[-1])
        next_ranges = []
        map_lines = section[1:]
        maps = [[int(x) for x in map_line.strip().split(" ")] for map_line in map_lines]
        for map_vals in maps:
            dest_range_start, source_range_start, range_len = map_vals
            source_range = Range(source_range_start, source_range_start + range_len)
            dest_range = Range(dest_range_start, dest_range_start + range_len)

            new_unmapped_ranges = []
            for unmapped_range in unmapped_ranges:
                unmapped_ranges, mapped_ranges = unmapped_range.pass_through_map(source_range, dest_range)
                new_unmapped_ranges.extend(unmapped_ranges)
                next_ranges.extend(mapped_ranges)

            unmapped_ranges = new_unmapped_ranges

        # unmapped ranges get passed through as is
        next_ranges.extend(unmapped_ranges)
        ranges_through_process.append(next_ranges)

    final_ranges = ranges_through_process[-1]
    min_val = min(r.start for r in final_ranges)
    return min_val

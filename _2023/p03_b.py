from dataclasses import dataclass


@dataclass
class PartNumber:
    num: int
    start: tuple[int, int]

    @property
    def locs(self) -> list[tuple[int, int]]:
        start_r, start_c = self.start
        return [(start_r, start_c + i) for i in range(len(str(self.num)))]


def get_adj_locs(loc: tuple[int, int]) -> list[tuple[int, int]]:
    r, c = loc
    return [(r + diff_r, c + diff_c) for diff_r in [-1, 0, 1] for diff_c in [-1, 0, 1]]


def get_adj_part_nums(gear_loc: tuple[int, int], part_nums: list[PartNumber]) -> list[PartNumber]:
    gear_adj_locs = get_adj_locs(gear_loc)

    return [part_num for part_num in part_nums if set(part_num.locs) & set(gear_adj_locs)]


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    part_nums = []
    gear_locs = set()

    for r, line in enumerate(lines):
        in_number = False
        num_strs = []
        for c, char in enumerate(line):
            if char.isdigit():
                if in_number:
                    num_strs[-1][0] += char
                else:
                    num_strs.append([char, (r, c)])
                in_number = True
            else:
                in_number = False

            if char == "*":
                gear_locs.add((r, c))

        part_nums.extend([PartNumber(num=int(num_str), start=(r, c)) for num_str, (r, c) in num_strs])

    total = 0
    for gear_loc in gear_locs:
        adj_part_nums = get_adj_part_nums(gear_loc, part_nums)
        if len(adj_part_nums) == 2:
            part_num_a, part_num_b = adj_part_nums
            total += part_num_a.num * part_num_b.num

    return total

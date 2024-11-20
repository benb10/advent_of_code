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


def part_number_is_touching_symbol(part_number: PartNumber, symbols: set[tuple[int, int]]):
    adj_locs = set()

    for part_loc in part_number.locs:
        adj_locs.update(get_adj_locs(part_loc))

    return adj_locs & symbols


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    part_nums = []
    symbols = set()

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

            is_symbol = not char.isdigit() and char != "."
            if is_symbol:
                symbols.add((r, c))

        part_nums.extend([PartNumber(num=int(num_str), start=(r, c)) for num_str, (r, c) in num_strs])

    total = sum(part_num.num for part_num in part_nums if part_number_is_touching_symbol(part_num, symbols))

    return total

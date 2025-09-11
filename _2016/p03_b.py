def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0

    nums_grid = []

    for line in lines:
        nums = [int(x) for x in line.split(" ") if x]
        nums_grid.append(nums)

    for c in range(3):
        for r in range(0, len(nums_grid), 3):
            side_lengths = [
                nums_grid[r][c],
                nums_grid[r + 1][c],
                nums_grid[r + 2][c],
            ]
            side_lengths.sort()
            *other_sides, longest_side = side_lengths
            is_valid = sum(other_sides) > longest_side
            if is_valid:
                total += 1

    return total

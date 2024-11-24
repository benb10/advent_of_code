def get_cell_power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = power_level // 100 % 10  # get hundreds digit
    power_level -= 5
    return power_level


def get_grid(serial_number, size):
    grid = []

    for row_index in range(size):
        grid.append([])
        for column_index in range(size):
            x = row_index + 1
            y = column_index + 1

            cell_power = get_cell_power(x, y, serial_number)
            grid[-1].append(cell_power)
    return grid


def get_sub_grid(grid, tl_coord, size):
    pass


def print_grid(grid):
    column_width = 3  # assumes all 1 digit numbers, possibly negative
    for row in grid:
        for num in row:
            print(str(num).rjust(column_width), end="")
        print("")


grid = get_grid(18, 50)


def run(s: str) -> int:
    # grid = get_grid(18, 50)
    return 0

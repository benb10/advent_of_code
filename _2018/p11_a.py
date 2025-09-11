def get_cell_power(x: int, y: int, grid_serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = power_level // 100 % 10  # get hundreds digit
    power_level -= 5
    return power_level


def get_grid(grid_serial_number: int, size: int) -> list[list[int]]:
    grid = []

    for row_index in range(size):
        grid.append([])
        for column_index in range(size):
            x = column_index + 1
            y = row_index + 1

            cell_power = get_cell_power(x, y, grid_serial_number)
            grid[-1].append(cell_power)
    return grid


def run(s: str) -> str:
    grid_serial_number = int(s.strip())
    grid_size = 300
    grid = get_grid(grid_serial_number, grid_size)

    max_power = -999999
    max_power_x = None
    max_power_y = None

    for row_index in range(grid_size - 2):
        for column_index in range(grid_size - 2):
            square_power = sum(
                grid[a][b] for a in range(row_index, row_index + 3) for b in range(column_index, column_index + 3)
            )
            if square_power > max_power:
                max_power = square_power
                max_power_x = column_index + 1
                max_power_y = row_index + 1

    return f"{max_power_x},{max_power_y}"

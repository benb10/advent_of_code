from tqdm import tqdm


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
    max_power_square_size = None
    sq_id_to_power = {
        (row_index, column_index, 1): grid[row_index][column_index]
        for row_index in range(grid_size)
        for column_index in range(grid_size)
    }

    for square_size in tqdm(range(2, 301)):
        for row_index in range(grid_size - square_size + 1):
            for column_index in range(grid_size - square_size + 1):
                last_square_power = sq_id_to_power[(row_index, column_index, square_size - 1)]
                new_vert_line = sum(grid[row_index + r][column_index + square_size - 1] for r in range(square_size))
                new_horizontal_line = sum(
                    grid[row_index + square_size - 1][column_index + c] for c in range(square_size)
                )
                bottom_right_cell_power = grid[row_index + square_size - 1][column_index + square_size - 1]
                square_power = last_square_power + new_vert_line + new_horizontal_line - bottom_right_cell_power

                sq_id_to_power[(row_index, column_index, square_size)] = square_power

                if square_power > max_power:
                    max_power = square_power
                    max_power_x = column_index + 1
                    max_power_y = row_index + 1
                    max_power_square_size = square_size
                    print(f"{max_power}: {max_power_x},{max_power_y},{max_power_square_size}")

    return f"{max_power_x},{max_power_y},{max_power_square_size}"

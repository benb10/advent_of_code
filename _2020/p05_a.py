def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    max_seat_id = 0

    for line in lines:
        row_chars = line[:7]
        column_chars = line[7:]

        row = 0
        for i, char in enumerate(row_chars[::-1]):
            if char == "F":
                continue
            row += 2**i

        column = 0
        for i, char in enumerate(column_chars[::-1]):
            if char == "L":
                continue
            column += 2**i

        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id

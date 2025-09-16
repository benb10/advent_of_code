def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    all_seat_ids = []

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
        all_seat_ids.append(seat_id)

    for n in range(min(all_seat_ids), max(all_seat_ids) + 1):
        if n not in all_seat_ids:
            return n

    return None

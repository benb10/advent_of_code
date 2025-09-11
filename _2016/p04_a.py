from collections import Counter


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        start, checksum = line.split("[")
        *letter_parts, id_part = start.split("-")

        chars = ""
        for letter_part in letter_parts:
            chars += letter_part

        sector_id = int(id_part)
        checksum = checksum.replace("]", "")

        char_to_count = Counter(chars)
        sorted_chars = sorted(set(chars), key=lambda c: (-char_to_count[c], c))

        is_real_room = "".join(sorted_chars[:5]) == checksum
        if is_real_room:
            total += sector_id

    return total

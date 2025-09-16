from more_itertools import windowed


def run(s: str) -> int | None:
    chars = s.strip()
    window_size = 14

    for i, sub_chars in enumerate(windowed(chars, window_size)):
        no_duplicates = len(sub_chars) == len(set(sub_chars))
        if no_duplicates:
            return i + window_size

    return None

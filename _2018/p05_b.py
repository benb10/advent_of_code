import string
from copy import deepcopy


def run(s: str) -> int:
    chars = [c for c in s.strip()]

    min_length = None

    for c in string.ascii_lowercase:
        chars_to_remove = {c, c.upper()}
        new_chars = [c for c in chars if c not in chars_to_remove]
        output_chars = run_reaction(new_chars)
        size_output_chars = len(output_chars)

        if min_length is None or size_output_chars < min_length:
            min_length = size_output_chars

    return min_length


def run_reaction(input_chars: list[str]) -> list[str]:
    chars = deepcopy(input_chars)

    pairs_to_find = {x for c in string.ascii_lowercase for x in [(c, c.upper()), (c.upper(), c)]}

    while True:
        indices_to_remove = set()

        i = 0
        upper_bound = len(chars) - 1
        while True:
            if i >= upper_bound:
                break

            a = chars[i]
            b = chars[i + 1]

            if (a, b) in pairs_to_find:
                indices_to_remove.add(i)
                indices_to_remove.add(i + 1)
                i += 2
            else:
                i += 1

        if not indices_to_remove:
            break

        chars = [c for i, c in enumerate(chars) if i not in indices_to_remove]

    return chars

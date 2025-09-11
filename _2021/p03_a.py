from collections import Counter


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    gamma_str = ""
    epsilon_str = ""

    width = len(lines[0])
    for i in range(width):
        chars_in_column = [line[i] for line in lines]
        char_to_count = Counter(chars_in_column)
        least_common_char, most_common_char = sorted(set(chars_in_column), key=lambda c: char_to_count[c])
        gamma_str += most_common_char
        epsilon_str += least_common_char

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    return gamma * epsilon

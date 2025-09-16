from collections import Counter


def run(s: str) -> str:
    lines = [line.strip() for line in s.strip().split("\n")]
    word_length = len(lines[0])
    word = ""

    for i in range(word_length):
        char_to_count = Counter(line[i] for line in lines)
        most_popular_char, _count = max(char_to_count.items(), key=lambda x: x[1])
        word += most_popular_char

    return word

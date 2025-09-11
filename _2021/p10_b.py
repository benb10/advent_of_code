from statistics import median


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    open_to_closed = {
        "[": "]",
        "(": ")",
        "<": ">",
        "{": "}",
    }

    closed_to_open = {v: k for k, v in open_to_closed.items()}

    char_to_score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []

    for line in lines:
        open_brackets = []

        is_valid = True

        for char in line:
            if char in open_to_closed:
                open_brackets.append(char)
            elif char in closed_to_open:
                expected = open_to_closed[open_brackets[-1]]

                if char == expected:
                    open_brackets.pop(-1)

                else:
                    is_valid = False
                    break
            else:
                raise ValueError(char)

        if is_valid:
            chars_to_complete = [open_to_closed[c] for c in open_brackets[::-1]]
            score = 0

            for char in chars_to_complete:
                score *= 5
                score += char_to_score[char]

            scores.append(score)

    return median(scores)

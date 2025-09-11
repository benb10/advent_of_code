def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    open_to_closed = {
        "[": "]",
        "(": ")",
        "<": ">",
        "{": "}",
    }

    closed_to_open = {v: k for k, v in open_to_closed.items()}

    illegal_char_to_score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    score = 0

    for line in lines:
        open_brackets = []

        for char in line:
            if char in open_to_closed:
                open_brackets.append(char)
            elif char in closed_to_open:
                expected = open_to_closed[open_brackets[-1]]

                if char == expected:
                    open_brackets.pop(-1)

                else:
                    score += illegal_char_to_score[char]
                    break
            else:
                raise ValueError(char)

    return score

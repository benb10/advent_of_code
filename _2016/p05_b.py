import hashlib


def run(s: str) -> str:
    input_str = s.strip()

    i = 0
    password: list[str | None] = [None for _ in range(8)]

    while True:
        is_solution, position, value = check_is_solution(input_str, i)

        if is_solution and password[position] is None:
            password[position] = value
            if all(x is not None for x in password):
                return "".join(password)

        i += 1


def check_is_solution(input_str: str, i: int) -> tuple[bool, int | None, str | None]:
    hash_output = hashlib.md5(f"{input_str}{i}".encode()).hexdigest()
    if not hash_output.startswith("00000"):
        return False, None, None

    a = hash_output[5]
    b = hash_output[6]

    is_valid_position = a.isdigit() and 0 <= int(a) <= 7
    if not is_valid_position:
        return False, None, None

    return True, int(a), b

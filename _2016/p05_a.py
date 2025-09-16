import hashlib


def run(s: str) -> str:
    input_str = s.strip()

    i = 0
    password = ""

    while True:
        hash_output = hashlib.md5(f"{input_str}{i}".encode()).hexdigest()
        if hash_output.startswith("00000"):
            next_digit = hash_output[5]
            password += next_digit
            if len(password) == 8:
                return password

        i += 1

import hashlib


def run(s: str) -> int:
    s = s.strip()

    n = 1

    while True:
        output = hashlib.md5(f"{s}{n}".encode()).hexdigest()
        if output.startswith("000000"):
            return n
        n += 1

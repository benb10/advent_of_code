def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    for line in lines:
        start, checksum = line.split("[")
        *words, id_part = start.split("-")
        sector_id = int(id_part)

        new_words = [apply_shift_cipher(word, sector_id) for word in words]

        sentence = " ".join(new_words)

        if sentence == "northpole object storage":
            return sector_id

    return None


def apply_shift_cipher(word: str, offset: int) -> str:
    new_word = ""

    for char in word:
        alphabet_index = ord(char) - 97
        new_alphabet_index = (alphabet_index + offset) % 26
        new_char = chr(new_alphabet_index + 97)
        new_word += new_char

    return new_word

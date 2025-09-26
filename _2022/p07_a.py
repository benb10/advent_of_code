def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    file_to_size: dict[tuple[str, ...], int] = {}
    all_directories: set[tuple[str, ...]] = set()
    current_path = tuple()

    for line in lines:
        words = line.split(" ")

        if words == ["$", "cd", ".."]:
            current_path = current_path[:-1]

        elif words[:2] == ["$", "cd"]:
            current_path += (words[2],)
            all_directories.add(current_path)

        elif words[0].isdigit():
            file_path = current_path + (words[1],)
            size = int(words[0])
            file_to_size[file_path] = size

    total = 0

    for directory in all_directories:
        size = sum(
            size
            for file, size in file_to_size.items()
            if len(file) > len(directory) and file[: len(directory)] == directory
        )
        if size <= 100_000:
            total += size

    return total

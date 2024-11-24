def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    first_line = lines[0]
    seed_num_part = first_line.split(":")[1]
    seed_nums = [int(x) for x in seed_num_part.strip().split(" ")]

    sections = []
    last_line = None
    for line in lines[2:]:
        line = line.strip()
        if line:
            if last_line:
                sections[-1].append(line)
            else:
                # start a new section
                sections.append([line])
        last_line = line

    paths = [[seed_num] for seed_num in seed_nums]

    for section in sections:
        nums_to_process = [path[-1] for path in paths]
        num_to_next_num = {x: x for x in nums_to_process}
        map_lines = section[1:]
        maps = [[int(x) for x in map_line.strip().split(" ")] for map_line in map_lines]
        for map_vals in maps:
            dest_range_start, source_range_start, range_len = map_vals
            source_range_end = source_range_start + range_len
            for num_to_process in nums_to_process:
                if source_range_start <= num_to_process < source_range_end:
                    diff = dest_range_start - source_range_start
                    num_to_next_num[num_to_process] = num_to_process + diff

        next_nums = [num_to_next_num[x] for x in nums_to_process]
        for path, next_num in zip(paths, next_nums):
            path.append(next_num)

    final_nums = [path[-1] for path in paths]
    return min(final_nums)

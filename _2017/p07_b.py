from collections import Counter


def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    programs = set()
    child_to_parent = {}
    parent_to_children = {}
    program_to_self_weight = {}
    program_to_total_weight = {}

    for line in lines:
        words = line.split(" ")
        parent_program = words[0]
        programs.add(parent_program)
        children = [x.replace(",", "") for x in words[3:]]

        for child in children:
            child_to_parent[child] = parent_program

        parent_to_children[parent_program] = children

        weight = int(words[1][1:-1])
        program_to_self_weight[parent_program] = weight
        if not children:
            program_to_total_weight[parent_program] = weight

    program_to_gens_above = {}

    for program in programs:
        current_location = program
        num_gens_above = 0

        while current_location in child_to_parent:
            current_location = child_to_parent[current_location]
            num_gens_above += 1

        program_to_gens_above[program] = num_gens_above

    programs_sorted_child_to_parent = sorted(programs, key=lambda x: -program_to_gens_above[x])

    for program in programs_sorted_child_to_parent:
        if program in program_to_total_weight:
            continue

        children = parent_to_children[program]

        child_weights = [program_to_total_weight[x] for x in children]
        child_weights_all_equal = all(x == child_weights[0] for x in child_weights)

        if not child_weights_all_equal:
            # find the odd one out
            weight_to_count = Counter(child_weights)
            assert len(weight_to_count) == 2
            odd_weight_out = next(weight for weight, count in weight_to_count.items() if count == 1)
            other_weight = next(weight for weight, count in weight_to_count.items() if count > 1)
            diff = other_weight - odd_weight_out
            odd_child = next(child for child in children if program_to_total_weight[child] == odd_weight_out)
            correct_weight = program_to_self_weight[odd_child] + diff
            return correct_weight

        total_weight = program_to_self_weight[program] + sum(child_weights)
        program_to_total_weight[program] = total_weight

    return None

from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    bag_to_inner_bag_counts = {}

    for line in lines:
        outer_bag_color, inner_bags_str = line.split(" bags contain ", 1)
        if inner_bags_str == "no other bags.":
            continue

        inner_bags_str = inner_bags_str.replace(".", "")
        inner_bags_parts = inner_bags_str.split(", ")

        inner_bag_counts = []

        for inner_bags_part in inner_bags_parts:
            num_str, *inner_colour, _ = inner_bags_part.split(" ")
            num = int(num_str)
            colour = " ".join(inner_colour)
            inner_bag_counts.append((colour, num))

        bag_to_inner_bag_counts[outer_bag_color] = inner_bag_counts

    bag_to_count = defaultdict(int)
    bag_to_count["shiny gold"] = 1
    bag_counts_to_process = [("shiny gold", 1)]

    while bag_counts_to_process:
        bag_to_process, bag_count = bag_counts_to_process.pop(0)

        inner_bag_counts = bag_to_inner_bag_counts.get(bag_to_process)
        if not inner_bag_counts:
            # nothing more to add up
            continue

        for inner_bag, num_inner_bags in inner_bag_counts:
            num_inner_bags = bag_count * num_inner_bags
            bag_to_count[inner_bag] += num_inner_bags
            bag_counts_to_process.append((inner_bag, num_inner_bags))

    return sum(bag_to_count.values()) - 1  # -1 so we don't count the shiny gold bag

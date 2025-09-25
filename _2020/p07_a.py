from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    bag_to_outer_bags = defaultdict(set)

    for line in lines:
        outer_bag_color, inner_bags_str = line.split(" bags contain ", 1)
        if inner_bags_str == "no other bags.":
            continue

        inner_bags_str = inner_bags_str.replace(".", "")
        inner_bags_parts = inner_bags_str.split(", ")

        for inner_bags_part in inner_bags_parts:
            _, *inner_colour, _ = inner_bags_part.split(" ")
            colour = " ".join(inner_colour)
            bag_to_outer_bags[colour].add(outer_bag_color)

    bags_to_check = ["shiny gold"]
    possible_outer_bags = set()

    while bags_to_check:
        bag_to_check = bags_to_check.pop(0)
        outer_bags = bag_to_outer_bags[bag_to_check]
        possible_outer_bags.update(outer_bags)
        bags_to_check.extend(outer_bags)

    return len(possible_outer_bags)

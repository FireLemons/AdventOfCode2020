#!/usr/bin/python3
import re

input_bag_data = open("input.txt", "r")

bags_data = {}
valid_bag_color_count = 0

color_lexer = re.compile(r"^(\w+\ \w+)")
contents_lexer = re.compile(r"(\d+)\ (\w+\ \w+)\ bags?")

for line in input_bag_data:
    bag_contents = contents_lexer.findall(line)
    if len(bag_contents):
        bag_color = color_lexer.match(line).group(1)
        for bag_spec in bag_contents:
            minmum_child_quantity = int(bag_spec[0])
            child_color = bag_spec[1]

            if not bag_color in bags_data:
                bags_data[bag_color] = {}

            bag_data = bags_data[bag_color]

            if not "contents" in bag_data:
                bag_data["contents"] = []

            bag_data["contents"].append(child_color)

            if not child_color in bags_data:
                bags_data[child_color] = {}

            child_bag = bags_data[child_color]

            if not "required" in child_bag:
                child_bag["required"] = [[minmum_child_quantity, bag_color]]
            else:
                child_bag["required"].append([minmum_child_quantity, bag_color])

gold_tree_bfs = [bags_data["shiny gold"]]

while len(gold_tree_bfs):
    node = gold_tree_bfs.pop()

    if "required" in node:
        for color in node["required"]:
            color_name = color[1]
            if not "is_member" in bags_data[color_name]:
                bags_data[color_name]["is_member"] = True
                valid_bag_color_count += 1
                gold_tree_bfs.append(bags_data[color_name])

print(valid_bag_color_count)

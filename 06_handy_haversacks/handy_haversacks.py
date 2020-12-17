#!/usr/bin/python3
import re
import pprint

input_bag_data = open("input_simple.txt", "r")

bags_data = {}
valid_bag_color_count = 0

line_lexer = re.compile(r"(\w+\ \w+)\ bags\ contain\ (\d+|no)\ ((\w+\ \w+)\ bags?|other\ bags)(,\ (\d+)\ (\w+\ \w+))?")

for line in input_bag_data:
    line_data = line_lexer.match(line)
    if line_data.group(4):
        bag_color = line_data.group(1)
        minmum_child_quantity = int(line_data.group(2))
        child_color = line_data.group(4)

        if not bag_color in bags_data:
            bags_data[bag_color] = {}

        bag_data = bags_data[bag_color]

        if not "contents" in bag_data:
            bag_data["contents"] = {}

        bag_data["contents"][child_color] = minmum_child_quantity

        if line_data.group(5):
            quantity = int(line_data.group(6))
            color = line_data.group(7)

            if not color in bags_data:
                bags_data[color] = {}

            bag_prime_data = bags_data[color]

            if not quantity in bag_prime_data:
                bag_prime_data["quantity"] = quantity
            else:
                bag_prime_data["quantity"] += quantity
        
pprint.pprint(bags_data)
print(valid_bag_color_count)

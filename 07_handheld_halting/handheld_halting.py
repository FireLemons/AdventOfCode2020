#!/usr/bin/python
import re
import pprint

line_lexer = re.compile(r"(nop|acc|jmp)\ ([+-]\d+)")

def process_line(line):
    line_data = line_lexer.search(line).groups()
    return [line_data[0], int(line_data[1])]

input_instructions = open("input.txt", "r").read().split("\n")
input_instructions.pop()
input_instructions = map(process_line, input_instructions)

pprint.pprint(input_instructions)

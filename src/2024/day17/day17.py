import os
import re

file_path = os.path.join(os.path.dirname(__file__), "day17.txt")

with open(file_path, "r") as file:
    contents = file.read()

a, b, c, *program = map(int, re.findall(r"\d+", contents))

## Part 1
def combo(operand):
    if 0 <= operand <= 3:return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    else: raise RuntimeError("Bad operand",operand)

pointer = 0
output = []
while pointer < len(program):
    op = program[pointer]
    operand = program[pointer + 1]
    if op == 0: #adv
        a = a >> combo(operand)
    elif op == 1: #bxl
        b = b ^ operand
    elif op == 2: #bst
        b = combo(operand) % 8
    elif op == 3: #jnz
        if a != 0:
            pointer = operand
            continue
    elif op == 4: #bxc
        b = b ^ c
    elif op == 5: #out
        output.append(combo(operand) % 8)
    elif op == 6: #bdv
        b = a >> combo(operand)
    elif op == 7: #cdv
        c = a >> combo(operand)
    pointer += 2

output_string = ",".join(map(str, output))
assert output_string == "7,6,5,3,6,5,7,0,4"

## Part 2
def find(program,ans):
    if program == []: return ans
    for t in range(8):
        a = (ans << 3) + t
        b = a % 8
        b = b ^ 2
        c = a >> b
        # a = a >> 3
        b = b ^ 7
        b = b ^ c
        if(b % 8 == program[-1]):
            sub = find(program[:-1],a)
            if(sub) is None: continue
            return sub

register_A = find(program,0)
assert register_A == 190615597431823
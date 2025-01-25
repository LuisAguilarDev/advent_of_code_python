import os
import re

## Part 1
file_path = os.path.join(os.path.dirname(__file__), "day24.txt")
with open(file_path, "r") as file:
    contents = file.read().split("\n")

known = {}
formulas = {}

for line in contents:
    if line == '':continue
    if ":" in line:
        x,y = line.split(": ")
        known[x] = int(y)
    else:
        x,op,y,wire = line.replace(" ->","").split()
        formulas[wire] = (op,x,y)

operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y
}
## modifies original known
def calc(wire) -> int :
    if wire in known: return known[wire]
    op,x,y = formulas[wire]
    known[wire] = operators[op](calc(x),calc(y))
    return known[wire]

z = []
i = 0
while True:
    key = "z" + str(i).rjust(2,"0")
    if key not in formulas: break
    z.append(calc(key))
    i += 1

## two lines modifies the original
## z.reverse()
## print(int("".join(map(str,z)),2))

## list[???] creates a copy look for syntax
p1 = int("".join(map(str,z[::-1])),2)
assert p1 == 60714423975686

## Part 2
known = {}
formulas = {}

for line in contents:
    if line == '':continue
    if ":" in line:
        x,y = line.split(": ")
        known[x] = int(y)
    else:
        x,op,y,wire = line.replace(" ->","").split()
        formulas[wire] = (op,x,y)

## identifies operations to get the sum
# def pp(wire,depth=0):
#     if wire[0] in "xy": return "  " * depth + wire
#     op,x,y = formulas[wire]
#     return " " * depth + op + " (" + wire + ")\n" + pp(x,depth+1) + "\n" + pp(y,depth + 1)
# print(pp("z01"))
def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def verify_z(wire, num):
    # print("vz", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x, y]) == ["x00", "y00"]
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify_intermediate_xor(wire, num):
    # print("vx", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    # print("vc", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)

def verify_direct_carry(wire, num):
    # print("vd", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "AND": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    # print("vr", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "AND": return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify(num):
    return verify_z(make_wire("z", num), num)

def progress():
    i = 0
    
    while True:
        if not verify(i): break
        i += 1
    
    return i

swaps = []

for _ in range(1):
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]

print(",".join(sorted(swaps)))
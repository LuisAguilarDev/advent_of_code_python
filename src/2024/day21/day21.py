from collections import deque
from itertools import product
from functools import cache
import os

# content can be piped trought comand line
# cat src/day21/test.txt | python src/day21/day21.py
# for line in open(0).read().splitlines():
#     print(line)
#     print(solve(line,num_keypad))

file_path = os.path.join(os.path.dirname(__file__), "day21.txt")

with open(file_path, "r") as file:
    contents = file.read()
codes = contents.split("\n")
def compute_seqs(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r,c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x,y)] = ["A"]
                continue
            posibilites = []
            q = deque([(pos[x],"")])
            optimal = float("inf")
            while q:
                (r,c),moves = q.popleft()
                for nr,nc,nm in [(r-1,c,"^"),(r+1,c,"v"),(r,c-1,"<"),(r,c+1,">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]):continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1:break
                        optimal = len(moves) +1
                        posibilites.append(moves+nm+"A")
                    else:
                        q.append(((nr,nc),moves+nm))
                else:
                    continue
                break
            seqs[(x,y)] = posibilites
    return seqs

def solve(string,seqs):
    options = [seqs[(x,y)] for x,y in zip("A" + string,string)]
    return ["".join(x) for x in product(*options)]

num_keypad = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"]
]
num_seqs = compute_seqs(num_keypad)
dir_keypad = [
    [None,"^","A"],
    ["<","v",">"]
]
dir_seqs = compute_seqs(dir_keypad)
dir_lengths = {key: len(value[0]) for key,value in dir_seqs.items()}
total = 0
# part1
for code in codes:
    robot1 = solve(code,num_seqs)
    next = robot1
    for _ in range(2):
        possible_next = []
        for seq in next:
            possible_next += solve(seq,dir_seqs)
        minlength = min(map(len,possible_next))
        next = [seq for seq in possible_next if len(seq) == minlength]
    length = len(next[0])
    complexity = length * int(code[:-1])
    total += complexity

print(total)
assert(total == 212488)

# part2
@cache
def compute_length(seq,depth=25):
    if depth == 1:
        return sum(dir_lengths[(x,y)] for x,y in zip("A"+seq,seq))
    length = 0
    for x,y in zip("A"+seq,seq):
        length += min(compute_length(subseq,depth - 1) for subseq in dir_seqs[(x,y)])
    return length

total2 = 0
for code in codes:
    inputs = solve(code,num_seqs)
    length = min(map(compute_length,inputs))
    complexity = length * int(code[:-1])
    total2 += complexity
print(total2)
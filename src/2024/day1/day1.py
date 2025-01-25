import os
import re

file_path = os.path.join(os.path.dirname(__file__), "day1.txt")

with open(file_path, "r") as file:
    contents = file.read().splitlines()

# Part 1
lists = list(map(list,zip(*[list(map(int,line.split())) for line in contents])))
for l in lists: l.sort()
result = sum([abs(x-y) for x,y in zip(*lists)])

assert(result == 2375403)

# Part 2
l,r = list(map(list,zip(*[list(map(int,line.split())) for line in contents])))
result2 = sum([x * r.count(x) for x in l])

assert(result2 == 23082277)
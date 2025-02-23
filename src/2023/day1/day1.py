import os
import re

file_path = os.path.join(os.path.dirname(__file__), "day1.txt")

with open(file_path, "r") as file:
    contents = file.read().splitlines()

# Part 1
total = 0
for line in contents:
    list_number = re.findall(r'\d+',line)
    number = "".join(list_number)
    if not number: continue
    if len(number) == 1:
        total += int(number + number)
    else: total += int(number[0] + number[-1])

assert(total == 54573)

# Part 2
numbers = {"one": "1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

def get_number(s:str):
    if s in numbers:
        return numbers[s]
    return s

with open(file_path, "r") as file:
    contents = file.read().splitlines()

pattern = "(?=(" + "|".join(numbers.keys()) + "|" + "\d))"
p = re.compile(pattern)

total = 0
for line in contents:
    matches = re.findall(p, line)
    if len(matches) == 0: continue
    nums = list(map(get_number,matches))
    total += int(nums[0] + nums[-1])

# first iteration
# for line in contents:
#     matches = re.findall(p, line)
#     if len(matches) == 0:
#         continue
#     if len(matches) == 1:
#         str_num = matches[0]
#         sum += int(str_num + str_num) if len(str_num) == 1 else int(numbers[str_num] + numbers[str_num])
#         continue
#     n1,n2 = matches[0],matches[-1]
#     if len(n1) == 1 and len(n2) == 1:
#         sum += int(n1 + n2) 
#     elif not len(n1) == 1 and len(n2) == 1:
#         sum += int(numbers[n1] + n2)
#     elif len(n1) == 1 and not len(n2) == 1:
#         sum += int(n1 + numbers[n2])
#     else: sum += int(numbers[n1] + numbers[n2])

assert(total == 54591)
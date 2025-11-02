import math
import os
# ---- Day 6: Wait For It ----
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sample_path = os.path.join(os.path.dirname(__file__), "sample.txt")
with open(file_path, "r") as file:
    contents = file.read().splitlines()
with open(sample_path, "r") as file:
    sample_contents = file.read().splitlines()

# Part 1
for line in contents:
    if line.startswith("Time:"):
        times = line.split(":")[1].strip().split()
    if line.startswith("Distance:"):
        distances = line.split(":")[1].strip().split()

all_posibles = []
for race in range(len(times)):
    time = int(times[race])
    distance = int(distances[race])
    pressed_time_button = time
    posibilities = 0
    while pressed_time_button > 0:
        speed = pressed_time_button
        distance_covered = speed * (time - pressed_time_button)
        if distance_covered > int(distance):
            posibilities += 1
        pressed_time_button -= 1
    all_posibles.append(posibilities)

result = math.prod(all_posibles)

# Part 2

# Cuadratic equation: x^2 - time*x + distance = 0
for line in contents:
    if line.startswith("Time:"):
        t_time = "".join(line.split(":")[1].strip().split())
    if line.startswith("Distance:"):
        t_distance = "".join(line.split(":")[1].strip().split())

time = int(t_time)
distance = int(t_distance)

xt1 = (time + math.sqrt(time**2 - 4 * 1 * distance)) / 2
xt2 = (time - math.sqrt(time**2 - 4 * 1 * distance)) / 2

if xt1 > xt2:
    xt1, xt2 = xt2, xt1

xt1 = math.ceil(xt1)
xt2 = math.floor(xt2)

result = xt2 - xt1 + 1
print("Result cuadratic approach:", result)

# Hyper neutrino
n = 1
margin = 0
for hold in range(time):
    if hold * (time - hold) >= distance:
        margin += 1
n *= margin

print("Result binary search approach:", n)

# Binary search approach
# ???

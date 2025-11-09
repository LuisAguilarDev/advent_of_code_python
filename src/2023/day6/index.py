import math
from global_utils.utils import read_file
from global_utils.logger import logger
import time

logger.info("---- Day 6: Wait For It ----")

contents = read_file("input.txt")
sample_contents = read_file("sample.txt")

logger.info("Part 1")


def get_time_distance_lists(contents):
    times = []
    distances = []
    for line in contents:
        if line.startswith("Time:"):
            times = line.split(":")[1].strip().split()
        if line.startswith("Distance:"):
            distances = line.split(":")[1].strip().split()
    return times, distances


times, distances = get_time_distance_lists(contents)


def get_product_of_possibilities(times, distances):
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
    return math.prod(all_posibles)


result = get_product_of_possibilities(times, distances)
logger.info(f"Result part 1: {result}")
assert (result == 449820)

logger.info("Part 2")


def get_time_distance(contents):
    for line in contents:
        if line.startswith("Time:"):
            t_time = "".join(line.split(":")[1].strip().split())
        if line.startswith("Distance:"):
            t_distance = "".join(line.split(":")[1].strip().split())
    return int(t_time), int(t_distance)


race_time, race_distance = get_time_distance(contents)

# Cuadratic equation: x^2 - time*x + distance = 0


def cuadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2


def get_ways_to_beat_cuadratic(race_time, race_distance):
    xt1, xt2 = cuadratic_equation(1, -race_time, race_distance)
    if xt1 > xt2:
        xt1, xt2 = xt2, xt1

    xt1 = math.ceil(xt1)
    xt2 = math.floor(xt2)
    return xt2 - xt1 + 1


result = get_ways_to_beat_cuadratic(race_time, race_distance)
logger.info(f"Result cuadratic equation approach: {result}")
assert (result == 42250895)


# Hyper neutrino solution
# time_start = time.time()
# n = 1
# margin = 0
# for hold in range(race_time):
#     if hold * (race_time - hold) >= race_distance:
#         margin += 1
# n *= margin
# time_end = time.time()
# execution_time = time_end - time_start
# logger.info(
#     f"Execution time for hyper neutrino approach: {execution_time:.6f} seconds")
# logger.info(f"Result hyper neutrino approach: {n}")


def binary_search_approach(race_time, race_distance):
    # Find the minimum hold time that beats the distance
    low = 0
    high = race_time
    min_hold = race_time + 1
    while low <= high:
        mid = (low + high) // 2
        if mid * (race_time - mid) >= race_distance:
            min_hold = mid
            high = mid - 1
        else:
            low = mid + 1

    # Find the maximum hold time that beats the distance
    # low = 0
    # high = race_time
    # max_hold = -1
    # while low <= high:
    #     mid = (low + high) // 2
    #     if mid * (race_time - mid) >= race_distance:
    #         max_hold = mid
    #         low = mid + 1
    #     else:
    #         high = mid - 1

    # if min_hold > max_hold:
    #     return 0

    # the max is not required since the function is symmetric
    return (race_time - min_hold) - min_hold + 1


time_start = time.time()
result = binary_search_approach(race_time, race_distance)
time_end = time.time()
execution_time = time_end - time_start
logger.info(f"Result binary search approach: {result}")
assert (result == 42250895)
logger.info(
    f"Execution time for binary search approach: {execution_time:.6f} seconds")

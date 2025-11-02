import os
# ---- Day 5: If You Give A Seed A Fertilizer ----
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sample_path = os.path.join(os.path.dirname(__file__), "sample.txt")
with open(file_path, "r") as file:
    contents = file.read().splitlines()
with open(sample_path, "r") as file:
    sample_contents = file.read().splitlines()

# Part 1
seeds = list()
current_section = None
maps = dict()

areas = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
         "water-to-light", "light-to-temperature", "temperature-to-humidity",
         "humidity-to-location"]

for line in contents:
    if line.startswith("seeds:"):
        seeds = [int(seed) for seed in line.split(":")[1].strip().split()]
    if not line:
        current_section = None
        continue
    if current_section:
        if current_section not in maps:
            maps[current_section] = []
        maps[current_section].append([int(x) for x in line.split()])

    for area in areas:
        if line.startswith(area):
            current_section = area
            break

# build the ranges and final numbers


def get_min_location_from_seeds(seeds):
    result_min = float('inf')
    # part 2 caching
    cache = {}
    for seed in seeds:
        if seed in cache:
            result_min = min(result_min, cache[seed])
            continue
        seed_num = seed
        # seed -> soil
        current_number = seed_num
        next_number = None
        for area in areas:
            lines = maps.get(area)
            for line in lines:
                soil, seed, r = line
                start, end = [seed, seed + r - 1]
                if start <= current_number <= end:
                    next_number = current_number + soil - seed
                    break
            else:
                next_number = current_number
            current_number = next_number
            next_number = None
        cache[seed] = current_number
        result_min = min(result_min, current_number)
    return result_min


result_min = get_min_location_from_seeds(seeds)

# assert (result_min == 836040384)

# Part 2


def get_min_location_from_seeds_optimized(seeds):
    current_ranges = list()
    for seed_i in range(0, len(seeds), 2):
        next_ranges = list()
        seed_num = seeds[seed_i]
        seed_range = seeds[seed_i + 1]
        current_ranges.append((seed_num, seed_num + seed_range - 1))

    # seed -> soil
    iteration = 0
    for area in areas:
        iteration += 1
        lines = maps.get(area)
        area_ranges = []
        for line in lines:
            soil, seed, r = line
            start, end = [seed, seed + r - 1]
            area_ranges.append((start, end, soil - seed))
        area_ranges.sort()
        while current_ranges:
            c_start, c_end = current_ranges.pop(0)
            overlap_found = False
            total = len(area_ranges)
            current = 0
            for a_start, a_end, offset in area_ranges:
                current += 1
                if a_end < c_start:
                    continue
                if a_start > c_end:
                    break
                # overlap
                overlap_found = True
                n_start = max(c_start, a_start) + offset
                n_end = min(c_end, a_end) + offset

                # outside the ranges we keep the same values
                if n_end + 1 - offset <= c_end and current == total:
                    next_ranges.append((n_end + 1 - offset, c_end))
                if current == 1 and a_start > c_start:
                    next_ranges.append((c_start, n_start - 1 - offset))

                next_ranges.append((n_start, n_end))
            if not overlap_found:
                next_ranges.append((c_start, c_end))
        current_ranges = next_ranges
        next_ranges = list()
    return sorted(current_ranges)[0][0]


result = get_min_location_from_seeds_optimized(seeds)

assert (result == 10834440)

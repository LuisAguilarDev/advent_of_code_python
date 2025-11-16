from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    seeds = list()
    maps = list()
    current_section = -1
    for line in contents:
        if line.startswith("seeds:"):
            seeds = [int(seed) for seed in line.split(":")[1].strip().split()]
            continue
        if not line:
            continue
        if "map" in line:
            current_section += 1
            maps.append([])
            continue
        if current_section >= 0:
            maps[current_section].append([int(x) for x in line.split()])
    return seeds, maps


def get_min_location_from_seeds(seeds, maps):
    result_min = float('inf')
    for seed in seeds:
        seed_num = seed
        current_number = seed_num
        next_number = None
        for area in maps:
            for info in area:
                soil, seed, r = info
                start, end = [seed, seed + r - 1]
                if start <= current_number <= end:
                    next_number = current_number + soil - seed
                    break
            else:
                next_number = current_number
            current_number = next_number
            next_number = None
        result_min = min(result_min, current_number)
    return result_min


def get_range_seeds(seeds):
    ranges = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i + 1]
        ranges.append((start, start + length - 1))
    return ranges


def get_min_location_from_seeds_optimized(seeds, maps):
    current_ranges = get_range_seeds(seeds)

    for area in maps:
        current_ranges = get_new_ranges(current_ranges, area)

    current_ranges.sort()
    return current_ranges[0][0]


def get_area_ranges(area):
    area_ranges = []
    for dest_start, source_start, length in area:
        source_end = source_start + length - 1
        offset = dest_start - source_start
        area_ranges.append((source_start, source_end, offset))
    return area_ranges


def get_new_ranges(current_ranges, area):
    area_ranges = get_area_ranges(area)
    next_ranges = []
    for c_start, c_end in current_ranges:
        next_ranges.extend(
            transform_single_range(c_start, c_end, area_ranges))

    return next_ranges


def transform_single_range(c_start, c_end, area_ranges):
    result_ranges = []
    remaining_start = c_start
    area_ranges.sort()  # To process each area from lowest to highest

    for a_start, a_end, offset in area_ranges:
        if a_end < remaining_start:
            continue  # Area range is completely before remaining range
        if a_start > c_end:
            break  # Area range is completely after current range

        # Handle the part before this area range (if any)
        if remaining_start < a_start:
            result_ranges.append((remaining_start, a_start - 1))
            remaining_start = a_start

        # Handle the overlap
        overlap_start = max(remaining_start, a_start)
        overlap_end = min(c_end, a_end)
        if overlap_start <= overlap_end:
            transformed_start = overlap_start + offset
            transformed_end = overlap_end + offset
            result_ranges.append((transformed_start, transformed_end))
            remaining_start = overlap_end + 1
    return result_ranges


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    seeds, maps = parse_data(contents)
    return 836040384 == get_min_location_from_seeds(seeds, maps)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    seeds, maps = parse_data(contents)
    return 10834440 == get_min_location_from_seeds_optimized(seeds, maps)


def main():
    logger.info("---- Day 5: If You Give A Seed A Fertilizer ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

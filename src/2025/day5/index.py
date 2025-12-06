from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents) -> list[tuple[int]]:
    ranges = list()
    ingredients_ids = list()
    isRange = True
    for line in contents:
        if not line.strip():
            isRange = False
            continue
        if isRange:
            ranges.append(tuple(map(int, line.split("-"))))
        else:
            ingredients_ids.append(int(line))
    return ranges, ingredients_ids


def combined_ranges(ranges: list[tuple[int]]) -> list[tuple[int]]:
    # Sort ranges by start value
    ranges.sort()
    combined = []
    last_start, last_end = ranges[0]

    for c_start, c_end in ranges[1:]:
        # is overlapped
        if c_start <= (last_end + 1):
            last_end = max(last_end, c_end)
            continue
        # is not overlapped
        combined.append((last_start, last_end))
        last_start, last_end = c_start, c_end
    combined.append((last_start, last_end))
    return combined


def count_fresh_ingredients(ranges: list[tuple[int]], ingredients_ids: list[int]) -> int:
    fresh_ingredients = 0
    for ingredient_id in ingredients_ids:
        for r_start, r_end in ranges:
            if r_start <= ingredient_id <= r_end:
                break
        else:
            continue
        fresh_ingredients += 1
    return fresh_ingredients


def count_valid_ids(ranges: list[tuple[int]]) -> int:
    valid_ids = 0
    for r_start, r_end in ranges:
        valid_ids += (r_end - r_start + 1)
    return valid_ids


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    ranges, ingredients_ids = parse_data(contents)
    def_ranges = combined_ranges(ranges)
    total = count_fresh_ingredients(def_ranges, ingredients_ids)
    logger.info(f"Total fresh ingredients: {total}")
    return 511 == total


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    ranges, ingredients_ids = parse_data(contents)
    def_ranges = combined_ranges(ranges)
    sum = count_valid_ids(def_ranges)
    logger.info(f"Sum Part 2: {sum}")
    return 350939902751909 == sum


def main():
    logger.info("---- Day 5: Cafeteria ----")
    # result_part_1 = do_part_1()
    # assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

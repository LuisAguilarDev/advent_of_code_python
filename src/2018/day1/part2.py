from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    vars = list()
    for line in contents:
        vars.append(line)
    return vars

def get_repeated_frequency(vars) -> int:
    seen = dict()
    frequency = 0
    seen[frequency] = 1
    index = 0
    while True:
        for var in vars:
            frequency += int(var)
            if frequency not in seen:
                seen[frequency] = 0
            seen[frequency] += 1
            if seen[frequency] > 1:
                return frequency
        index += 1

def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("data/input.txt")
    vars = parse_data(contents)
    freq = get_repeated_frequency(vars)
    logger.info(f"Password Part 2: {freq}")
    return 709 == freq
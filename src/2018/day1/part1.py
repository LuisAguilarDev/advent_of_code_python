from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    vars = list()
    for line in contents:
        vars.append(line)
    return vars


def get_frecuency_value(vars) -> int:
    freq = 0
    for var in vars:
        freq += int(var)
    return freq

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("data/input.txt")
    vars = parse_data(contents)
    freq = get_frecuency_value(vars)
    logger.info(f"Value: {freq}")
    return 500 == freq
import math

from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    seqs = list()
    for line in contents:
        seqs.append((line[0], int(line[1:])))
    return seqs


def get_password(seqs) -> int:
    password = 0
    dial = 50
    for direction, steps in seqs:
        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100
        if dial == 0:
            password += 1
    return password


def get_password_part_2(seqs) -> int:
    password = 0
    dial = 50
    for direction, steps in seqs:
        if direction == "R":
            if dial + steps > 99:
                password += (dial + steps) // 100
            dial = (dial + steps) % 100
        else:
            if dial - steps < 0:
                password += math.ceil((steps - dial) / 100)
            dial = (dial - steps) % 100
    return password


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    seqs = parse_data(contents)
    password = get_password(seqs)
    logger.info(f"Password: {password}")
    return 1154 == password


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    seqs = parse_data(contents)
    password = get_password_part_2(seqs)
    logger.info(f"Password Part 2: {password}")
    return 6819 == password


def main():
    logger.info("---- Day 1: Secret Entrance ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

from global_utils.utils import read_file
from global_utils.logger import logger

# . is ground, there is no pipe in this tile.
# S is the starting position of the animal # there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# dict(symbol: list((dr,dc)))
directions = {
    "-": [(0, 1), (0, -1)],
    "|": [(-1, 0), (1, 0)],
    "L": [(1, 0), (0, 1)],
    "J": [(1, 0), (0, -1)],
    "7": [(-1, 0), (0, -1)],
    "F": [(-1, 0), (0, 1)],
}


def parse_data(contents):
    pass


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    sequences = parse_data(contents)
    # logger.info(result)
    # return 1696140818 == result
    return True


# def do_part_2() -> bool:
#     logger.info(f"Part 2")
#     contents = read_file("input.txt")
#     sequences = parse_data(contents)
#     result = get_sum_from_past_values(sequences)
#     logger.info(result)
#     return 1152 == result


def main():
    logger.info("---- Day 10: Pipe Maze ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    # result_part_2 = do_part_2()
    # assert (True == result_part_2)


if __name__ == "__main__":
    main()

from global_utils.logger import logger
from .part1 import do_part_1
from .part2 import do_part_2


def main():
    logger.info("---- Day 1: Chronal Calibration ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

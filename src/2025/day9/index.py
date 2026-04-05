from global_utils.logger import logger
from .part1 import do_part_1
from .part2 import do_part_2

def main() -> None:
    logger.info("---- Day 9: Movie Theater ----")
    result_part_1: bool = do_part_1()
    assert True == result_part_1
    result_part_2: bool = do_part_2()
    assert True == result_part_2


if __name__ == "__main__":
    main()
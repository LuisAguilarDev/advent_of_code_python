from global_utils.logger import logger
from .part1 import do_part_1


def main() -> None:
    logger.info("--- Day 10: The Stars Align ---")
    result_part_1: bool = do_part_1()
    assert True == result_part_1


if __name__ == "__main__":
    main()

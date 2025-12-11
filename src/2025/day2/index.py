from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    for line in contents:
        ranges = line.split(",")
        return list(map(lambda x: list(map(int, x.split("-"))), ranges))


def get_sum_invalid_ids(ranges: list[list[str]]) -> int:
    sum = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            i_str = str(i)
            if len(i_str) % 2 == 1:
                continue
            mid = len(i_str) // 2
            left = i_str[:mid]
            right = i_str[mid:]
            if left == right:
                sum += i
    return sum


def is_invalid(i_str: str) -> bool:
    """
    Build the posible patterns by repeating substrings and compare
    with the original string.
    from length 1 to half the length of the string
    """
    for seq_len in range(1, len(i_str) // 2 + 1):
        pattern = i_str[:seq_len] * (len(i_str) // seq_len)
        if pattern == i_str:
            return True
    return False


def get_sum_invalid_ids_2(ranges: list[list[str]]) -> int:
    sum = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            i_str = str(i)
            if len(i_str) == 1:
                continue
            if is_invalid(i_str):
                sum += i
    return sum


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    ranges = parse_data(contents)
    sum = get_sum_invalid_ids(ranges)
    logger.info(f"Sum: {sum}")
    return 56660955519 == sum


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    ranges = parse_data(contents)
    sum = get_sum_invalid_ids_2(ranges)
    logger.info(f"Sum Part 2: {sum}")
    return 79183223243 == sum


def main():
    logger.info("---- Day 2: Gift Shop ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

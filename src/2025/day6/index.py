from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents) -> list[list[str]]:
    grid = list()
    for line in contents:
        dirty_list = line.split(" ")
        clean_list = list(filter(lambda x: x != "", dirty_list))
        grid.append(clean_list)
    return grid


def calculate_cephalodpod_math_part_1(grid: list[list[str]]) -> int:
    R = len(grid)
    C = len(grid[0])
    total = []
    for r in range(R):
        # we dont process the last row
        if r == R - 1:
            continue
        # we use the first row as list(integers)
        if r == 0:
            total = [int(x) for x in grid[r]]
            continue
        else:
            for c,symbol in enumerate(grid[R-1],0):
                if symbol == "+":
                    total[c] += int(grid[r][c])
                else:
                    total[c] *= int(grid[r][c])
    return sum(total)


# Part 2
def parse_data_2(contents) -> list[list[str]]:
    grid = list()
    R = len(contents)
    for r, line in enumerate(contents):
        dirty_list = list(line)
        if r < R - 1:
            clean_list = list(map(lambda x: 0 if x == "" else x, dirty_list))
        else:
            clean_list = list(filter(lambda x: x != "", list(map(str.strip, dirty_list))))
        grid.append(clean_list)
    return grid

def calculate_cephalodpod_math_part_2(grid: list[list[str]]) -> int:
    R = len(grid) - 1
    C = len(grid[0]) - 1
    total = []
    index_symbol = len(grid[R]) - 1
    total = []
    current_result = 0
    for c in range(C,-1,-1):
        symbol = grid[R][index_symbol]
        value = ""
        for r in range(R):
            value += grid[r][c]
        if value.strip() == "":
            if current_result != 0:
                total.append(current_result)
            current_result = 0
            index_symbol -= 1
            continue
        if symbol == "+":
            current_result += int(value)
        else:
            if current_result == 0:
                current_result = 1
            current_result *= int(value)
    if current_result != 0 and current_result != "":
        total.append(current_result)
    return sum(total)


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    grid = parse_data(contents)
    result = calculate_cephalodpod_math_part_1(grid)
    logger.info(f"Result Part 1: {result}")
    return 4580995422905 == result


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    grid = parse_data_2(contents)
    result = calculate_cephalodpod_math_part_2(grid)
    logger.info(f"Result Part 2: {result}")
    return 10875057285868 == result


def main():
    logger.info("---- Day 6: Trash Compactor ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

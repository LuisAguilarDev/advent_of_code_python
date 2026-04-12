from global_utils.logger import logger


def get_power_level(x: int, y: int, serial_number: int) -> list[tuple[int, int, int, int]]:
    """Gets the power level based on the calculation given on the excercise"""
    rack_ID = x + 10
    power_level = rack_ID * y + serial_number
    power_level = rack_ID * power_level
    power_level = int(str(power_level)[-3])
    return power_level - 5


def get_power_levels(serial_number):
    power_levels = dict()
    max = 300
    for x in range(1, max + 1):
        for y in range(1, max + 1):
            power_levels[(x, y)] = get_power_level(x, y, serial_number)
    return power_levels


def get_best_area(serial_number: int) -> str:
    base_power_levels = get_power_levels(serial_number)
    size = 300
    # build SAT summed-area table
    sat = [[0] * (size + 1) for _ in range(size + 1)]
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            sat[x][y] = (base_power_levels[(x, y)]
                         + sat[x-1][y]
                         + sat[x][y-1]
                         - sat[x-1][y-1])

    best = float('-inf')
    solution = None
    for a in range(1, size + 1):
        for x in range(1, size - a + 2):
            for y in range(1, size - a + 2):
                total = (sat[x+a-1][y+a-1]
                         - sat[x-1][y+a-1]
                         - sat[x+a-1][y-1]
                         + sat[x-1][y-1])
                if total > best:
                    best = total
                    solution = f"{x},{y},{a}"

    return solution


def do_part_2() -> bool:
    serial_number = 5034
    solution = get_best_area(serial_number)

    logger.info("Part 2")
    logger.info(f"Solution:\n{solution}")
    return solution == "229,251,16"

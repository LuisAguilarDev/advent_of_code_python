from global_utils.logger import logger


def get_power_level(x: int, y: int, serial_number: int) -> list[tuple[int, int, int, int]]:
    """Gets the power level based on the calculation given on the excercise"""
    rack_ID = x + 10
    power_level = rack_ID * y + serial_number
    power_level = rack_ID * power_level
    power_level = int(str(power_level)[-3])
    return power_level - 5


def get_area_power_level(X: int, Y: int, area_size: int, power_levels: dict, base_power_levels: dict) -> int:
    # reuse the previously calculated (area_size-1) x (area_size-1) total
    previous_total = power_levels.get((X, Y), 0)

    # add the new last column (x = X + area_size - 1, full height)
    for y in range(Y, Y + area_size):
        previous_total += base_power_levels[(X + area_size - 1, y)]

    # add the new last row (y = Y + area_size - 1, excluding corner already counted)
    for x in range(X, X + area_size - 1):
        previous_total += base_power_levels[(x, Y + area_size - 1)]
    
    return previous_total


def get_power_levels(serial_number):
    power_levels = dict()
    max = 300
    for x in range(1,max + 1):
        for y in range(1,max + 1):
            power_levels[(x,y)] = get_power_level(x,y,serial_number)
    return power_levels

def get_best_area(serial_number):
    base_power_levels = get_power_levels(serial_number)
    print(base_power_levels)
    power_levels = base_power_levels.copy()
    max = 300
    solution = None
    best_power_level = float('-inf')
    for a in range(2,max + 1):
        print(f"current_area={a}")
        for x in range(1,max - a + 2):
            for y in range(1,max - a + 2):
                apl = get_area_power_level(x,y,a,power_levels,base_power_levels)
                power_levels[(x, y)] = apl
                if apl > best_power_level:
                    print(f"found best={apl},sol{x},{y},{a}")
                    best_power_level = apl
                    solution = f"{x},{y},{a}"
    return solution

def do_part_2() -> bool:
    serial_number = 5034
    solution = get_best_area(serial_number)

    logger.info("Part 2")
    logger.info(f"Solution:\n{solution}")
    return solution == "229,251,16"

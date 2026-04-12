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
    for x in range(1,max + 1):
        for y in range(1,max + 1):
            power_levels[(x,y)] = get_power_level(x,y,serial_number)
    return power_levels

def get_area_power_level(X: int, Y: int, serial_number: int, power_levels: dict) -> int:
    total_power_level = 0
    for x in range(X, X + 3):
        for y in range(Y, Y + 3):
            total_power_level += power_levels.get((x, y))
    return total_power_level

def get_coordinate(serial_number: int)-> None | int:
    best_coordinate = None
    best_power_level = -1
    power_levels = get_power_levels(serial_number)
    max = 300
    for x in range(1, max - 1): # 3x3 area, so we need to stop at max - 1 to avoid out of bounds
        for y in range(1, max - 1): # 3x3 area, so we need to stop at max - 1 to avoid out of bounds
            c_pl = get_area_power_level(x, y, serial_number, power_levels)
            if c_pl > best_power_level:
                best_power_level = c_pl
                best_coordinate = str(x) + "," + str(y)
    return best_coordinate

def do_part_1() -> bool:
    serial_number = 5034
    coordinate = get_coordinate(serial_number)
    logger.info("Part 1")
    logger.info(f"Result:\n{coordinate}")
    return coordinate == "235,63"

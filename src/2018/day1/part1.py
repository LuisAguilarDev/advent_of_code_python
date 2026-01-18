from global_utils.utils import read_file
from global_utils.logger import logger


def sum_values(numbers) -> int:
    """
    Returns the sum of all elements in the list
    
    numbers is a list of numbers
    """
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum

def do_part_1() -> bool:
    logger.info("Part 1")
    numbers = read_file("data/input.txt")
    # no transformation required
    sum = sum_values(numbers)
    logger.info(f"Sum: {sum}")
    return 500 == sum

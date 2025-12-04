from global_utils.utils import read_file
from global_utils.logger import logger
from graphviz import Digraph


def parse_data(contents) -> list[list[str]]:
    banks = list()
    for line in contents:
        banks.append(list(list(line)))
    return banks


def get_max_in_bank(bank: list[str]) -> int:
    values = set()
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            values.add(int(bank[i] + bank[j]))
    return max(values)


def get_total_joltage(banks: list[list[str]]) -> int:
    total_joltage = 0
    for bank in banks:
        total_joltage += get_max_in_bank("".join(bank))
    return total_joltage


def get_max_joltage(s: str, n: int = 12) -> int:
    result = []
    start = 0

    for i in range(n):
        # Desde la posicion actual cuan lejos puedo ir
        # Necesito dejar (n - i - 1) dígitos después
        end = len(s) - (n - i - 1)
        # Encontrar el máximo en ese rango
        best = start
        for j in range(start, end):
            if s[j] > s[best]:
                best = j

        result.append(s[best])
        start = best + 1

    return int(''.join(result))


def get_total_joltage_part_2(banks: list[list[str]]) -> int:
    total_joltage = 0
    for bank in banks:
        total_joltage += get_max_joltage("".join(bank))
    return total_joltage


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    banks = parse_data(contents)
    total_joltage = get_total_joltage(banks)
    logger.info(f"Total joltage: {total_joltage}")
    return 17109 == total_joltage


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    banks = parse_data(contents)
    sum = get_total_joltage_part_2(banks)
    logger.info(f"Sum Part 2: {sum}")
    return 169347417057382 == sum


def main():
    logger.info("---- Day 2: Gift Shop ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

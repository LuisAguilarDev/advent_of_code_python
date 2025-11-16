from constants.constants import all_directions, horizontal_directions
from global_utils.utils import read_file
from global_utils.logger import logger


def search_numbers_coordinates(matrix, sr, sc):
    visited = set()
    if (sr, sc) in visited:
        return 0
    ROWS, COLS = len(matrix), len(matrix[0])
    stack = list()
    found = list()
    for dr, dc in all_directions:
        nr, nc = sr + dr, sc + dc
        if (nr, nc) in visited or nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
            continue
        char = matrix[nr][nc]
        if char in "0123456789":
            stack.append((nr, nc))
            visited.add((nr, nc))
            found.append((nr, nc))
    while stack:
        r, c = stack.pop()
        for dr, dc in horizontal_directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited or nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                continue
            char = matrix[nr][nc]
            if char in "0123456789":
                found.append((nr, nc))
                visited.add((nr, nc))
                stack.append((nr, nc))
    return found


def get_number_sum(found, matrix):
    total = 0
    found.sort()
    current_number = ""
    lr = found[0][0]
    lc = None
    for r, c in found:
        # 1) is not the same row
        if r != lr:
            if current_number:
                total += int(current_number)
                current_number = ""
            lr = r
            lc = None
        # 2) is not adjacent column
        if lc is not None and c != lc + 1:
            if current_number:
                total += int(current_number)
                current_number = ""
        # 3) is the first number in the row
        current_number += matrix[r][c]
        lc = c
    if current_number:
        total += int(current_number)
    return total


def build_schematic(contents):
    matrix = list()
    for line in contents:
        # split each character and add to list
        row = list(line)
        matrix.append(row)
    return matrix


def sum_of_part_numbers_in_schematic(schematic):
    result = 0
    for r, row in enumerate(schematic):
        for c, char in enumerate(row):
            if char not in "0123456789.":
                coordinates = search_numbers_coordinates(schematic, r, c)
                result += get_number_sum(coordinates, schematic)
    return result


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    base_schematic = build_schematic(contents)
    return 532428 == sum_of_part_numbers_in_schematic(base_schematic)


def get_gear_mul(found, matrix):
    found.sort()
    numbers = list()
    current_number = ""
    lr = found[0][0]
    lc = None
    for r, c in found:
        # 1) is not the same row
        if r != lr:
            if current_number:
                numbers.append(int(current_number))
                current_number = ""
            lr = r
            lc = None
        # 2) is not adjacent column
        if lc is not None and c != lc + 1:
            if current_number:
                numbers.append(int(current_number))
                current_number = ""
        # 3) is the first number in the row
        current_number += matrix[r][c]

        lc = c
    if current_number:
        numbers.append(int(current_number))
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0


def sum_gear_ratio(schematic):
    result = 0
    for r, row in enumerate(schematic):
        for c, char in enumerate(row):
            if char not in "0123456789.":
                coordinates = search_numbers_coordinates(schematic, r, c)
                result += get_gear_mul(coordinates, schematic)
    return result


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    base_schematic = build_schematic(contents)
    return sum_gear_ratio(base_schematic) == 84051670


def main():
    logger.info("---- Day 3: Gear Ratios ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

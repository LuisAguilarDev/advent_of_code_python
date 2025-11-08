import os
import re
from constants.constants import all_directions, horizontal_directions

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sample_path = os.path.join(os.path.dirname(__file__), "sample.txt")
with open(file_path, "r") as file:
    contents = file.read().splitlines()
with open(sample_path, "r") as file:
    sample_contents = file.read().splitlines()

# Part 1
# Build a matrix from input


def search_numbers_coordinates(matrix, sr, sc):
    if (sr, sc) in visited:
        return 0
    ROWS, COLS = len(matrix), len(matrix[0])
    stack = list()
    found = list()
    for dr, dc in all_directions:
        nr, nc = sr + dr, sc + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            continue
        char = matrix[nr][nc]
        if re.match(r"\d", char) and (nr, nc) not in visited:
            stack.append((nr, nc))
            visited.add((nr, nc))
            found.append((nr, nc))
    while stack:
        r, c = stack.pop()
        for dr, dc in horizontal_directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            char = matrix[nr][nc]
            if re.match(r"\d", char) and (nr, nc) not in visited:
                found.append((nr, nc))
                visited.add((nr, nc))
                stack.append((nr, nc))
    return found


def get_number_sum(found):
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


visited = set()
matrix = list()
for line in contents:
    # split each character and add to list
    row = list(line)
    matrix.append(row)

result = 0
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if re.match(r"[^\d.]", char):
            coordinates = search_numbers_coordinates(matrix, r, c)
            result += get_number_sum(coordinates)

assert (result == 532428)

# Part 2
# gear any symbol


def get_gear_mul(found):
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


visited = set()
result = 0
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if re.match(r"[^\d.]", char):
            coordinates = search_numbers_coordinates(matrix, r, c)
            result += get_gear_mul(coordinates)

assert (result == 84051670)

# guardar en una estructura de datos los numeros y sus posiciones
# recorrer la estructura de datos y buscar los numeros adyacentes
# formar los numeros y sumarlos
# para la parte 2, multiplicar los numeros en lugar de sumarlos

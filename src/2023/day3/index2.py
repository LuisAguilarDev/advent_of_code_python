from global_utils.utils import read_file
from global_utils.logger import logger

logger.info("---- Day 3: Gear Ratios (Alternative Approach) ----")

contents = read_file("input.txt")
sample_contents = read_file("sample.txt")

logger.info("Part 1")

matrix = [list(line.strip()) for line in contents]


def extract_numbers(matrix):
    """Extrae todos los números con sus posiciones (fila, col_inicio, col_fin, valor)"""
    numbers = []
    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        c = 0
        while c < COLS:
            if matrix[r][c].isdigit():
                # Encontramos el inicio de un número
                start_col = c
                number_str = ""

                # Recolectar todos los dígitos del número
                while c < COLS and matrix[r][c].isdigit():
                    number_str += matrix[r][c]
                    c += 1

                end_col = c - 1
                numbers.append((r, start_col, end_col, int(number_str)))
            else:
                c += 1

    return numbers


def extract_symbols(matrix):
    """Extrae todas las posiciones de símbolos (no dígitos ni puntos)"""
    symbols = []
    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):
            char = matrix[r][c]
            if not char.isdigit() and char != '.':
                symbols.append((r, c))

    return symbols


def is_number_adjacent_to_symbol(number, symbol_pos):
    """Verifica si un número es adyacente a una posición de símbolo"""
    row, start_col, end_col, _ = number
    symbol_row, symbol_col = symbol_pos

    # Verificar si el símbolo está adyacente a cualquier parte del número
    for num_col in range(start_col, end_col + 1):
        if abs(row - symbol_row) <= 1 and abs(num_col - symbol_col) <= 1:
            return True

    return False


def sum_of_schematic(numbers, symbols):
    total = 0
    symbol_positions = [(r, c) for r, c in symbols]

    for number in numbers:
        # Verificar si este número es adyacente a al menos un símbolo
        for symbol_pos in symbol_positions:
            if is_number_adjacent_to_symbol(number, symbol_pos):
                total += number[3]  # number[3] es el valor numérico
                break  # No necesitamos verificar más símbolos para este número

    return total


numbers = extract_numbers(matrix)
symbols = extract_symbols(matrix)

result1 = sum_of_schematic(numbers, symbols)
logger.info(f"Sum of part numbers: {result1}")
assert (result1 == 532428)

logger.info("Part 2")


def sum_gear_ratio(numbers, symbols):
    total = 0
    symbols = [(r, c) for r, c in symbols]
    for symbol in symbols:
        adjacent_numbers = []
        for number in numbers:
            if is_number_adjacent_to_symbol(number, symbol):
                adjacent_numbers.append(number[3])
        if len(adjacent_numbers) == 2:
            total += adjacent_numbers[0] * adjacent_numbers[1]
    return total


result2 = sum_gear_ratio(numbers, symbols)
logger.info(f"Sum of gear ratios: {result2}")
assert (result2 == 84051670)

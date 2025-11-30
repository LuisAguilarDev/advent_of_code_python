from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    sequences = list()
    for line in contents:
        sequences.append(list(map(int, line.split(" "))))
    return sequences


def get_next_seq(sequence: list[int]) -> list[int]:
    next_sequence = list()
    for number in range(1, len(sequence)):
        next_sequence.append(sequence[number] - sequence[number - 1])
    return next_sequence


def is_zeroed(sequence: list[int]) -> bool:
    for number in sequence:
        if number != 0:
            return False
    return True


def get_next_value(sequence: list[int]) -> int:
    next_seqs = [sequence]
    current_sequence = sequence
    while not is_zeroed(current_sequence):
        next_seq = get_next_seq(current_sequence)
        next_seqs.append(next_seq)
        current_sequence = next_seq
    reversed_seq = list(reversed(next_seqs))
    result = 0
    for num in range(1, len(reversed_seq)):
        result = result + reversed_seq[num][-1]
    return result


def get_past_value(sequence: list[int]) -> int:
    next_seqs = [sequence]
    current_sequence = sequence
    while not is_zeroed(current_sequence):
        next_seq = get_next_seq(current_sequence)
        next_seqs.append(next_seq)
        current_sequence = next_seq
    reversed_seq = list(reversed(next_seqs))
    result = 0
    for num in range(1, len(reversed_seq)):
        result = (result - reversed_seq[num][0]) * - 1
    return result


def get_sum_from_next_values(sequences: list[list[int]]) -> int:
    result = 0
    for seq in sequences:
        result += get_next_value(seq)
    return result


def get_sum_from_past_values(sequences: list[list[int]]) -> int:
    result = 0
    for seq in sequences:
        result += get_past_value(seq)
    return result


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    sequences = parse_data(contents)
    result = get_sum_from_next_values(sequences)
    logger.info(result)
    return 1696140818 == result


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    sequences = parse_data(contents)
    result = get_sum_from_past_values(sequences)
    logger.info(result)
    return 1152 == result


def main():
    logger.info("---- Day 8: Haunted Wasteland ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

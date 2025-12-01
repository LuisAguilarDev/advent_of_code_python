import math

from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    instructions = ""
    network = dict()
    for line in contents:
        if not instructions:
            instructions = line
        elif line.strip():
            node, expr = line.split("=")
            l, r = expr.strip()[1:-1].split(",")
            network[node.strip()] = (l.strip(), r.strip())
    return instructions, network


def count_steps(instructions: str, network: dict) -> int:
    steps = 0
    current_node = "AAA"
    # como detectar un ciclo correectamente, entrar a un node con mismo indice?
    while True:
        if current_node == "ZZZ":
            return steps
        left, right = network[current_node]
        next = instructions[steps % len(instructions)]
        if next == "L":
            current_node = left
        else:
            current_node = right
        steps += 1


def get_start_nodes(network) -> list:
    starts = list()
    for node in network:
        if node.endswith("A"):
            starts.append(node)
    return starts


def get_cycle(start_node: str, instructions: str, network: dict) -> tuple:
    steps = 0
    current_node = start_node
    first_z_found = -1
    cycles = list()
    while True:
        if current_node.endswith("Z"):
            if first_z_found == -1:
                first_z_found = steps
                cycles.append(steps)
            if first_z_found != steps and steps % first_z_found == 0:
                break
        left, right = network[current_node]
        next = instructions[steps % len(instructions)]
        if next == "L":
            current_node = left
        else:
            current_node = right
        steps += 1
    return first_z_found, cycles


def steps_from_a_z(data) -> int:
    instructions, network = data
    logger.info(len(instructions))
    nodes = get_start_nodes(network)
    solution = list()
    for node in nodes:
        cycle_start, steps = get_cycle(node, instructions, network)
        logger.info(
            f"Node: {node}, Cycle start: {cycle_start}, Steps: {steps}")
        solution.append(cycle_start)
    # they only have 1 cycle not intermediate cycles
    # find lcm Least Common Multiple (English) in spanish Mínimo Común Múltiplo (MCM)
    # lcm = solution[0]
    # for i in range(1, len(solution)):
    #     lcm = lcm * solution[i] // math.gcd(lcm, solution[i])
    # return lcm
    return math.lcm(*solution)


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    instructions, network = parse_data(contents)
    return 14893 == count_steps(instructions, network)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    instructions, network = parse_data(contents)
    return 10241191004509 == steps_from_a_z((instructions, network))


def main():
    logger.info("---- Day 8: Haunted Wasteland ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

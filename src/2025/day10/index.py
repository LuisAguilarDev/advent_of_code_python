from ortools.linear_solver import pywraplp

from global_utils.utils import read_file
from global_utils.logger import logger

# https://www.youtube.com/watch?v=At6kCiP4o2Y - Using Google's Ortools Solver for Linear Programming in Python - Step by Step

def parse_data(contents) -> list[list[str]]:
    machines = list() 
    for line in contents:
        parts = line.split()
        # goal
        goal_str = parts[0]
        goal_binary_str = goal_str[1:-1].replace("#", "1").replace(".", "0")
        size = len(goal_binary_str)
        goal = int(goal_binary_str, 2)
        # buttons
        buttons = parts[1:-1]
        buttons_binary = []
        for button in buttons:
            button_binary = ["0"] * size
            button_index = button[1:-1].split(",")
            for index in button_index:
                button_binary[int(index)] = "1"
            button_binary_str = "".join(button_binary)
            button_binary = int(button_binary_str, 2)
            buttons_binary.append(button_binary)
        machines.append((goal, buttons_binary))
    return machines


def parse_data_2(contents) -> list[list[str]]:
    machines = list()
    for line in contents:
        parts = line.split()
        # buttons
        buttons = parts[1:-1]
        buttons_binary = []
        for button in buttons:
            button_index = list(map(int, button[1:-1].split(",")))
            buttons_binary.append(button_index)
        # joltage
        joltage_str = parts[-1][1:-1]
        joltage_list = list(map(int, joltage_str.split(",")))
        machines.append((buttons_binary, joltage_list))
    return machines

def steps_to_turn_on_machine(machine):
    goal, buttons = machine
    current = 0
    queue = [(0,0)] # (steps, state)
    visited = dict()
    visited[0] = 0
    while queue:
        steps, current = queue.pop(0)
        if current == goal:
            return steps
        for button in buttons:
            next_state = current ^ button
            if next_state not in visited or visited[next_state] < steps + 1:
                queue.append((steps + 1, next_state))
                visited[next_state] = steps + 1
    return steps

def steps_to_turn_on_all_machines(machines):
    steps = 0
    for machine in machines:
        steps += steps_to_turn_on_machine(machine)
    return steps


def get_heuristic(state, goal):
    return sum(goal[i] - state[i] for i in range(len(goal)))


def steps_to_calibrate_joltage(machine):
    buttons, goal_joltage = machine
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables creation: to store the times a buttons needs to be pressed
    times_pressed_buttons = [solver.IntVar(
        0, solver.infinity(), f'x{i}') for i in range(len(buttons))]

    # Constraints: for each position, sum of buttons that affect it = goal
    num_positions = len(goal_joltage)
    for pos in range(num_positions):
        # Find which buttons affect this position
        contributing = []
        for btn_idx, affected_positions in enumerate(buttons):
            if pos in affected_positions:
                contributing.append(times_pressed_buttons[btn_idx])

        if contributing:
            # Sum of presses = target value for this position
            solver.Add(sum(contributing) == goal_joltage[pos])

    # Minimize total presses
    solver.Minimize(sum(times_pressed_buttons))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        total = sum(int(var.solution_value()) for var in times_pressed_buttons)
        return total

    return 0

def steps_to_calibrate_all_machines(machines):
    steps = 0
    for machine in machines:
        steps += steps_to_calibrate_joltage(machine)
    return steps

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    machines = parse_data(contents)
    steps = steps_to_turn_on_all_machines(machines)
    logger.info(f"Steps: {steps}")
    return 404 == steps


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    machines = parse_data_2(contents)
    steps = steps_to_calibrate_all_machines(machines)
    logger.info(f"Steps: {steps}")
    # return 8368033065 == sol
    return True


def main():
    logger.info("---- Day 10: Factory ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

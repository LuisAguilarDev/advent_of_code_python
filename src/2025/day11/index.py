from global_utils.utils import read_file
from global_utils.logger import logger

def parse_data(contents) -> list[list[str]]:
    positions = dict()
    for line in contents:
        data = line.split(":")
        positions[data[0]] = data[1].strip().split(" ")
    return positions

def count_paths(positions: dict) -> int:
    start = "you"
    end = "out"
    path_count = 0

    def dfs(current: str, visited: set):
        nonlocal path_count
        # nonlocal is used to use the path_count variable from the outer scope
        if current == end:
            path_count += 1
            return
        for neighbor in positions.get(current, []):
            if neighbor and neighbor in visited:
                continue
            next_visited = visited.copy()
            if neighbor:
                next_visited.add(neighbor)
            dfs(neighbor, next_visited)

    dfs(start, set([start]))
    return path_count

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    positions = parse_data(contents)
    paths = count_paths(positions)
    logger.info(f"Paths: {paths}")
    # return 404 == steps


# def do_part_2() -> bool:
#     logger.info(f"Part 2")
#     contents = read_file("input.txt")
#     machines = parse_data_2(contents)
#     steps = steps_to_calibrate_all_machines(machines)
#     logger.info(f"Steps: {steps}")
#     # return 8368033065 == sol
#     return True


def main():
    logger.info("---- Day 11: Reactor ----")
    result_part_1 = do_part_1()
    # assert (True == result_part_1)
    # result_part_2 = do_part_2()
    # assert (True == result_part_2)


if __name__ == "__main__":
    main()

from global_utils.utils import read_file
from global_utils.logger import logger
from constants.constants import all_directions


def parse_data(contents) -> list[list[str]]:
    grid = list()
    for line in contents:
        grid.append(list(list(line)))
    return grid


def get_total_paper_accesible(grid: list[list[str]]) -> int:
    R = len(grid)
    C = len(grid[0])
    papers_accesible = 0
    for r in range(R):
        for c in range(C):
            # Its not paper
            if grid[r][c] != '@':
                continue
            papers_around = 0
            for dr, dc in all_directions:
                nr, nc = r + dr, c + dc
                # Its outside the grid
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                value = grid[nr][nc]
                if value == '@':
                    papers_around += 1
            if papers_around < 4:
                papers_accesible += 1
    return papers_accesible


def its_removable_paper(grid: list[list[str]], r: int, c: int) -> bool:
    R = len(grid)
    C = len(grid[0])
    # Its not paper
    if grid[r][c] != '@':
        return False
    papers_around = 0
    for dr, dc in all_directions:
        nr, nc = r + dr, c + dc
        # Its outside the grid
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            continue
        value = grid[nr][nc]
        if value == '@':
            papers_around += 1
    if papers_around < 4:
        return True
    return False


def recursive_remotion(grid: list[list[str]], r: int, c: int) -> int:
    R = len(grid)
    C = len(grid[0])
    if grid[r][c] == ".":
        return 0
    # Its not paper
    if grid[r][c] != '@':
        return 0
    papers_removed = 0
    if its_removable_paper(grid, r, c):
        grid[r][c] = '.'
        papers_removed += 1
        for dr, dc in all_directions:
            nr, nc = r + dr, c + dc
            # Its outside the grid
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            papers_removed += recursive_remotion(grid, nr, nc)
    return papers_removed


def get_total_removable_paper(grid: list[list[str]]) -> int:
    R = len(grid)
    C = len(grid[0])
    removable_papers = 0
    for r in range(R):
        for c in range(C):
            if its_removable_paper(grid, r, c):
                grid[r][c] = '.'
                removable_papers += 1
                for dr, dc in all_directions:
                    nr, nc = r + dr, c + dc
                    # Its outside the grid
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue
                    removable_papers += recursive_remotion(
                        grid, nr, nc)
    return removable_papers


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    grid = parse_data(contents)
    count = get_total_paper_accesible(grid)
    logger.info(f"Count of paper accessible: {count}")
    return 1502 == count


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    grid = parse_data(contents)
    total = get_total_removable_paper(grid)
    logger.info(f"Sum Part 2: {total}")
    return 9083 == total


def main():
    logger.info("---- Day 4: Printing Department ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

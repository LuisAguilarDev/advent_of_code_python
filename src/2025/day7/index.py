from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents) -> list[list[str]]:
    grid = list()
    for line in contents:
        grid.append(list(line))
    return grid

def find_start_of_beam(grid: list[list[str]]) -> tuple[int,int]:
    start = "S"
    for c in range(len(grid[0])):
        if start == grid[0][c]:
            return (0,c)
    return (-1,-1)

def count_beam_split(grid: list[list[str]],start:tuple[int,int]) -> int:
    R = len(grid)
    C = len(grid[0])
    queue = [(start[0], start[1])]
    count = 0
    direction_down = [(1,0)]
    direction_sides = [(1,-1),(1,1)]
    while queue:
        r, c = queue.pop(0)
        for dr, dc in direction_down:
            nr, nc = r + dr, c + dc
            # Check bounds and if it's part of the beam
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if grid[nr][nc] == ".":
                grid[nr][nc] = "|"  # Mark as visited
                queue.append((nr, nc))
            if grid[nr][nc] == "^":
                for sdr, sdc in direction_sides:
                    nnr, nnc = r + sdr, c + sdc
                    if nnr < 0 or nnr >= R or nnc < 0 or nnc >= C:
                        continue
                    if grid[nnr][nnc] == ".":
                        grid[nnr][nnc] = "|"  # Mark as visited
                        queue.append((nnr, nnc))
                count += 1
    return count

def add_timeline(queue,r,c, ct):
    # looks for existing entry and increments timeline count
    for i in range(len(queue)):
        if queue[i][0] == r and queue[i][1] == c:
            queue[i] = (r,c,queue[i][2] + ct) # +1?
            return
    queue.append((r,c,ct))


def count_timelines(grid: list[list[str]],start) -> int:
    R = len(grid)
    C = len(grid[0])
    queue = [(start[0], start[1], 1)] # Each entry is (row, col, timeline_count)
    timelines = 0
    direction_down = [(1, 0)]
    direction_sides = [(1, -1), (1, 1)]
    end = R - 1
    while queue:
        r, c, t = queue.pop(0)
        if r == end:
            timelines += t
            continue
        for dr, dc in direction_down:
            nr, nc = r + dr, c + dc
            # Check bounds and if it's part of the beam
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if grid[nr][nc] == ".":
                add_timeline(queue,nr,nc,t)
            if grid[nr][nc] == "^":
                for sdr, sdc in direction_sides:
                    nnr, nnc = r + sdr, c + sdc
                    if nnr < 0 or nnr >= R or nnc < 0 or nnc >= C:
                        continue
                    if grid[nnr][nnc] == ".":
                        add_timeline(queue,nnr,nnc,t)
    return timelines

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    grid = parse_data(contents)
    start = find_start_of_beam(grid)
    logger.info(f"Start of beam at: {start}")
    result = count_beam_split(grid,start)
    logger.info(f"Result Part 1: {result}")
    return 1675 == result


def do_part_2() -> bool:
      logger.info(f"Part 2")
      contents = read_file("input.txt")
      grid = parse_data(contents)
      start = find_start_of_beam(grid)
      logger.info(f"Start of beam at: {start}")
      result = count_timelines(grid,start)
      logger.info(f"Result Part 2: {result}")
#     return 10875057285868 == result


def main():
    logger.info("---- Day 6: Trash Compactor ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    # assert (True == result_part_2)


if __name__ == "__main__":
    main()

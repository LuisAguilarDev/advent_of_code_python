from collections import defaultdict
import heapq
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    adjacency_list = defaultdict(list)
    for line in lines:
        pre, step = line[5], line[36]
        adjacency_list[pre].append(step)
    return adjacency_list


def get_time(lines, workers, base_time):
    adjacency_list = parse_data(lines)

    nodes = set()
    nodes_required = defaultdict(int)

    for step, neighbors in adjacency_list.items():
        nodes.add(step)
        for neighbor in neighbors:
            nodes.add(neighbor)
            nodes_required[neighbor] += 1

    # Cola de prioridad por orden alfabetico para tareas disponibles
    q = []
    for n in nodes:
        if nodes_required[n] == 0:
            heapq.heappush(q, n)

    # Cola de prioridad para workers: (tiempo_fin, nodo)
    w_q = []
    time = 0

    while q or w_q:
        # Asignar tareas a workers disponibles
        while q and len(w_q) < workers:
            task = heapq.heappop(q)
            finish_time = time + base_time + (ord(task) - ord('A') + 1)
            heapq.heappush(w_q, (finish_time, task))

        if not w_q:
            break
        # Extraer el worker que termina primero
        time, done = heapq.heappop(w_q)
        for neighbor in adjacency_list[done]:
            nodes_required[neighbor] -= 1
            if nodes_required[neighbor] == 0:
                heapq.heappush(q, neighbor)

    return time


def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    time = get_time(lines, workers=5, base_time=60)
    logger.info(f"time: {time}")
    return 1107 == time

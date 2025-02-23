import os
import re
import math
import time
from functools import cache

# --- Day 19: Not Enough Minerals ---
file_path = os.path.join(os.path.dirname(__file__), "day19.txt")

with open(file_path, "r") as file:
    contents = file.read().splitlines()

# sprint(contents)
# which blueprint is better to maximize the number of geodes
text = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
          Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

def getData(lines):
    blueprints = dict()
    materials = ["ore","clay","obsidian","geode"]
    for index,line in enumerate(lines):
        requeriments = line.split(":")
        blueprints[index + 1] = []
        bp_req = requeriments[1].split(".")
        for i in range(len(materials)):
            p = re.compile(r"\d+")
            if i <= 1:
                blueprints[index + 1].append([int(p.findall(bp_req[i])[0]),0,0,0])
            if i == 2:
                blueprints[index + 1].append([*map(int,p.findall(bp_req[i])),0,0])
            if i == 3:
                blueprints[index + 1].append([int(p.findall(bp_req[i])[0]),0,int(p.findall(bp_req[i])[1]),0])
    return blueprints

# Part 1

def get_max_robots(blueprint):
    max_cost = [0,0,0,float("inf")]
    for cost in blueprint:
        for i in range(3):
            max_cost[i] = max(max_cost[i],cost[i])
    return max_cost

def getNeighbor(time,c_resources,c_robots,blueprint,max_robots_needed,max_time):
    # this wait until resources are available and the possible robot can be built
    for mat,reqs in enumerate(blueprint):
        can_be_build = True
        w_time = 0
        # if we got the max robots dont build anymore
        if c_robots[mat] == max_robots_needed[mat]: continue
        for req_index,req_res in enumerate(reqs):
            if req_res > 0:
                if c_robots[req_index] == 0:
                    can_be_build = False
                    continue
                w_time = max(w_time,math.ceil((req_res - c_resources[req_index])/c_robots[req_index]))
        if not can_be_build: continue
        # +1 per build time
        w_time += 1
        if (w_time + time) > max_time: continue
        # production_time * robots - spent
        p_resources = list(map(lambda robot: robot * w_time,c_robots))
        n_resources = [x + y - z for x, y, z in zip(p_resources, c_resources,reqs)]
        n_time = time + w_time
        n_robots = [*c_robots]
        n_robots[mat] += 1
        yield [n_time,n_resources,n_robots]
    # or just wait until the end
    if c_robots[3] > 0:
        yield getEnd(time,c_robots,c_resources,max_time)

# def getEnd(time,c_robots,c_resources,max_time):
#     wait_to_end = max_time - time
#     p_resources = list(map(lambda robot: robot * wait_to_end,c_robots))
#     n_resources = [x + y for x, y in zip(p_resources, c_resources)]
#     return max_time,n_resources,c_robots

def getEnd(time,c_robots,c_resources,max_time):
    wait_to_end = max_time - time
    n_resources = [c_resources[i] + c_robots[i]*wait_to_end for i in range(4)]
    return max_time,n_resources,c_robots


def dfs(resources,robots,blueprint,max_time):
    maxgeode = 0
    visited = set()
    stack = [[0,resources,robots]]
    max_robots_needed = get_max_robots(blueprint)
    while stack:
        time,c_resorces,c_robots = stack.pop()
        if time == max_time:
            maxgeode = max(maxgeode,c_resorces[3]) # ["ore","clay","obsidian","geode"]
            continue
        for n_time,n_resources,n_robots in getNeighbor(time,c_resorces,c_robots,blueprint,max_robots_needed,max_time):
            if (n_time,*n_resources,*n_robots) not in visited:
                visited.add((n_time,*n_resources,*n_robots))
                stack.append([n_time,n_resources,n_robots])
    return maxgeode

def getAllQualityLevels(blueprints,max_time=24):
    resources = [0,0,0,0]
    robots = [1,0,0,0]
    total = 0
    for bp_n,blueprint in enumerate(blueprints.values()):
        max_geode = dfs(resources,robots,blueprint,max_time)
        total += (bp_n + 1) * max_geode
    return total

start_time = time.perf_counter() 
print("maxGeode:",getAllQualityLevels(getData(contents)))
end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.4f} seconds")

# Part 2

# 11 mins
# def getAllQualityLevels2(blueprints, max_time=32):
#     """
#     For Part 2, compute the product of maximum geodes for the first three blueprints.
#     """
#     initial_resources = [0, 0, 0, 0]
#     initial_robots = [1, 0, 0, 0]
#     total = 1
#     for bp in range(1, 4):
#         max_geodes = dfs(initial_resources, initial_robots, blueprints[bp], max_time)
#         print(f"Blueprint {bp}: max geodes = {max_geodes}")
#         total *= max_geodes
#     return total
# start_time = time.perf_counter() 
# print("maxGeode:",getAllQualityLevels2(getData(contents)))
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.4f} seconds")

# caching isn't enought cause resource parameter
# caching needs hashable parameters list are not allowed
# resources is a parameter highly variable 
#2 Caching and pruning
def upper_bound(current_time, geode, r_geode, max_time):
    """
    Compute an optimistic upper bound of geodes achievable from the current state.
    This assume that from now on we can build a new geode robot every minute.
    """
    remaining = max_time - current_time
    return geode + r_geode * remaining + (remaining * (remaining - 1)) // 2

def recursive_dfs(resources, robots, blueprint, max_time, c_time=0):
    max_robots_needed = get_max_robots(blueprint)
    global_best = 0  # We'll update this as we explore states

    @cache
    def rec(state):
        # Without nonlocal, a new local variable would be created in rec(), without affecting the global_best of recursive_dfs.
        nonlocal global_best
        time_state, ore, clay, obs, geode, r_ore, r_clay, r_obs, r_geode = state

        # Clamp resources: no need to store more than what can be spent in remaining time.
        remaining = max_time - time_state
        ore = min(ore, max_robots_needed[0] * remaining)
        clay = min(clay, max_robots_needed[1] * remaining)
        obs = min(obs, max_robots_needed[2] * remaining)
        state = (time_state, ore, clay, obs, geode, r_ore, r_clay, r_obs, r_geode)

        # Prune if even an optimistic estimate cannot beat the best found so far.
        if upper_bound(time_state, geode, r_geode, max_time) <= global_best:
            return geode

        # Base case: time has run out.
        if time_state >= max_time:
            global_best = max(global_best, geode)
            return geode

        best_local = geode
        current_resources = [ore, clay, obs, geode]
        current_robots = [r_ore, r_clay, r_obs, r_geode]

        # Try building each possible robot.
        for n_time, n_resources, n_robots in getNeighbor(time_state, current_resources, current_robots, blueprint, max_robots_needed, max_time):
            new_state = (
                n_time,
                n_resources[0],
                n_resources[1],
                n_resources[2],
                n_resources[3],
                n_robots[0],
                n_robots[1],
                n_robots[2],
                n_robots[3]
            )
            candidate = rec(new_state)
            best_local = max(best_local, candidate)
            global_best = max(global_best, best_local)

        # Also consider simply waiting until max_time.
        wait_geodes = getEnd(time_state, current_resources, current_robots, max_time)[2][3]
        best_local = max(best_local, wait_geodes)
        global_best = max(global_best, best_local)
        return best_local

    # turn hashable
    init_state = (
        c_time,
        resources[0],
        resources[1],
        resources[2],
        resources[3],
        robots[0],
        robots[1],
        robots[2],
        robots[3]
    )
    return rec(init_state)

def getAllQualityLevels2(blueprints, max_time=32):
    initial_resources = [0, 0, 0, 0]
    initial_robots = [1, 0, 0, 0]
    total = 1
    for bp in range(1, 4):
        max_geodes = recursive_dfs(initial_resources, initial_robots, blueprints[bp], max_time)
        print(f"Blueprint {bp}: max geodes = {max_geodes}")
        total *= max_geodes
    return total

start_time = time.perf_counter()
result = getAllQualityLevels2(getData(contents))
end_time = time.perf_counter()
print("Max Geodes (Part 2):", result)
print(f"Execution time: {end_time - start_time:.4f} seconds")

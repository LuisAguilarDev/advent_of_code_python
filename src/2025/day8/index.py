from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents) -> list[list[str]]:
    positions = list()
    for line in contents:
        positions.append(tuple(line.split(",")))
    return positions

def get_euclidean_distance(pos1: tuple[int,int,int], pos2: tuple[int,int,int]) -> float:
    return ((int(pos1[0]) - int(pos2[0])) ** 2 + (int(pos1[1]) - int(pos2[1])) ** 2 + (int(pos1[2]) - int(pos2[2])) ** 2) ** 0.5

def build_distances(positions: list[tuple[str,str]]) -> dict[tuple[str,str,str,str], float]:
    distances = list()
    visited = set()
    for position in positions:
        x,y,z = position
        for other_position in positions:
            if other_position == position:
                continue
            # start to avoid duplicate calculations
            hash1 = tuple([*position, *other_position])
            hash2 = tuple([*other_position, *position])
            if hash1 in visited or hash2 in visited:
                continue
            visited.add(hash1)
            visited.add(hash2)
            # end to avoid duplicate calculations
            ox,oy,oz = other_position
            dist = get_euclidean_distance( (int(x),int(y),int(z)), (int(ox),int(oy),int(oz)) )
            distances.append(((dist,*position, *other_position)))
    return distances


def get_circuits(positions: list[tuple[str, str, str]], verify_connections: int) -> list:
    """
    Traverse the smallest distances first, building circuits until the number of connections to verify is reached
    """
    circuits = set()
    for position in positions:
        circuits.add(frozenset([position]))
    remaining_connections = verify_connections
    distances = sorted(build_distances(positions))
    for data in distances:
        remaining_connections -= 1
        _, x1, y1, z1, x2, y2, z2 = data
        if remaining_connections < 0:
            return circuits
        pos1 = (x1,y1,z1)
        pos2 = (x2,y2,z2)
        circuit1 = None
        circuit2 = None
        for circuit in circuits:
            if pos1 in circuit:
                circuit1 = circuit
            if pos2 in circuit:
                circuit2 = circuit
        # merge circuits
        if circuit1 != circuit2:
            new_circuit = circuit1.union(circuit2)
            circuits.remove(circuit1)
            circuits.remove(circuit2)
            circuits.add(new_circuit)
    return circuits


def get_last_connection(positions: list[tuple[str, str, str]]) -> list:
    """
    Traverse all distances until all positions are connected into a single circuit,
    return the product of the coordinates of the last two positions connected
    """
    circuits = set()
    for position in positions:
        circuits.add(frozenset([position]))
    distances = sorted(build_distances(positions))
    logger.info(f"Total distances: {len(distances)}")
    for data in distances:
        _, x1, y1, z1, x2, y2, z2 = data
        pos1 = (x1, y1, z1)
        pos2 = (x2, y2, z2)
        circuit1 = None
        circuit2 = None
        for circuit in circuits:
            if pos1 in circuit:
                circuit1 = circuit
            if pos2 in circuit:
                circuit2 = circuit
        # merge circuits
        if circuit1 != circuit2:
            new_circuit = circuit1.union(circuit2)
            circuits.remove(circuit1)
            circuits.remove(circuit2)
            circuits.add(new_circuit)
            if len(circuits) == 1:
                x1,y1,z1 = pos1
                x2,y2,z2 = pos2
                return int(x1) * int(x2)

                
    return circuits

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    positions = parse_data(contents)
    circuits = get_circuits(positions,1000)
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    sol = 1
    for i, circuit in enumerate(circuits):
        sol *= len(circuit)
        if i == 2:
            break
    logger.info(f"Solution: {sol}")
    return 117000 == sol


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    positions = parse_data(contents)
    sol = get_last_connection(positions)
    logger.info(f"Solution: {sol}")
    return 8368033065 == sol


def main():
    logger.info("---- Day 8: Playground ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()

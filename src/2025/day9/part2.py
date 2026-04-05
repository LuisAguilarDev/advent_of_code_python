from global_utils.utils import read_file
from global_utils.logger import logger
from .part1 import parse_data, is_diagonal, get_area
import matplotlib.pyplot as plt
import os

def get_valid_positions(positions):
    valid_pos = set()
    n = len(positions)
    for i in range(n):
        r1, c1 = positions[i]
        r2, c2 = positions[(i + 1) % n]
        valid_pos.add((r1, c1))
        if r1 == r2:
            for c in range(min(c1, c2), max(c1, c2) + 1):
                valid_pos.add((r1, c))
        else:
            for r in range(min(r1, r2), max(r1, r2) + 1):
                valid_pos.add((r, c1))
    return valid_pos

def get_corners(pos1,pos2):
    r1,c1 = pos1
    r2,c2 = pos2
    pos3 = r1, c2
    pos4 = r2, c1
    return set([pos1,pos2,pos3,pos4])


def is_range_contained(target_min, target_max, ranges):
    """Check if (target_min, target_max) is contained within any range in the list."""
    return any(r_min <= target_min and r_max >= target_max for r_min, r_max in ranges)


def is_valid_rectangle(min_r, max_r, min_c, max_c, valid_ranges):
    row_ranges = valid_ranges["row_ranges"]
    col_ranges = valid_ranges["col_ranges"]
    if not is_range_contained(min_r, max_r, col_ranges[min_c]):
        return False
    if not is_range_contained(min_r, max_r, col_ranges[max_c]):
        return False
    if not is_range_contained(min_c, max_c, row_ranges[min_r]):
        return False
    if not is_range_contained(min_c, max_c, row_ranges[max_r]):
        return False
    return True


def get_biggest_area_part2(positions: list[tuple[str, str]], valid_ranges:dict) -> tuple:
    big_area = -1
    n = len(positions)
    total = n * (n - 1) // 2
    reviewed = 0
    for i in range(n):
        for j in range(i + 1, n):
            reviewed += 1
            print(f"\r{reviewed}/{total} ({reviewed * 100 // total}%)", end="", flush=True)
            pos1 = positions[i]
            pos2 = positions[j]
            if is_diagonal(pos1, pos2):
                area = get_area(pos1, pos2)
                if area < big_area:
                    continue
                r1, c1 = pos1
                r2, c2 = pos2
                min_r, max_r = min(r1, r2), max(r1, r2)
                min_c, max_c = min(c1, c2), max(c1, c2)
                if is_valid_rectangle(min_r, max_r, min_c, max_c, valid_ranges):
                    big_area = area
    return big_area


def plot_valid_positions(positions, valid_positions, big_rects=None, filename='valid_positions.png'):
    from matplotlib.patches import Rectangle
    vp_rows = [r for r, _ in valid_positions]
    vp_cols = [c for _, c in valid_positions]
    p_rows = [r for r, _ in positions]
    p_cols = [c for _, c in positions]

    _, ax = plt.subplots(figsize=(12, 10))
    ax.scatter(vp_cols, vp_rows, c='blue', s=2, label='valid positions')
    ax.scatter(p_cols, p_rows, c='red', s=10, label='original positions')

    if big_rects:
        big_rects_sorted = sorted(big_rects, key=lambda x: x[0], reverse=True)
        for idx, (area, min_r, min_c, max_r, max_c) in enumerate(big_rects_sorted):
            letter = chr(ord('A') + idx) if idx < 26 else str(idx)
            width = max_c - min_c
            height = max_r - min_r
            rect = Rectangle((min_c, min_r), width, height,
                              linewidth=1.5, edgecolor='black', facecolor='black', alpha=0.3)
            ax.add_patch(rect)
            cx = min_c + width / 2
            cy = min_r + height / 2
            ax.text(cx, cy, f"{letter}\n{area:,}", color='black',
                    fontsize=7, ha='center', va='center', fontweight='bold')

    ax.invert_yaxis()
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.legend()
    ax.set_title('Valid Positions Grid')
    output_path = os.path.join(os.path.dirname(__file__), filename)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    logger.info(f"Plot saved to {output_path}")

def point_in_polygon(r, c, polygon):
    n = len(polygon)
    inside = False
    j = n - 1
    for i in range(n):
        ri, ci = polygon[i]
        rj, cj = polygon[j]
        if ((ri > r) != (rj > r)) and (c < (cj - ci) * (r - ri) / (rj - ri) + ci):
            inside = not inside
        j = i
    return inside

def build_spans(values, coord=None, axis=None, polygon=None):
    sorted_vals = sorted(values)
    if not sorted_vals:
        return []
    # Find consecutive groups
    groups = []
    start = end = sorted_vals[0]
    for v in sorted_vals[1:]:
        if v == end + 1:
            end = v
        else:
            groups.append((start, end))
            start = end = v
    groups.append((start, end))

    if len(groups) == 1 or polygon is None:
        return groups

    # Merge groups where the gap is OUTSIDE the polygon (staircase step)
    merged = [groups[0]]
    for g in groups[1:]:
        gap_mid = (merged[-1][1] + g[0]) // 2
        if axis == 'row':
            inside = point_in_polygon(coord, gap_mid, polygon)
        else:
            inside = point_in_polygon(gap_mid, coord, polygon)
        if inside:
            merged[-1] = (merged[-1][0], g[1])  # interior gap → merge
        else:
            merged.append(g)        # exterior gap → separate spans
    return merged

def get_valid_ranges(valid_positions, positions):
    """
    Build valid ranges for each row and column.

    Input: set of valid positions (r, c), original polygon vertices
    Output: dict with:
        - "row_ranges": row -> list of (start_col, end_col) spans
        - "col_ranges": col -> list of (start_row, end_row) spans
    Uses ray casting to determine if gaps between boundary groups
    are inside (interior gap → separate spans) or outside (staircase → merge).
    """
    rows = {}
    cols = {}
    for r, c in valid_positions:
        rows.setdefault(r, []).append(c)
        cols.setdefault(c, []).append(r)
    return {
        "row_ranges": {r: build_spans(cs, coord=r, axis='row', polygon=positions) for r, cs in rows.items()},
        "col_ranges": {c: build_spans(rs, coord=c, axis='col', polygon=positions) for c, rs in cols.items()},
    }

def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("data/input.txt")
    positions = parse_data(contents)
    valid_positions = get_valid_positions(positions)
    valid_ranges = get_valid_ranges(valid_positions, positions)
    plot_valid_positions(positions, valid_positions, filename='valid_positions_start.png')
    sol = get_biggest_area_part2(positions, valid_ranges)
    logger.info(f"Solution: {sol}")
    return 1560299548 == sol

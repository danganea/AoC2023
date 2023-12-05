from collections import defaultdict
import functools
import operator

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def compute_neighbors(row, start, end, row_len, col_len):
    neighbor_positions = set()

    #     N,  NE, E, SE, S, SW, W, NW
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    assert len(dx) == 8
    assert len(dy) == 8

    for i in range(start, end + 1):
        for diff_x, diff_y in zip(dx, dy):
            new_pos_x = row + diff_x
            new_pos_y = i + diff_y

            if not (0 <= new_pos_x < row_len and 0 <= new_pos_y < col_len):
                continue

            neighbor_positions.add((new_pos_x, new_pos_y))

    return neighbor_positions


def _main_part_1(input):
    grid = input.split("\n")
    # rows
    n = len(grid)
    # columns
    m = len(grid[0])
    print(n, m)

    sum = 0
    for i in range(n):
        start = None
        for j in range(m):
            if grid[i][j].isdigit():
                if start is None:
                    start = j
            else:
                if start is not None:
                    end = j - 1
                    if any(
                        (not grid[i][j].isdigit()) and grid[i][j] != "."
                        for (i, j) in compute_neighbors(i, start, end, n, m)
                    ):
                        sum += int(grid[i][start : end + 1])

                start = None

        if start is not None:
            end = m - 1
            if any(
                ((not grid[i][j].isdigit()) and grid[i][j] != ".")
                for (i, j) in compute_neighbors(i, start, end, n, m)
            ):
                sum += int(grid[i][start : end + 1])

            start = None

    print(sum)
    return sum


def _main_part_2(input):
    grid = input.split("\n")
    # rows
    n = len(grid)
    # columns
    m = len(grid[0])

    numbers_per_gear = defaultdict(list)

    for i in range(n):
        start = None
        for j in range(m):
            if grid[i][j].isdigit():
                if start is None:
                    start = j
            else:
                if start is not None:
                    end = j - 1
                    number = int(grid[i][start : end + 1])

                    neighbors = compute_neighbors(i, start, end, n, m)

                    for nei_x, nei_y in neighbors:
                        if grid[nei_x][nei_y] == "*":
                            numbers_per_gear[(nei_x, nei_y)].append(number)

                    start = None

        if start is not None:
            end = m - 1
            number = int(grid[i][start : end + 1])

            neighbors = compute_neighbors(i, start, end, n, m)

            for nei_x, nei_y in neighbors:
                if grid[nei_x][nei_y] == "*":
                    numbers_per_gear[(nei_x, nei_y)].append(number)

            start = None

    result = sum(functools.reduce(operator.mul, l, 1) for l in numbers_per_gear.values() if len(l) == 2)

    print(result)
    return result


if __name__ == "__main__":
    # with open("src/day3/input.in") as f:
    # with open("src/day3/test_input.in") as f:
    # input = f.read()

    _main_part_1(input)
    _main_part_2(input)
